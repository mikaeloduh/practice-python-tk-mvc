
#from cycletimegui import CycleTimeGUI
import os

class Gear:
    def __init__(self):
        self.data = {"module":0, "start":0, "tLength":0, "passes_1":0, "ffeed_1":0, "dressPass_1":0, "dressFeed_1":0, "byPass_1":0}
        self.observers = []
        self.setDressingTime1 = 0
        self.setCycleTime1 = 0
        self.result1 = 0
        # test
        #self.module = 0
        self.plug = 6.0
        #self.start = 1
        #self.tLength = 4.91
        self.dressPlug = 12

    def addObserver(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer(self.data)


    def setData(self, data):
        self.data = data
        self.module = self.data["module"]
        self.start = self.data["start"]
        self.tLength = self.data["tLength"]
        self.passes = self.data["passes_1"]
        self.ffeed = self.data["ffeed_1"]
        self.dressPass = self.data["dressPass_1"]
        self.dressFeed = self.data["dressFeed_1"]
        self.byPass = self.data["byPass_1"]
        # notify
        self.notify()

    def getData(self):
        return self.data


    def toCalculate(self):
        self.setCycleTime1 = self.plug + self.start * self.passes * self.tLength / self.ffeed * (41*200/1.68)
        self.setDressingTime1  = ( self.dressPlug + 19*6 * self.dressPass / self.dressFeed + self.dressPlug ) * (self.start * self.passes // self.byPass)

        print(self.setCycleTime1)
        print(self.setDressingTime1)

        self.result1 = self.setDressingTime1 + self.setCycleTime1
        #self.setDressingTime1
        #self.setCycleTime1

        #print(self.result1)
        print(type(self.result1))
