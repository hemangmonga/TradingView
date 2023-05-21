import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from main import TvDatafeed, Interval
import pandas_ta as ta

from Candle import Candle


def get_prev_candle_timestamp(timeframe):
    now = datetime.now()

    rounded_time = now - timedelta(seconds=now.second, microseconds=now.microsecond)
    rounded_time -= timedelta(
        minutes=(rounded_time.minute % timeframe) + timeframe) if rounded_time.minute % timeframe != 0 else timedelta(
        minutes=timeframe)

    return pd.Timestamp(rounded_time)


class TradingviewClient:

    def __init__(self, trading_symbol, market):
        # print(username, password)
        self.tv = TvDatafeed()
        self.trading_symbol = trading_symbol
        self.market = market

    def get_data(self, timeframe=5, bars=5000, last_row=0, supertrend_length=10, supertrend_multiplier=1):
        while 1:
            try:
                if timeframe == 1:
                    data = self.tv.get_hist(self.trading_symbol, self.market, interval=Interval.in_1_minute,
                                            n_bars=bars)
                    data['color'] = np.where(data['open'] < data['close'], 'green', 'red')

                elif timeframe == 5:
                    data = self.tv.get_hist(self.trading_symbol, self.market, interval=Interval.in_5_minute,
                                            n_bars=bars)
                    data["EMA5"] = ta.ema(data.close, length=5)
                    data = data.fillna(99999)
                    data['alert_pe'] = np.where(data['EMA5'] <= data['low'], True, False)
                    data['alert_ce'] = np.where(data['EMA5'] >= data['high'], True, False)
                    data['color'] = np.where(data['open'] < data['close'], 'green', 'red')

                elif timeframe == 15:
                    data = self.tv.get_hist(self.trading_symbol, self.market, interval=Interval.in_15_minute,
                                            n_bars=bars)
                    data["EMA5"] = ta.ema(data.close, length=5)
                    data = data.fillna(99999)
                    data['alert_pe'] = np.where(data['EMA5'] <= data['low'], True, False)
                    data['alert_ce'] = np.where(data['EMA5'] >= data['high'], True, False)
                    data['color'] = np.where(data['open'] < data['close'], 'green', 'red')

                data = data.drop('symbol', axis=1)
                data = data.reset_index()
                data.ta.supertrend(length=supertrend_length, multiplier=supertrend_multiplier, append=True)
                data.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume', 'EMA5',
                                'alert_pe', 'alert_ce', 'color', 'supertrend_value', 'supertrend_direction',
                                'supertrend_green', 'supertrend_red']
                if last_row:
                    timestamp = get_prev_candle_timestamp(timeframe)
                    data = data[data['datetime'] == timestamp]
                    if data.empty:
                        print("\nmarket is closed!\n")
                break
            except Exception as e:
                print('error in get_data: ', e)
                time.sleep(0.2)
                pass

        return data

    def LTP(self, timeframe=5):
        data = self.get_data(timeframe=timeframe, last_row=0, supertrend_multiplier=1)
        return data.tail(1).iloc[0].close

    def prev_candle(self, timeframe=5):
        data = self.get_data(timeframe=timeframe, last_row=1, supertrend_multiplier=1)
        prev = Candle(data)
        return prev

    def curr_candle(self, timeframe=5):
        data = self.get_data(timeframe=timeframe, last_row=0, supertrend_multiplier=1)
        data = data.tail(1).iloc[0]
        curr = Candle(data)
        return curr
