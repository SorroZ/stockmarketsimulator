#!/usr/bin/python

import random
import math


class Stock:

    NBR_OF_STOCKS = -1

    def __init__(self, name="Unknown", tag="-", startValue=100, risk=5):
        self.name = name
        self.tag = tag
        self.values = [startValue]
        self.derivate = [0]
        self.lifeLenght = 1
        # 0 = only negetive, 1 = only positive
        self.effectivness = random.uniform(0.49, 0.51)
        self.risk = risk
        self.bankruptcy = False
        self.id = Stock.NBR_OF_STOCKS
        Stock.NBR_OF_STOCKS += 1

# GET ATTRIBUTES
# ------------------------------------------------------------------------------
    def getLastValue(self):
        last = len(self.values) - 1
        return round(self.values[last], 2)

    def getAllValues(self):
        return self.values

# OPERATIONS
# ------------------------------------------------------------------------------

    # private
    def deviationPart(self):
        x = random.uniform(0, 7)  # the x value
        c = (self.risk / float(10)) * random.uniform(0, 0.5) * \
            math.exp(-x) * random.uniform(0, 1)  # the function value
        fluc = random.uniform(0, 1)

        dev = 1
        if fluc > self.effectivness:
            dev = -1
        c = c * dev

        return c

    def changeByTime(self):
        if not self.bankruptcy:
            lastIndex = len(self.values) - 1
            last = self.values[lastIndex]
            newValue = last + (last + 1) * self.deviationPart()
            if newValue <= 0:
                newValue=0
                self.bankruptcy=True
            self.values.append(newValue)
        else:
            self.values.append(0)

        self.lifeLenght += 1



# INFORMATION ABOUT OBJECT
#----------------------------------------------------------------------

    def getPerformance(self, days):
        perfText=""
        lastIndex=len(self.values) - 1
        if len(self.values) > days + 1:
            diff=self.compareValues(self.values, lastIndex, lastIndex - days)
            perfText += str(diff) + " %"
        else:
            perfText="No data"
        return perfText

    def getTotalPerformance(self):
        perfText=""
        lastIndex=len(self.values) - 1
        diff=self.compareValues(self.values, lastIndex, 0)
        perfText += str(diff) + " %"

        return perfText

    def compareValues(self, l, first, last):
        if l[last] == 0:
            return 0
        else:
            return round(l[first] / float(l[last]) - 1, 4) * 100
