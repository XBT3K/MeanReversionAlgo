# Trading Algorithm

This repository contains a trading algorithm that is designed to execute trades automatically based on certain market conditions. It is written in Python and uses the Oanda API to get real-time market data and execute trades.

## Getting Started

To use this algorithm, you will need to sign up for an Oanda account and obtain an API key. You will also need to install the required Python packages. To do this, run the following command:

pip install -r requirements.txt

You will also need to create a `config.ini` file with your API key and other configuration options. An example `config.ini` file can be found in this repository.

## Usage

To use the algorithm, simply run the `main.py` file:

python main.py

The algorithm will connect to the Oanda API and start listening for market data. When certain market conditions are met, it will automatically execute trades according to the configured strategy.

## Backtesting

To backtest the algorithm, you can use the `backtesting.py` file. This file simulates market conditions and allows you to test the algorithm's performance under various conditions. To use the file, simply run:

python backtesting.py

## Configuration

The `config.ini` file contains various configuration options that can be used to customize the algorithm's behavior. The following options are available:

- `account_id`: The ID of the Oanda account that will be used to execute trades.
- `access_token`: The access token for your Oanda API account.
- `environment`: The environment to use for the Oanda API. This can be either `live` or `practice`.
- `currency_pairs`: A comma-separated list of currency pairs to trade.
- `strategy`: The name of the strategy to use for trading.
- `stop_loss`: The stop loss in pips for each trade.
- `take_profit`: The take profit in pips for each trade.

## Contributing

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
