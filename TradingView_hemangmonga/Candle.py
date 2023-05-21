class Candle:
    def __init__(self, data):
        self.open = data.open
        self.high = data.high
        self.low = data.low
        self.close = data.close
        self.EMA5 = data.EMA5
        self.EMA_alert_pe = data.alert_pe
        self.EMA_alert_ce = data.alert_ce
        self.color = data.color
        self.supertrend_value = data.supertrend_value
        self.supertrend_direction = data.supertrend_direction
        self.supertrend_green = data.supertrend_green
        self.supertrend_red = data.supertrend_red


