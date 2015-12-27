#!/usr/bin/python

from classes.stock import Stock
from prettytable import PrettyTable


class Market:

    def __init__(self, nbrStocks=10):
        self.stocks = [Stock() for i in range(nbrStocks)]

    def getAllStocks(self):
        return self.stocks

    def increaseTime(self):
        for s in self.stocks:
            s.changeByTime()

    def printMarketText(self):
        t = PrettyTable(['Tag', 'Rate', 'Perf. day',
                         'Perf. week', 'Perf. month', 'Perf. year', 'Perf. total'])
        for s in self.stocks:
            t.add_row([s.id, s.getLastValue(), s.getPerformance(
                1), s.getPerformance(7), s.getPerformance(30), s.getPerformance(365), s.getTotalPerformance()])

        return t
