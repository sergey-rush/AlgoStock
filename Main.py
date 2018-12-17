import os
import csv
import matplotlib.pyplot as plt
from Core.Stock import Stock
from Data.DataManager import DataManager

dm = DataManager()
data_manager = dm.get_instance()

issuer_list = data_manager.get_issuers()
for issuer in issuer_list:
    print("\n{} {} {}\n".format(issuer.id, issuer.ticker, issuer.name))
    stock_list = data_manager.get_stocks_by_issuer_id(issuer.id)
    high_stocks = []
    for stock in stock_list:
        print("{} {} {} {} {} {} {} {} {}".format(stock.id, stock.ticker, stock.per, stock.trade_date, stock.open, stock.high, stock.low, stock.close, stock.volume))
        rpl = Stock.nth_repl_all(stock.high, '.', '', 2)
        high_stocks.append(float(rpl))
    plt.plot(high_stocks)
    plt.show()

print("\nCompleted")

