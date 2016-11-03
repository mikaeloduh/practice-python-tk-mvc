
#from cycletimegui import CycleTimeGUI
import os

class Gear:
    def __init__(self):
        self.data = {
                        "workID": "untitled-project",
                        "parts": {
                            "productID": "no-name",
                            "module": 0,
                            "normPressAng_d": 0,
                            "normPressAng_m": 0,
                            "normPressAng_s": 0,
                            "starts": 0,
                            "pitchDia": 0,
                            "outDia": 0,
                            "rootDia": 0,
                            "leadAng_d": 0,
                            "leadAng_m": 0,
                            "leadAng_s": 0,
                            "toothThick": 0,
                            "threadLen": 0
                        },
                        "machining": [
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
        #self.module = self.data["parts"]["module"]
        self.starts = self.data["parts"]["starts"]
        self.threadLen = self.data["parts"]["threadLen"]

        self.passes_1 = self.data["machining"][0]["passes"]
        self.feedForw_1 = self.data["machining"][0]["feedForw"]
        self.dressPass_1 = self.data["machining"][0]["dressPass"]
        self.dressFeed_1 = self.data["machining"][0]["dressFeed"]
        self.byPass_1 = self.data["machining"][0]["dressFrq"]

        self.passes_2 = self.data["machining"][1]["passes"]
        self.feedForw_2 = self.data["machining"][1]["feedForw"]
        self.dressPass_2 = self.data["machining"][1]["dressPass"]
        self.dressFeed_2 = self.data["machining"][1]["dressFeed"]
        self.byPass_2 = self.data["machining"][1]["dressFrq"]

        self.passes_3 = self.data["machining"][2]["passes"]
        self.feedForw_3 = self.data["machining"][2]["feedForw"]
        self.dressPass_3 = self.data["machining"][2]["dressPass"]
        self.dressFeed_3 = self.data["machining"][2]["dressFeed"]
        self.byPass_3 = self.data["machining"][2]["dressFrq"]

        self.passes_4 = self.data["machining"][3]["passes"]
        self.feedForw_4 = self.data["machining"][3]["feedForw"]
        self.dressPass_4 = self.data["machining"][3]["dressPass"]
        self.dressFeed_4 = self.data["machining"][3]["dressFeed"]
        self.byPass_4 = self.data["machining"][3]["dressFrq"]
        # notify
        self.notify()

    def getData(self):
        return self.data

    def toCalculate(self):
        self.grindTime_1 = 0
        self.dressTime_1 = 0
        self.grindTime_2 = 0
        self.dressTime_2 = 0
        self.grindTime_3 = 0
        self.dressTime_3 = 0
        self.grindTime_4 = 0
        self.dressTime_4 = 0
        self.cycleTime = 0

        if self.passes_1:
            self.grindTime_1 = 6.0 + self.starts * self.passes_1 * self.threadLen / self.feedForw_1 * (41*200/1.68)
        if self.byPass_1:
            self.dressTime_1  = ( 12 + 19*6 * self.dressPass_1 / self.dressFeed_1 + 12 ) * (self.starts * self.passes_1 // self.byPass_1)

        if self.passes_2:
            self.grindTime_2 = 6.0 + self.starts * self.passes_2 * self.threadLen / self.feedForw_2 * (41*200/1.68)
        if self.byPass_2:
            self.dressTime_2  = ( 12 + 19*6 * self.dressPass_2 / self.dressFeed_2 + 12 ) * (self.starts * self.passes_2 // self.byPass_2)

        if self.passes_3:
            self.grindTime_3 = 6.0 + self.starts * self.passes_3 * self.threadLen / self.feedForw_3 * (41*200/1.68)
        if self.byPass_4:
            self.dressTime_3  = ( 12 + 19*6 * self.dressPass_3 / self.dressFeed_3 + 12 ) * (self.starts * self.passes_3 // self.byPass_3)

        if self.passes_4:
            self.grindTime_4 = 6.0 + self.starts * self.passes_4 * self.threadLen / self.feedForw_4 * (41*200/1.68)
        if self.byPass_4:
            self.dressTime_4  = ( 12 + 19*6 * self.dressPass_4 / self.dressFeed_4 + 12 ) * (self.starts * self.passes_4 // self.byPass_4)

        self.cycleTime = self.dressTime_1 + self.grindTime_1 + self.dressTime_2 + self.grindTime_2 + self.dressTime_3 + self.grindTime_3 + self.dressTime_4 + self.grindTime_4
