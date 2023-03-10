import pandas as pd
import numpy as np
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.orders as orders
import time
import configparser


class MeanReversion:
    def __init__(self, symbol, window_size, overbought_threshold, oversold_threshold, units):
        self.symbol = symbol
        self.window_size = window_size
        self.overbought_threshold = overbought_threshold
        self.oversold_threshold = oversold_threshold
        self.data = pd.DataFrame()
        self.oanda = oandapyV20.API(access_token=config['oanda']['access_token'], environment=config['oanda']['environment'])
        self.units = units
        
    def get_data(self):
        params = {"count": self.window_size, "granularity": "M5"}
        r = instruments.InstrumentsCandles(instrument=self.symbol, params=params)
        self.oanda.request(r)
        raw_data = r.response.get("candles")
        data = pd.DataFrame([{"time": x["time"], "close": float(x["mid"]["c"])} for x in raw_data])
        data.set_index("time", inplace=True)
        data.index = pd.DatetimeIndex(data.index)
        self.data = self.data.append(data)
        self.data = self.data[~self.data.index.duplicated(keep='last')]
        
    def check_signal(self):
        if len(self.data) < self.window_size:
            return
        sma = self.data["close"].rolling(window=self.window_size).mean()
        std = self.data["close"].rolling(window=self.window_size).std()
        z_score = (self.data["close"] - sma) / std
        last_z_score = z_score[-1]
        if last_z_score > self.overbought_threshold:
            return -1 # Sell signal
        elif last_z_score < self.oversold_threshold:
            return 1 # Buy signal
        else:
            return 0 # No signal
        
    def execute_trade(self, signal):
        if signal == 0:
            return
        params = {
            "order": {
                "instrument": self.symbol,
                "units": self.units * signal,
                "type": "MARKET"
            }
        }
        r = orders.OrderCreate(accountID=config['oanda']['account_id'], data=params)
        self.oanda.request(r)
        print(r.response)


def run_live_trading():
    mean_reversion = MeanReversion(symbol=config['oanda']['symbol'], window_size=int(config['mean_reversion']['window_size']), 
                                   overbought_threshold=float(config['mean_reversion']['overbought_threshold']), 
                                   oversold_threshold=float(config['mean_reversion']['oversold_threshold']), 
                                   units=int(config['oanda']['units']))
    while True:
        try:
            mean_reversion.get_data()
            signal = mean_reversion.check_signal()
            mean_reversion.execute_trade(signal)
            time.sleep(60)
        except:
            print("Error occurred.")


def run_backtesting():
    mean_reversion = MeanReversion(symbol=config['oanda']['symbol'], window_size=int(config['mean_reversion']['window_size']), 
                                   overbought_threshold=float(config['mean_reversion']['overbought_threshold']), 
                                   oversold_threshold=float(config['mean_reversion']['oversold_threshold']), 
                                   units=int(config['oanda']['units']))
    historical_data = pd.read_csv(config['backtesting']['data_file'], index_col=0, parse_dates=True)
    for index
