#!/usr/bin/python
import matplotlib.pyplot as plt

from stock import Stock
#------------------------------------------

timeArray = [0]
s = Stock("Test", "T", 100)
for i in xrange(1,1000):
    timeArray.append(i)
    s.changeByTime()


#print s.getAllValues()


plt.plot(timeArray, s.getAllValues())
#plt.axis([0, 6, 0, 20])
plt.show()
