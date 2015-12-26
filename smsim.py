#!/usr/bin/python
import matplotlib.pyplot as plt
import time
import sys
import curses

from stock import Stock
#------------------------------------------

if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    timeArray = [0]
    s = Stock("Test", "T", 100)
    for i in xrange(1,1000):
        timeArray.append(i)
        s.changeByTime()
        stdscr.addstr(0, 0, s.getPerformance())
        time.sleep(0.5);
        stdscr.refresh()


print s.getPerformance()


#plt.plot(timeArray, s.getAllValues())
plt.plot([0, 6, 0, 20], [0,1,2,3])
plt.plot([1, 7, 1, 21], [0,1,2,3])
plt.show()
