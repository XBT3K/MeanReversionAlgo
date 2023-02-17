# Forex Mean Reversion Trading Algorithm

This project contains a trading algorithm that uses mean reversion to trade the EUR/USD forex pair. The algorithm calculates the z-score of the close price based on a rolling mean and standard deviation, and enters a trade when the z-score reaches an oversold or overbought threshold. The algorithm is executed using the OANDA API.

## Getting Started

### Prerequisites

To run this project, you will need the following:

* Python 3
* `oandapyV20` Python package
* OANDA API access token
* OANDA account ID

### Installing

1. Clone this repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Create a `config.ini` file with your OANDA API access token and account ID. The file should have the following format:

### Usage

To run the algorithm, run `python main.py` in your terminal.

### Backtesting

You can backtest the algorithm using historical data by running `python backtest.py`. The backtest uses data from the past year and simulates trades based on the same mean reversion strategy used in the live trading algorithm.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
