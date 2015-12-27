#!/usr/bin/python
import matplotlib.pyplot as plt
import time
import sys
import curses

from classes.stock import Stock
from classes.market import Market
#------------------------------------------

if __name__ == "__main__":
    #stdscr = curses.initscr()
    #curses.echo()
    #curses.cbreak()
    #curses.nocbreak()

    timeArray = [0]
    s = Stock("Test", "T", 100)
    m = Market()
    for i in xrange(1, 2000):
        timeArray.append(i)
        # s.changeByTime()
        m.increaseTime()
        #stdscr.addstr(0, 0, m.printMarketText().get_string())
        #stdscr.refresh()
        #time.sleep(0.5)

    #curses.endwin()
    print m.printMarketText()

    for i in m.stocks:
        plt.plot(timeArray, i.getAllValues())

    plt.show()
