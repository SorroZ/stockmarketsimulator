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

    def getPerformance(self, days):
        perfText = ""
        if len(self.values) > days + 1:
            day = self.compareInList(self.values, lastIndex, lastIndex - days)
            perfText += "Day:\t" + str(day) + " %\n"
        else:
            perfText = "No data"

        return perfText


    def getPerformance(self):
        perfText = "Company name: "+self.name +"\tStock code: "+self.tag+"\n"
        lastIndex = len(self.values) - 1
        if len(self.values) > 1:
            day = self.compareInList(self.values, lastIndex, lastIndex - 1)
            perfText += "Day:\t" + str(day) + " %\n"
        if len(self.values) > 8:
            week = self.compareInList(self.values, lastIndex, lastIndex - 7)
            perfText += "Week:\t" + str(week) + " %\n"
        if len(self.values) > 31:
            month = self.compareInList(self.values, lastIndex, lastIndex - 30)
            perfText += "Month:\t" + str(month) + " %\n"
        if len(self.values) > 366:
            year = self.compareInList(self.values, lastIndex, lastIndex - 365)
            perfText += "Year:\t" + str(year) + " %\n"
        if len(self.values) > 1:
            total = self.compareInList(self.values, lastIndex, 0)
            perfText += "Total:\t" + str(total) + " %\n"

        return perfText

    def compareInList(self, l, first, last):
        return round( l[first]/float(l[last])  - 1, 4 ) * 100
