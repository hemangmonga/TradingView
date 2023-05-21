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
