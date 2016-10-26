
#from cycletimegui import CycleTimeGUI
import os

class Gear:
    def __init__(self):
        self.data = {
                        "workID": "",
                        "parts": {
                            "productID": "",
                            "module": 0,
                            "normPressAng": 0,
                            "starts": 0,
                            "pitchDia": 0,
                            "outDia": 0,
                            "rootDia": 0,
                            "leadAng": 0,
                            "toothThick": 0,
                            "threadLen": 0
                        },
                        "machining": [
                            {
                                "passes": 1,
                                "feedForw": 0,
                                "feedBack": 0,
                                "infeedForw": 0,
                                "infeedBack": 0,
                                "infeedTotal": 0,
                                "plunge": 0,
                                "speed": 0,
                                "dressPass": 0,
                                "dressInfeed": 0,
                                "dressFeed": 0,
                                "dressFrq": 0
                            },
                            {
                                "passes": 0,
                                "feedForw": 0,
                                "feedBack": 0,
                                "infeedForw": 0,
                                "infeedBack": 0,
                                "infeedTotal": 0,
                                "plunge": 0,
                                "speed": 0,
                                "dressPass": 0,
                                "dressInfeed": 0,
                                "dressFeed": 0,
                                "dressFrq": 0
                            },
                            {
                                "passes": 0,
                                "feedForw": 0,
                                "feedBack": 0,
                                "infeedForw": 0,
                                "infeedBack": 0,
                                "infeedTotal": 0,
                                "plunge": 0,
                                "speed": 0,
                                "dressPass": 0,
                                "dressInfeed": 0,
                                "dressFeed": 0,
                                "dressFrq": 0
                            },
                            {
                                "passes": 0,
                                "feedForw": 0,
                                "feedBack": 0,
                                "infeedForw": 0,
                                "infeedBack": 0,
                                "infeedTotal": 0,
                                "plunge": 0,
                                "speed": 0,
                                "dressPass": 0,
                                "dressInfeed": 0,
                                "dressFeed": 0,
                                "dressFrq": 0
                            }
                        ]
                    }

        self.observers = []
        self.grindTime_1 = 0
        self.dressTime_1 = 0
        self.grindTime_2 = 0
        self.dressTime_2 = 0
        self.grindTime_3 = 0
        self.dressTime_3 = 0
        self.grindTime_4 = 0
        self.dressTime_4 = 0
        self.cycleTime = 0

        #self.notify()

    def addObserver(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer(self.data)

    def setData(self, data):
        self.data = data
        self.module = self.data["parts"]["module"]
        self.starts = self.data["parts"]["starts"]
        self.threadLen = self.data["parts"]["threadLen"]
        self.passes = self.data["machining"][0]["passes"]
        self.feedForw = self.data["machining"][0]["feedForw"]
        self.dressPass = self.data["machining"][0]["dressPass"]
        self.dressFeed = self.data["machining"][0]["dressFeed"]
        self.byPass = self.data["machining"][0]["dressFrq"]
        # notify
        self.notify()

    def getData(self):

        return self.data

    def toCalculate(self):
        self.grindTime_1 = 6.0 + self.starts * self.passes * self.threadLen / self.feedForw * (41*200/1.68)
        self.dressTime_1  = ( 12 + 19*6 * self.dressPass / self.dressFeed + 12 ) * (self.starts * self.passes // self.byPass)

        self.grindTime_2 = 6.0 + self.starts * self.passes * self.threadLen / self.feedForw * (41*200/1.68)
        self.dressTime_2  = ( 12 + 19*6 * self.dressPass / self.dressFeed + 12 ) * (self.starts * self.passes // self.byPass)

        self.grindTime_3 = 6.0 + self.starts * self.passes * self.threadLen / self.feedForw * (41*200/1.68)
        self.dressTime_3  = ( 12 + 19*6 * self.dressPass / self.dressFeed + 12 ) * (self.starts * self.passes // self.byPass)

        self.grindTime_4 = 6.0 + self.starts * self.passes * self.threadLen / self.feedForw * (41*200/1.68)
        self.dressTime_4  = ( 12 + 19*6 * self.dressPass / self.dressFeed + 12 ) * (self.starts * self.passes // self.byPass)

        self.cycleTime = self.dressTime_1 + self.grindTime_1 + self.dressTime_2 + self.grindTime_2 + self.dressTime_3 + self.grindTime_3 + self.dressTime_4 + self.grindTime_4
