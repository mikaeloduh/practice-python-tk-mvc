
#from cycletimegui import CycleTimeGUI
import os

class Gear:
    def __init__(self):
        self.__workspace = {}
        self.__workspace['workID'] = 'untitled-project'

        parts = {}
        parts['productID'] = 'no-name'
        parts['module'] = 0
        parts['normPressAng_d'] = 0
        parts['normPressAng_m'] = 0
        parts['normPressAng_s'] = 0
        parts['starts'] = 0
        parts['pitchDia'] = 0
        parts['outDia'] = 0
        parts['rootDia'] = 0
        parts['leadAng_d'] = 0
        parts['leadAng_m'] = 0
        parts['leadAng_s'] = 0
        parts['toothThick'] = 0
        parts['threadLen'] = 0
        self.__workspace['parts'] = parts

        machining = [{}]
        machining[0]['passes'] = 0
        machining[0]['feedForw'] = 0
        machining[0]['feedBack'] = 0
        machining[0]['infeedForw'] = 0
        machining[0]['infeedBack'] = 0
        machining[0]['infeedTotal'] = 0
        machining[0]['plunge'] = 0
        machining[0]['speed'] = 0
        machining[0]['dressPass'] = 0
        machining[0]['dressInfeed'] = 0
        machining[0]['dressFeed'] = 0
        machining[0]['dressFrq'] = 0        
        self.__workspace['machining'] = machining * 4

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
            observer(self.__workspace)

    def setData(self, data):
        self.__workspace = data
        
        # notify
        self.notify()

    def getData(self):
        return self.__workspace

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

        starts = self.__workspace["parts"]["starts"]
        threadLen = self.__workspace["parts"]["threadLen"]

        passes_1 = self.__workspace["machining"][0]["passes"]
        feedForw_1 = self.__workspace["machining"][0]["feedForw"]
        dressPass_1 = self.__workspace["machining"][0]["dressPass"]
        dressFeed_1 = self.__workspace["machining"][0]["dressFeed"]
        byPass_1 = self.__workspace["machining"][0]["dressFrq"]

        passes_2 = self.__workspace["machining"][1]["passes"]
        feedForw_2 = self.__workspace["machining"][1]["feedForw"]
        dressPass_2 = self.__workspace["machining"][1]["dressPass"]
        dressFeed_2 = self.__workspace["machining"][1]["dressFeed"]
        byPass_2 = self.__workspace["machining"][1]["dressFrq"]

        passes_3 = self.__workspace["machining"][2]["passes"]
        feedForw_3 = self.__workspace["machining"][2]["feedForw"]
        dressPass_3 = self.__workspace["machining"][2]["dressPass"]
        dressFeed_3 = self.__workspace["machining"][2]["dressFeed"]
        byPass_3 = self.__workspace["machining"][2]["dressFrq"]

        passes_4 = self.__workspace["machining"][3]["passes"]
        feedForw_4 = self.__workspace["machining"][3]["feedForw"]
        dressPass_4 = self.__workspace["machining"][3]["dressPass"]
        dressFeed_4 = self.__workspace["machining"][3]["dressFeed"]
        byPass_4 = self.__workspace["machining"][3]["dressFrq"]

        if passes_1:
            self.grindTime_1 = 6.0 + starts * passes_1 * threadLen / feedForw_1 * (41*200/1.68)
        if byPass_1:
            self.dressTime_1  = ( 12 + 19*6 * dressPass_1 / dressFeed_1 + 12 ) * (starts * passes_1 // byPass_1)

        if passes_2:
            self.grindTime_2 = 6.0 + starts * passes_2 * threadLen / feedForw_2 * (41*200/1.68)
        if byPass_2:
            self.dressTime_2  = ( 12 + 19*6 * dressPass_2 / dressFeed_2 + 12 ) * (starts * passes_2 // byPass_2)

        if passes_3:
            self.grindTime_3 = 6.0 + starts * passes_3 * threadLen / feedForw_3 * (41*200/1.68)
        if byPass_4:
            self.dressTime_3  = ( 12 + 19*6 * dressPass_3 / dressFeed_3 + 12 ) * (starts * passes_3 // byPass_3)

        if passes_4:
            self.grindTime_4 = 6.0 + starts * passes_4 * threadLen / feedForw_4 * (41*200/1.68)
        if byPass_4:
            self.dressTime_4  = ( 12 + 19*6 * dressPass_4 / dressFeed_4 + 12 ) * (starts * passes_4 // byPass_4)

        self.cycleTime = self.dressTime_1 + self.grindTime_1 + self.dressTime_2 + self.grindTime_2 + self.dressTime_3 + self.grindTime_3 + self.dressTime_4 + self.grindTime_4
