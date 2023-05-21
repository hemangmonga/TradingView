# TradingView Package

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview
The TradingView package is an unofficial API that allows you to fetch live and historical data from TradingView. It provides convenient methods to retrieve data such as historical candlestick data, last traded price, and information about the previous and current candle.

With this package, you can easily integrate TradingView data into your Python applications, trading bots, or data analysis projects. The package supports various timeframes and provides additional features like calculating EMA values, setting alert flags, determining candle colors, and appending supertrend values.

## Installation
To install the TradingView package, you can use pip and specify the package index:

```shell
pip install -i https://test.pypi.org/simple/ TradingView
```

After installing the package, you also need to install the required dependencies. You can do this by running the following command:

```shell
pip install -r https://github.com/hemangmonga/TradingView/blob/master/requirements.txt
```

Make sure you have Python and pip installed on your system before proceeding with the installation.

## Usage
To use the TradingView package, you need to import the `TradingviewClient` class from the package and create an instance of it. Then, you can call various methods to fetch data or perform specific operations. Here are some examples:

```python
from TradingView import TradingviewClient

# Instantiate TradingviewClient
nifty = TradingviewClient(trading_symbol="NIFTY", market="NSE")

# Get historical data
data = nifty.get_data(timeframe=5, bars=5000, last_row=0)

# Get last traded price
ltp = nifty.LTP(timeframe=5)

# Get previous candle
prev_candle = nifty.prev_candle(timeframe=5)

# Get current candle
curr_candle = nifty.curr_candle(timeframe=5)
```

Please note that you should replace `"NIFTY"` and `"NSE"` with the appropriate trading symbol and market values you want to fetch data for. Adjust the parameters of the methods according to your requirements.

## Documentation
You can refer to DOCUMENTATION.md file to understand the functionality and usage of different methods. Additionally, you can explore the code provided in the `candle.py` and `TradingviewClient.py` files to gain insights into the implementation.

## Contributing
Contributions to the TradingView package are welcome! If you encounter any bugs, have feature requests, or want to contribute code improvements, please follow the guidelines outlined in the CONTRIBUTING.md file of this repository. Your contributions will be greatly appreciated.

## License
The TradingView package is distributed under the MIT License. For more information, please refer to the LICENSE file.

## Contact
If you have any questions, suggestions, or need further assistance, you can reach out to me, via hemangmonga@gmail.com. Feel free to provide feedback or report any issues you encounter.

## Acknowledgments
- [TradingView](https://www.tradingview.com/): The package leverages the TradingView platform to fetch live and historical data.

Certainly! Here are a few common questions that you can include in the `FAQ.md` file:

# Frequently Asked Questions

## Question 1

**Q: What markets are supported by the TradingView package?**
- A: The TradingView package supports various markets. You can specify the market parameter when creating a `TradingviewClient` instance to fetch data for a specific market.

## Question 2

**Q: What to do if I get this error?**
- A: Run the following commands
- ```shell
pip uninstall websocket
pip uninstall websocket-client
pip install websocket==0.2.1
pip install websocket-client==0.44.0

```

## Question 3
**Q: How can I fetch historical data using the TradingView package?**
- A: To fetch historical candlestick data, you can use the `get_data` method of the `TradingviewClient` class. You need to specify the desired timeframe, number of bars, and other parameters to retrieve the data.

## Question 4
**Q: How can I get the last traded price for a symbol?**
- A: You can use the `LTP` method of the `TradingviewClient` class, specifying the timeframe. This method returns the last traded price as a floating-point number.

## Question 5
**Q: How can I access information about the previous and current candle?**
- A: The `prev_candle` method of the `TradingviewClient` class provides information about the previous candle, including open, high, low, close, EMA values, alert flags, and supertrend values. Similarly, the `curr_candle` method gives information about the current candle.


