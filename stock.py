#!/usr/bin/python

import random
import math

class Stock:

    bankruptcy = False

    def __init__(self, name = "Unknown", tag = "-", startValue = 100, risk = 5):
        self.name = name
        self.tag = tag
        self.values = [ startValue ]
        self.effectivness = 0.5 # 0 = only negetive, 1 = only positive
        self.risk = risk

    def getLastValue(self):
        last = len(self.values) - 1
        return self.values[last]

    def getAllValues(self):
        return self.values

    def deviationPart(self):
        x = random.uniform(0,7) # the x value
        c = (self.risk/float(10))*random.uniform(0,0.5)*math.exp(-x)*random.uniform(0,1) # the function value
        fluc = random.uniform(0,1)

        dev = 1;
        if fluc > self.effectivness:
            dev = -1
        c = c * dev

        return c

    def changeByTime(self):
        if not self.bankruptcy:
            lastIndex = len(self.values) - 1
            last = self.values[lastIndex]
            newValue = last + last * self.deviationPart()
            if newValue <= 0:
                newValue = 0
                self.bankruptcy = True
            self.values.append(newValue)
        else:
            self.values.append(0)
