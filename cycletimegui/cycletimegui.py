from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from gear import Gear
import os
import json


class MainView(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=None)
        self.pack()

        self.workIdEntry = Label(self, justify = "center")
        self.workIdEntry.pack()

        self.nb = Notebook(self)
        self.nb.pack()
        self.nb1 = ImportGUI(self.nb)
        self.nb2 = CycleTimeGUI(self.nb)
        self.nb.add(self.nb1, text="Gear Data")
        self.nb.pack()
        self.nb.add(self.nb2, text="Machining Cycle")
        self.nb.pack()

    def getData(self):
        pass

    def setData(self, data):
        self.workIdEntry.config(text = str(data["workID"]))

class ImportGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        # row 0
        self.partNoLabel = Label(self, text = "Part No.")
        self.partNoLabel.grid(row=0, column=0, sticky=W)
        self.partNoEntry = Entry(self)
        self.partNoEntry.grid(row=0, column=1, columnspan=3)
        # row 1
        self.DPLabel = Label(self, text = "DP")
        self.DPLabel.grid(row=1, column=0, sticky=W)
        self.DPEntry = Entry(self)
        self.DPEntry.grid(row=1, column=1, columnspan=3)
        # row 2
        self.normalPALabel = Label(self, text = "Normal Pressure Angle")
        self.normalPALabel.grid(row=2, column=0, sticky=W)
        self.normalPAEntry1 = Entry(self, width = 6)
        self.normalPAEntry1.grid(row=2, column=1, columnspan=1)
        self.normalPAEntry2 = Entry(self, width = 6)
        self.normalPAEntry2.grid(row=2, column=2, columnspan=1)
        self.normalPAEntry3 = Entry(self, width = 6)
        self.normalPAEntry3.grid(row=2, column=3, columnspan=1)
        # row 3
        self.stratsLabel = Label(self, text = "Starts")
        self.stratsLabel.grid(row=3, column=0, sticky=W)
        self.startEntry = Entry(self)
        self.startEntry.grid(row=3, column=1, columnspan=3)
        # row 4
        self.pitchDiaLable = Label(self, text = "Pitch Diameter")
        self.pitchDiaLable.grid(row=4, column=0, sticky=W)
        self.pitchDiaEntry = Entry(self)
        self.pitchDiaEntry.grid(row=4, column=1, columnspan=3)
        # row 5
        self.outsideDiaLabel = Label(self, text = "Outside Diameter")
        self.outsideDiaLabel.grid(row=5, column=0, sticky=W)
        self.outsideDiaEntry = Entry(self)
        self.outsideDiaEntry.grid(row=5, column=1, columnspan=3)
        # row 6
        self.rooteDiaLable = Label(self, text = "Root Diameter")
        self.rooteDiaLable.grid(row=6, column=0, sticky=W)
        self.rooteDiaEntry = Entry(self)
        self.rooteDiaEntry.grid(row=6, column=1, columnspan=3)
        # row 7
        self.leadAngleLabel = Label(self, text = "Lead Angle")
        self.leadAngleLabel.grid(row=7, column=0, sticky=W)
        self.leadAngleEntry1 = Entry(self, width = 6)
        self.leadAngleEntry1.grid(row=7, column=1, columnspan=1)
        self.leadAngleEntry2 = Entry(self, width = 6)
        self.leadAngleEntry2.grid(row=7, column=2, columnspan=1)
        self.leadAngleEntry3 = Entry(self, width = 6)
        self.leadAngleEntry3.grid(row=7, column=3, columnspan=1)
        # row 8
        self.toothThicknLabel = Label(self, text = "Tooth Thickness (Axial)")
        self.toothThicknLabel.grid(row=8, column=0, sticky=W)
        self.toothThicknEntry = Entry(self)
        self.toothThicknEntry.grid(row=8, column=1, columnspan=3)
        # row 9
        self.threadLengthLabel = Label(self, text = "Thread Length")
        self.threadLengthLabel.grid(row=9, column=0, sticky=W)
        self.threadLengthEntry = Entry(self)
        self.threadLengthEntry.grid(row=9, column=1, columnspan=3)

    def getData(self):
        # Try to make it a float
        self.data["parts"]["productID"] = self.partNoEntry.get()
        self.data["parts"]["module"] = float(self.DPEntry.get())
        self.data["parts"]["normPressAng_d"] = int(self.normalPAEntry1.get())
        self.data["parts"]["normPressAng_m"] = int(self.normalPAEntry2.get())
        self.data["parts"]["normPressAng_s"] = int(self.normalPAEntry3.get())
        self.data["parts"]["starts"] = int(self.startEntry.get())
        self.data["parts"]["pitchDia"] = float(self.pitchDiaEntry.get())
        self.data["parts"]["outDia"] = float(self.outsideDiaEntry.get())
        self.data["parts"]["rootDia"] = float(self.rooteDiaEntry.get())
        self.data["parts"]["leadAng_d"] = int(self.leadAngleEntry1.get())
        self.data["parts"]["leadAng_m"] = int(self.leadAngleEntry2.get())
        self.data["parts"]["leadAng_s"] = int(self.leadAngleEntry3.get())
        self.data["parts"]["toothThick"] = float(self.toothThicknEntry.get())
        self.data["parts"]["threadLen"] = float(self.threadLengthEntry.get())

        return self.data

    def setData(self, data):
        self.data = data

        self.partNoEntry.delete(0, 'end')
        self.partNoEntry.insert('end', str(self.data["parts"]["productID"]))
        self.DPEntry.delete(0, 'end')
        self.DPEntry.insert('end', str(self.data["parts"]["module"]))
        self.normalPAEntry1.delete(0, 'end')
        self.normalPAEntry1.insert('end', str(self.data["parts"]["normPressAng_d"]))
        self.normalPAEntry2.delete(0, 'end')
        self.normalPAEntry2.insert('end', str(self.data["parts"]["normPressAng_m"]))
        self.normalPAEntry3.delete(0, 'end')
        self.normalPAEntry3.insert('end', str(self.data["parts"]["normPressAng_s"]))
        self.startEntry.delete(0, 'end')
        self.startEntry.insert('end', str(self.data["parts"]["starts"]))
        self.pitchDiaEntry.delete(0, 'end')
        self.pitchDiaEntry.insert('end', str(self.data["parts"]["pitchDia"]))
        self.outsideDiaEntry.delete(0, 'end')
        self.outsideDiaEntry.insert('end', str(self.data["parts"]["outDia"]))
        self.rooteDiaEntry.delete(0, 'end')
        self.rooteDiaEntry.insert('end', str(self.data["parts"]["rootDia"]))
        self.leadAngleEntry1.delete(0, 'end')
        self.leadAngleEntry1.insert('end', str(self.data["parts"]["leadAng_d"]))
        self.leadAngleEntry2.delete(0, 'end')
        self.leadAngleEntry2.insert('end', str(self.data["parts"]["leadAng_m"]))
        self.leadAngleEntry3.delete(0, 'end')
        self.leadAngleEntry3.insert('end', str(self.data["parts"]["leadAng_s"]))
        self.toothThicknEntry.delete(0, 'end')
        self.toothThicknEntry.insert('end', str(self.data["parts"]["toothThick"]))
        self.threadLengthEntry.delete(0, 'end')
        self.threadLengthEntry.insert('end', str(self.data["parts"]["threadLen"]))


class CycleTimeGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.tabs = Notebook(self)
        self.createWidgets()
        self.data = {}#[float(0)] * 11

    def createWidgets(self):
        self.panedWindow = Panedwindow(self, orient=VERTICAL)
        self.panedWindow.grid()

        ########## Labelframe: Grinding ############
        self.grindFrame = Labelframe(self.panedWindow, text = "Grinding")
        self.grindFrame.grid(row=0, column=0)
        # Label 1
        self.label_I = Label(self.grindFrame, text = "I")
        self.label_I.grid(row=0, column=1)
        # Label 2
        self.label_II = Label(self.grindFrame, text = "II")
        self.label_II.grid(row=0, column=2)
        # Label 3
        self.label_III = Label(self.grindFrame, text = "III")
        self.label_III.grid(row=0, column=3)
        # Label 4
        self.label_IV = Label(self.grindFrame, text = "IV")
        self.label_IV.grid(row=0, column=4)

        # row 1: passes
        # label 0
        self.grindingPassLabel = Label(self.grindFrame, text = "                  Passes")
        self.grindingPassLabel.grid(row=1, column=0, sticky=E)
        # Entry 1
        #self.p1 = IntVar()
        self.grindingPassInput_1 = Entry(self.grindFrame, width=5)#, textvariable = self.p1)
        self.grindingPassInput_1.grid(row=1, column=1)
        # Entry 2
        self.grindingPassInput_2 = Entry(self.grindFrame, width=5)
        self.grindingPassInput_2.grid(row=1, column=2)
        # Entry 3
        self.grindingPassInput_3 = Entry(self.grindFrame, width=5)
        self.grindingPassInput_3.grid(row=1, column=3)
        # Entry 4
        self.grindingPassInput_4 = Entry(self.grindFrame, width=5)
        self.grindingPassInput_4.grid(row=1, column=4)

        # row 2: Feed-Forward
        # label 0
        self.feedForwardLabel = Label(self.grindFrame, text = "Feed-Forward")
        self.feedForwardLabel.grid(row=2, column=0, sticky=E)
        # Entry 1
        self.feedForwardInput_1 = Entry(self.grindFrame, width=5)
        self.feedForwardInput_1.grid(row=2, column=1)
        # Entry 2
        self.feedForwardInput_2 = Entry(self.grindFrame, width=5)
        self.feedForwardInput_2.grid(row=2, column=2)
        # Entry 3
        self.feedForwardInput_3 = Entry(self.grindFrame, width=5)
        self.feedForwardInput_3.grid(row=2, column=3)
        # Entry 4
        self.feedForwardInput_4 = Entry(self.grindFrame, width=5)
        self.feedForwardInput_4.grid(row=2, column=4)

        # row 3: Feed-Backward
        # label 0
        self.feedBackwardLabel = Label(self.grindFrame, text = "Feed-Backward")
        self.feedBackwardLabel.grid(row=3, column=0, sticky=E)
        # Entry 1
        self.feedBackwardInput_1 = Entry(self.grindFrame, width=5)
        self.feedBackwardInput_1.grid(row=3, column=1)
        # Entry 2
        self.feedBackwardInput_2 = Entry(self.grindFrame, width=5)
        self.feedBackwardInput_2.grid(row=3, column=2)
        # Entry 3
        self.feedBackwardInput_3 = Entry(self.grindFrame, width=5)
        self.feedBackwardInput_3.grid(row=3, column=3)
        # Entry 4
        self.feedBackwardInput_4 = Entry(self.grindFrame, width=5)
        self.feedBackwardInput_4.grid(row=3, column=4)

        # row 4: Infeed-Forward
        # label 0
        self.infeedForwardLabel = Label(self.grindFrame, text = "Infeed-Forward")
        self.infeedForwardLabel.grid(row=4, column=0, sticky=E)
        # Entry 1
        self.infeedForwardInput_1 = Entry(self.grindFrame, width=5)
        self.infeedForwardInput_1.grid(row=4, column=1)
        # Entry 2
        self.infeedForwardInput_2 = Entry(self.grindFrame, width=5)
        self.infeedForwardInput_2.grid(row=4, column=2)
        # Entry 3
        self.infeedForwardInput_3 = Entry(self.grindFrame, width=5)
        self.infeedForwardInput_3.grid(row=4, column=3)
        # Entry 4
        self.infeedForwardInput_4 = Entry(self.grindFrame, width=5)
        self.infeedForwardInput_4.grid(row=4, column=4)

        # row 5 : Infeed-Backward
        # Label 0
        self.infeedBackwardLabel = Label(self.grindFrame, text = "Infeed-Backward")
        self.infeedBackwardLabel.grid(row=5, column=0, sticky=E)
        # Entry 1
        self.infeedBackwardInput_1 = Entry(self.grindFrame, width=5)
        self.infeedBackwardInput_1.grid(row=5, column=1)
        # Entry 2
        self.infeedBackwardInput_2 = Entry(self.grindFrame, width=5)
        self.infeedBackwardInput_2.grid(row=5, column=2)
        # Entry 3
        self.infeedBackwardInput_3 = Entry(self.grindFrame, width=5)
        self.infeedBackwardInput_3.grid(row=5, column=3)
        # Entry 4
        self.infeedBackwardInput_4 = Entry(self.grindFrame, width=5)
        self.infeedBackwardInput_4.grid(row=5, column=4)

        # row 6 : Infeed-Total
        # Label 0
        self.totalInfeedLabel = Label(self.grindFrame, text = "Infeed-Total")
        self.totalInfeedLabel.grid(row=6, column=0, sticky=E)
        # Entry 1
        self.totalInfeedOutput_1 = Entry(self.grindFrame, width=5)
        self.totalInfeedOutput_1.grid(row=6, column=1)
        # Entry 2
        self.totalInfeedOutput_2 = Entry(self.grindFrame, width=5)
        self.totalInfeedOutput_2.grid(row=6, column=2)
        # Entry 3
        self.totalInfeedOutput_3 = Entry(self.grindFrame, width=5)
        self.totalInfeedOutput_3.grid(row=6, column=3)
        # Entry 4
        self.totalInfeedOutput_4 = Entry(self.grindFrame, width=5)
        self.totalInfeedOutput_4.grid(row=6, column=4)

        # row 7: Plung Feed
        # Label 0
        self.plungFeedLabel = Label(self.grindFrame, text = "Plung Feed")
        self.plungFeedLabel.grid(row=7, column=0, sticky=E)
        # Entry 1
        self.plungFeedInput_1 = Entry(self.grindFrame, width=5)
        self.plungFeedInput_1.grid(row=7, column=1)
        # Entry 2
        self.plungFeedInput_2 = Entry(self.grindFrame, width=5)
        self.plungFeedInput_2.grid(row=7, column=2)
        # Entry 3
        self.plungFeedInput_3 = Entry(self.grindFrame, width=5)
        self.plungFeedInput_3.grid(row=7, column=3)
        # Entry 4
        self.plungFeedInput_4 = Entry(self.grindFrame, width=5)
        self.plungFeedInput_4.grid(row=7, column=4)

        ############# Labelframe 1: Dressing  ##############
        self.dressFrame = Labelframe(self.panedWindow, text = "Dressing", width=10000, height=10000)
        self.dressFrame.grid(row=1, column=0)

        # row 0: Dressing Passes
        # Label 0
        self.dresssingPassLabel = Label(self.dressFrame, text = "                  Passes")
        self.dresssingPassLabel.grid(row=0, column=0, sticky=E)
        # Entry 1
        self.dresssingPassInput_1 = Entry(self.dressFrame, width=5)
        self.dresssingPassInput_1.grid(row=0, column=1)
        # Entry 2
        self.dresssingPassInput_2 = Entry(self.dressFrame, width=5)
        self.dresssingPassInput_2.grid(row=0, column=2)
        # Entry 3
        self.dresssingPassInput_3 = Entry(self.dressFrame, width=5)
        self.dresssingPassInput_3.grid(row=0, column=3)
        # Entry 4
        self.dresssingPassInput_4 = Entry(self.dressFrame, width=5)
        self.dresssingPassInput_4.grid(row=0, column=4)

        # row 1: Dressing Infeed
        # Label 0
        self.dressingInfeedLabel = Label(self.dressFrame, text = "InFeed")
        self.dressingInfeedLabel.grid(row=1, column=0, sticky=E)
        # Entry 1
        self.dresssingInfeedInput_1 = Entry(self.dressFrame, width=5)
        self.dresssingInfeedInput_1.grid(row=1, column=1)
        # Entry 2
        self.dresssingInfeedInput_2 = Entry(self.dressFrame, width=5)
        self.dresssingInfeedInput_2.grid(row=1, column=2)
        # Entry 3
        self.dresssingInfeedInput_3 = Entry(self.dressFrame, width=5)
        self.dresssingInfeedInput_3.grid(row=1, column=3)
        # Entry 4
        self.dresssingInfeedInput_4 = Entry(self.dressFrame, width=5)
        self.dresssingInfeedInput_4.grid(row=1, column=4)

        # row 2: Dressing Feed
        # label 0
        self.dressingFeedLabel = Label(self.dressFrame, text = "Feed")
        self.dressingFeedLabel.grid(row=2, column=0, sticky=E)
        # Entry 1
        self.dressingFeedInput_1 = Entry(self.dressFrame, width=5)
        self.dressingFeedInput_1.grid(row=2, column=1)
        # Entry 2
        self.dressingFeedInput_2 = Entry(self.dressFrame, width=5)
        self.dressingFeedInput_2.grid(row=2, column=2)
        # Entry 3
        self.dressingFeedInput_3 = Entry(self.dressFrame, width=5)
        self.dressingFeedInput_3.grid(row=2, column=3)
        # Entry 4
        self.dressingFeedInput_4 = Entry(self.dressFrame, width=5)
        self.dressingFeedInput_4.grid(row=2, column=4)

        # raw 3: Dressing frq.
        # label 0
        self.dressingFrqLabel = Label(self.dressFrame, text = "Dressing Frq.")
        self.dressingFrqLabel.grid(row=3, column=0, sticky=E)

        # row 4: [drop down]
        # Label 0
        self.dressingFrqLabel = Label(self.dressFrame, text = "[By Passes]")
        self.dressingFrqLabel.grid(row=4, column=0, sticky=E)
        # Entry 1
        self.dressingFrqInput_1 = Entry(self.dressFrame, width=5)
        self.dressingFrqInput_1.grid(row=4, column=1)
        # Entry 2
        self.dressingFrqInput_2 = Entry(self.dressFrame, width=5)
        self.dressingFrqInput_2.grid(row=4, column=2)
        # Entry 3
        self.dressingFrqInput_3 = Entry(self.dressFrame, width=5)
        self.dressingFrqInput_3.grid(row=4, column=3)
        # Entry 4
        self.dressingFrqInput_4 = Entry(self.dressFrame, width=5)
        self.dressingFrqInput_4.grid(row=4, column=4)

        ############# Labelframe 2: Cycle Time  ##############
        self.resultFrame = Labelframe(self.panedWindow, text = " Cycle Time")
        self.resultFrame.grid(row=2, column=0)
        # row 0
        # label 0
        self.dressingSetLabel_1 = Label(self.resultFrame, text = "I")
        self.dressingSetLabel_1.grid(row=0, column=1)
        # label 0
        self.dressingSetLabel_2 = Label(self.resultFrame, text = "II")
        self.dressingSetLabel_2.grid(row=0, column=2)
        # label 0
        self.dressingSetLabel_3 = Label(self.resultFrame, text = "III")
        self.dressingSetLabel_3.grid(row=0, column=3)
        # label 0
        self.dressingSetLabel_4 = Label(self.resultFrame, text = "IV")
        self.dressingSetLabel_4.grid(row=0, column=4)

        # row 1: set dressing time
        # label 0
        self.dressingTimeLabel = Label(self.resultFrame, text = "Set Dressing Time")
        self.dressingTimeLabel.grid(row=1, column=0, sticky=E)
        # Entry 1
        self.dressingTimeOutput_1 = Entry(self.resultFrame, width=5)
        self.dressingTimeOutput_1.grid(row=1, column=1)
        # Entry 2
        self.dressingTimeOutput_2 = Entry(self.resultFrame, width=5)
        self.dressingTimeOutput_2.grid(row=1, column=2)
        # Entry 3
        self.dressingTimeOutput_3 = Entry(self.resultFrame, width=5)
        self.dressingTimeOutput_3.grid(row=1, column=3)
        # Entry 4
        self.dressingTimeOutput_4 = Entry(self.resultFrame, width=5)
        self.dressingTimeOutput_4.grid(row=1, column=4)

        # row 2: Set Cycle time (sec.)
        # label 0
        self.setCycleTimeLabel = Label(self.resultFrame, text = "Set Cycle Time")
        self.setCycleTimeLabel.grid(row=2, column=0, sticky=E)
        # Entry 1
        self.setCycleTimeOutput_1 = Entry(self.resultFrame, width=5)
        self.setCycleTimeOutput_1.grid(row=2, column=1)
        # Entry 2
        self.setCycleTimeOutput_2 = Entry(self.resultFrame, width=5)
        self.setCycleTimeOutput_2.grid(row=2, column=2)
        # Entry 3
        self.setCycleTimeOutput_3 = Entry(self.resultFrame, width=5)
        self.setCycleTimeOutput_3.grid(row=2, column=3)
        # Entry 4
        self.setCycleTimeOutput_4 = Entry(self.resultFrame, width=5)
        self.setCycleTimeOutput_4.grid(row=2, column=4)

        # raw 3: Total Cycle time (sec.)
        # label 0
        self.totalCycleTimeLabel = Label(self.resultFrame, text = "Total Cycle time")
        self.totalCycleTimeLabel.grid(row=3, column=0, sticky=E)
        # Entry 1
        self.totalCycleTimeOutput = Entry(self.resultFrame, width = "11")
        self.totalCycleTimeOutput.grid(row=3, column=1, columnspan=2)
        ################# Button 2 : Calcuate ###################
        self.calcuateBtn = Button(self.resultFrame, width=8, text = "Calcuate")
        self.calcuateBtn.grid(row=3, column=3, columnspan=2)

        # Place 3 Paned window
        self.panedWindow.add(self.grindFrame)
        self.panedWindow.add(self.dressFrame)
        self.panedWindow.add(self.resultFrame)


    def getData(self):
        self.data["machining"][0]["passes"] = int(self.grindingPassInput_1.get())
        self.data["machining"][0]["feedForw"] = float(self.feedForwardInput_1.get())
        self.data["machining"][0]["feedBack"] = float(self.feedBackwardInput_1.get())
        self.data["machining"][0]["infeedForw"] = float(self.infeedForwardInput_1.get())
        self.data["machining"][0]["infeedBack"] = float(self.infeedBackwardInput_1.get())
        self.data["machining"][0]["pluge"] = float(self.plungFeedInput_1.get())
        self.data["machining"][0]["dressPass"] = int(self.dresssingPassInput_1.get())
        self.data["machining"][0]["dressInfeed"] = float(self.dresssingInfeedInput_1.get())
        self.data["machining"][0]["dressFeed"] = float(self.dressingFeedInput_1.get())
        self.data["machining"][0]["dressFrq"] =  int(self.dressingFrqInput_1.get())

        self.data["machining"][1]["passes"] = int(self.grindingPassInput_2.get())
        self.data["machining"][1]["feedForw"] = float(self.feedForwardInput_2.get())
        self.data["machining"][1]["feedBack"] = float(self.feedBackwardInput_2.get())
        self.data["machining"][1]["infeedForw"] = float(self.infeedForwardInput_2.get())
        self.data["machining"][1]["infeedBack"] = float(self.infeedBackwardInput_2.get())
        self.data["machining"][1]["pluge"] = float(self.plungFeedInput_2.get())
        self.data["machining"][1]["dressPass"] = int(self.dresssingPassInput_2.get())
        self.data["machining"][1]["dressInfeed"] = float(self.dresssingInfeedInput_2.get())
        self.data["machining"][1]["dressFeed"] = float(self.dressingFeedInput_2.get())
        self.data["machining"][1]["dressFrq"] =  int(self.dressingFrqInput_2.get())

        self.data["machining"][2]["passes"] = int(self.grindingPassInput_3.get())
        self.data["machining"][2]["feedForw"] = float(self.feedForwardInput_3.get())
        self.data["machining"][2]["feedBack"] = float(self.feedBackwardInput_3.get())
        self.data["machining"][2]["infeedForw"] = float(self.infeedForwardInput_3.get())
        self.data["machining"][2]["infeedBack"] = float(self.infeedBackwardInput_3.get())
        self.data["machining"][2]["pluge"] = float(self.plungFeedInput_3.get())
        self.data["machining"][2]["dressPass"] = int(self.dresssingPassInput_3.get())
        self.data["machining"][2]["dressInfeed"] = float(self.dresssingInfeedInput_3.get())
        self.data["machining"][2]["dressFeed"] = float(self.dressingFeedInput_3.get())
        self.data["machining"][2]["dressFrq"] =  int(self.dressingFrqInput_3.get())

        self.data["machining"][3]["passes"] = int(self.grindingPassInput_4.get())
        self.data["machining"][3]["feedForw"] = float(self.feedForwardInput_4.get())
        self.data["machining"][3]["feedBack"] = float(self.feedBackwardInput_4.get())
        self.data["machining"][3]["infeedForw"] = float(self.infeedForwardInput_4.get())
        self.data["machining"][3]["infeedBack"] = float(self.infeedBackwardInput_4.get())
        self.data["machining"][3]["pluge"] = float(self.plungFeedInput_4.get())
        self.data["machining"][3]["dressPass"] = int(self.dresssingPassInput_4.get())
        self.data["machining"][3]["dressInfeed"] = float(self.dresssingInfeedInput_4.get())
        self.data["machining"][3]["dressFeed"] = float(self.dressingFeedInput_4.get())
        self.data["machining"][3]["dressFrq"] =  int(self.dressingFrqInput_4.get())
        #self.statusbar.config(text = "Bad input!")
        return self.data

    def setData(self, data):
        self.data = data
        self.grindingPassInput_1.delete(0, 'end')
        self.grindingPassInput_1.insert('end', str(self.data["machining"][0]["passes"]))
        self.feedForwardInput_1.delete(0, 'end')
        self.feedForwardInput_1.insert('end', str(self.data["machining"][0]["feedForw"]))
        self.feedBackwardInput_1.delete(0, 'end')
        self.feedBackwardInput_1.insert('end', str(self.data["machining"][0]["feedBack"]))
        self.infeedForwardInput_1.delete(0, 'end')
        self.infeedForwardInput_1.insert('end', str(self.data["machining"][0]["infeedForw"]))
        self.infeedBackwardInput_1.delete(0, 'end')
        self.infeedBackwardInput_1.insert('end', str(self.data["machining"][0]["infeedBack"]))
        self.plungFeedInput_1.delete(0, 'end')
        self.plungFeedInput_1.insert('end', str(self.data["machining"][0]["plunge"]))
        self.dresssingPassInput_1.delete(0, 'end')
        self.dresssingPassInput_1.insert('end', str(self.data["machining"][0]["dressPass"]))
        self.dresssingInfeedInput_1.delete(0, 'end')
        self.dresssingInfeedInput_1.insert('end', str(self.data["machining"][0]["dressInfeed"]))
        self.dressingFeedInput_1.delete(0, 'end')
        self.dressingFeedInput_1.insert('end', str(self.data["machining"][0]["dressFeed"]))
        self.dressingFrqInput_1.delete(0, 'end')
        self.dressingFrqInput_1.insert('end', str(self.data["machining"][0]["dressFrq"]))

        self.grindingPassInput_2.delete(0, 'end')
        self.grindingPassInput_2.insert('end', str(self.data["machining"][1]["passes"]))
        self.feedForwardInput_2.delete(0, 'end')
        self.feedForwardInput_2.insert('end', str(self.data["machining"][1]["feedForw"]))
        self.feedBackwardInput_2.delete(0, 'end')
        self.feedBackwardInput_2.insert('end', str(self.data["machining"][1]["feedBack"]))
        self.infeedForwardInput_2.delete(0, 'end')
        self.infeedForwardInput_2.insert('end', str(self.data["machining"][1]["infeedForw"]))
        self.infeedBackwardInput_2.delete(0, 'end')
        self.infeedBackwardInput_2.insert('end', str(self.data["machining"][1]["infeedBack"]))
        self.plungFeedInput_2.delete(0, 'end')
        self.plungFeedInput_2.insert('end', str(self.data["machining"][1]["plunge"]))
        self.dresssingPassInput_2.delete(0, 'end')
        self.dresssingPassInput_2.insert('end', str(self.data["machining"][1]["dressPass"]))
        self.dresssingInfeedInput_2.delete(0, 'end')
        self.dresssingInfeedInput_2.insert('end', str(self.data["machining"][1]["dressInfeed"]))
        self.dressingFeedInput_2.delete(0, 'end')
        self.dressingFeedInput_2.insert('end', str(self.data["machining"][1]["dressFeed"]))
        self.dressingFrqInput_2.delete(0, 'end')
        self.dressingFrqInput_2.insert('end', str(self.data["machining"][1]["dressFrq"]))

        self.grindingPassInput_3.delete(0, 'end')
        self.grindingPassInput_3.insert('end', str(self.data["machining"][2]["passes"]))
        self.feedForwardInput_3.delete(0, 'end')
        self.feedForwardInput_3.insert('end', str(self.data["machining"][2]["feedForw"]))
        self.feedBackwardInput_3.delete(0, 'end')
        self.feedBackwardInput_3.insert('end', str(self.data["machining"][2]["feedBack"]))
        self.infeedForwardInput_3.delete(0, 'end')
        self.infeedForwardInput_3.insert('end', str(self.data["machining"][2]["infeedForw"]))
        self.infeedBackwardInput_3.delete(0, 'end')
        self.infeedBackwardInput_3.insert('end', str(self.data["machining"][2]["infeedBack"]))
        self.plungFeedInput_3.delete(0, 'end')
        self.plungFeedInput_3.insert('end', str(self.data["machining"][2]["plunge"]))
        self.dresssingPassInput_3.delete(0, 'end')
        self.dresssingPassInput_3.insert('end', str(self.data["machining"][2]["dressPass"]))
        self.dresssingInfeedInput_3.delete(0, 'end')
        self.dresssingInfeedInput_3.insert('end', str(self.data["machining"][2]["dressInfeed"]))
        self.dressingFeedInput_3.delete(0, 'end')
        self.dressingFeedInput_3.insert('end', str(self.data["machining"][2]["dressFeed"]))
        self.dressingFrqInput_3.delete(0, 'end')
        self.dressingFrqInput_3.insert('end', str(self.data["machining"][2]["dressFrq"]))

        self.grindingPassInput_4.delete(0, 'end')
        self.grindingPassInput_4.insert('end', str(self.data["machining"][3]["passes"]))
        self.feedForwardInput_4.delete(0, 'end')
        self.feedForwardInput_4.insert('end', str(self.data["machining"][3]["feedForw"]))
        self.feedBackwardInput_4.delete(0, 'end')
        self.feedBackwardInput_4.insert('end', str(self.data["machining"][3]["feedBack"]))
        self.infeedForwardInput_4.delete(0, 'end')
        self.infeedForwardInput_4.insert('end', str(self.data["machining"][3]["infeedForw"]))
        self.infeedBackwardInput_4.delete(0, 'end')
        self.infeedBackwardInput_4.insert('end', str(self.data["machining"][3]["infeedBack"]))
        self.plungFeedInput_4.delete(0, 'end')
        self.plungFeedInput_4.insert('end', str(self.data["machining"][3]["plunge"]))
        self.dresssingPassInput_4.delete(0, 'end')
        self.dresssingPassInput_4.insert('end', str(self.data["machining"][3]["dressPass"]))
        self.dresssingInfeedInput_4.delete(0, 'end')
        self.dresssingInfeedInput_4.insert('end', str(self.data["machining"][3]["dressInfeed"]))
        self.dressingFeedInput_4.delete(0, 'end')
        self.dressingFeedInput_4.insert('end', str(self.data["machining"][3]["dressFeed"]))
        self.dressingFrqInput_4.delete(0, 'end')
        self.dressingFrqInput_4.insert('end', str(self.data["machining"][3]["dressFrq"]))

        self.dressingTimeOutput_1.delete(0, 'end')
        self.dressingTimeOutput_2.delete(0, 'end')
        self.dressingTimeOutput_3.delete(0, 'end')
        self.dressingTimeOutput_4.delete(0, 'end')
        self.setCycleTimeOutput_1.delete(0, 'end')
        self.setCycleTimeOutput_2.delete(0, 'end')
        self.setCycleTimeOutput_3.delete(0, 'end')
        self.setCycleTimeOutput_4.delete(0, 'end')
        self.totalCycleTimeOutput.delete(0, 'end')


class StatusBar(Label):
    def __init__(self, master):
        Label.__init__(self, master)
        self.config(text = "Welcome~~", relief=SUNKEN, anchor=W)
        self.pack(side=BOTTOM, fill=X)


class Control:
    def __init__(self, root):
        self.view = MainView(root)
        menubar = Menu(root)
        self.filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label = "File", menu=self.filemenu)
        self.filemenu.add_command(label = "New", command=self.newData)
        self.filemenu.add_command(label = "Open", command=self.openData)
        self.filemenu.add_command(label = "Save", command=self.saveData)
        self.filemenu.add_command(label = "Save As...", command=self.saveAs)
        self.filemenu.add_command(label = "Import", command=self.loadData)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Exit", command=root.quit)
        root.config(menu=menubar)
        self.statusbar = StatusBar(root)
        self.view.nb2.calcuateBtn.config(command=self.doCalcuate)
        self.newData()

        self.file_opt = options = {}
        options['defaultextension'] = '.json'
        options['filetypes'] = [('all files', '.json')]
        options['initialdir'] = './'
        options['initialfile'] = 'data.json'
        options['title'] = 'Choose a path'

    def newData(self):
        try:
            del self.g
            del self.file_path
        except AttributeError:
            pass
        self.g = Gear()
        self.g.addObserver(self.dataUpdate)
        self.g.notify()
        self.statusbar.config(text = "Please input data.")

    def openData(self):
        self.file_path = filedialog.askopenfilename(**self.file_opt)
        if self.file_path:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            self.g.setData(data)
            self.statusbar.config(text = "File Loaded!")

    # input: CycleTime.data, Gear.data
    # output: config file
    def saveData(self):
        data = self.view.nb2.getData()
        data.update(self.view.nb1.getData())

        try:
            with open(self.file_path, 'w') as f:
                data = self.g.getData()
                json.dump(data, f, indent=4)
                self.statusbar.config(text = self.file_path + ' Saved!')
        except (AttributeError, FileNotFoundError):
            self.file_path = filedialog.asksaveasfilename(**self.file_opt)
            if self.file_path:
                with open(self.file_path, 'w') as f:
                    data = self.g.getData()
                    json.dump(data, f, indent=4)
                    self.statusbar.config(text = self.file_path + ' Saved!')

    def saveAs(self):
        self.file_path = filedialog.asksaveasfilename(**self.file_opt)
        if self.file_path:
            with open(self.file_path, 'w') as f:
                data = self.g.getData()
                json.dump(data, f, indent=4)

    # input: config file
    # output: CycleTime.data, Gear.data
    def loadData(self):
        import_path = filedialog.askopenfilename()
        if import_path:
            f = open(import_path, 'r', encoding="big5")
            value = []
            for i in range(0,185,1):
                line = f.readline()
                j = line.find(',')
                value.append(line[j+1:].rstrip())
            f.close()
            data = {
                        "workID": "",
                        "parts": {
                            "productID": value[1],
                            "module": float(value[4]),
                            "normPressAng_d": int(value[4]),
                            "normPressAng_m": int(value[5]),
                            "normPressAng_s": int(value[6]),
                            "starts": int(value[9]),
                            "pitchDia": float(value[7]),
                            "outDia": float(value[8]),
                            "rootDia": float(value[10]),
                            "leadAng_d": int(value[12]),
                            "leadAng_m": int(value[13]),
                            "leadAng_s": int(value[14]),
                            "toothThick": float(value[22]),
                            "threadLen": float(value[20])
                        },
                        "machining": [
                            {
                                "passes": int(value[77]),
                                "feedForw": float(value[79]),
                                "feedBack": float(value[80]),
                                "infeedForw": float(value[82]),
                                "infeedBack": float(value[84]),
                                "infeedTotal": 0,
                                "plunge": float(value[123]),
                                "speed": 0,
                                "dressPass": int(value[68]),
                                "dressInfeed": float(value[70]),
                                "dressFeed": float(value[72]),
                                "dressFrq": int(value[75])
                            },
                            {
                                "passes": int(value[78]),
                                "feedForw": float(value[106]),
                                "feedBack": float(value[107]),
                                "infeedForw": float(value[9]),
                                "infeedBack": float(value[83]),
                                "infeedTotal": 0,
                                "plunge": float(value[85]),
                                "speed": 0,
                                "dressPass": int(value[69]),
                                "dressInfeed": float(value[71]),
                                "dressFeed": float(value[73]),
                                "dressFrq": int(value[76])
                            },
                            {
                                "passes": int(value[134]),
                                "feedForw": float(value[135]),
                                "feedBack": float(value[136]),
                                "infeedForw": float(value[137]),
                                "infeedBack": float(value[138]),
                                "infeedTotal": 0,
                                "plunge": float(value[140]),
                                "speed": 0,
                                "dressPass": int(value[142]),
                                "dressInfeed": float(value[143]),
                                "dressFeed": float(value[144]),
                                "dressFrq": int(value[145])
                            },
                            {
                                "passes": int(value[146]),
                                "feedForw": float(value[147]),
                                "feedBack": float(value[148]),
                                "infeedForw": float(value[150]),
                                "infeedBack": float(value[151]),
                                "infeedTotal": 0,
                                "plunge": float(value[152]),
                                "speed": 0,
                                "dressPass": int(value[154]),
                                "dressInfeed": float(value[155]),
                                "dressFeed": float(value[156]),
                                "dressFrq": int(value[157])
                            }
                        ]
                    }

            self.g.setData(data)
            self.statusbar.config(text = ".dat File Imported!")

    # input:
    def doCalcuate(self):
        self.view.nb2.dressingTimeOutput_1.delete(0, 'end')
        self.view.nb2.setCycleTimeOutput_1.delete(0, 'end')
        self.view.nb2.dressingTimeOutput_2.delete(0, 'end')
        self.view.nb2.setCycleTimeOutput_2.delete(0, 'end')
        self.view.nb2.dressingTimeOutput_3.delete(0, 'end')
        self.view.nb2.setCycleTimeOutput_3.delete(0, 'end')
        self.view.nb2.dressingTimeOutput_4.delete(0, 'end')
        self.view.nb2.setCycleTimeOutput_4.delete(0, 'end')
        self.view.nb2.totalCycleTimeOutput.delete(0, 'end')
        try:
            data = self.view.nb2.getData()
            data.update(self.view.nb1.getData())
        except ValueError:
            self.statusbar.config(text = "Invalid input!")
        else:
            self.g.setData(data)
            self.g.toCalculate()
            self.view.nb2.dressingTimeOutput_1.insert('end', self.timeFrom(int(self.g.dressTime_1)))
            self.view.nb2.setCycleTimeOutput_1.insert('end', self.timeFrom(int(self.g.grindTime_1)))
            self.view.nb2.dressingTimeOutput_2.insert('end', self.timeFrom(int(self.g.dressTime_2)))
            self.view.nb2.setCycleTimeOutput_2.insert('end', self.timeFrom(int(self.g.grindTime_2)))
            self.view.nb2.dressingTimeOutput_3.insert('end', self.timeFrom(int(self.g.dressTime_3)))
            self.view.nb2.setCycleTimeOutput_3.insert('end', self.timeFrom(int(self.g.grindTime_3)))
            self.view.nb2.dressingTimeOutput_4.insert('end', self.timeFrom(int(self.g.dressTime_4)))
            self.view.nb2.setCycleTimeOutput_4.insert('end', self.timeFrom(int(self.g.grindTime_4)))
            self.view.nb2.totalCycleTimeOutput.insert('end', self.timeFrom(int(self.g.cycleTime)))
            self.statusbar.config(text = "Success!")

    def dataUpdate(self, data):
        self.view.nb2.setData(data)
        self.view.nb1.setData(data)
        self.view.setData(data)

    def statusText(self, text):
        self.statusbar.config(text = text)

    def readFile(self):
        filename = askopenfilename()
        f = open(filename, 'r', encoding="big5")
        item = data = []
        for i in range(185):
            line = f.readline()
            j = line.find(',')
            item.append(line[0:j])
            value.append(line[j+1:])
        f.close()

        self.app.nb2.setData()
        self.g.setData([float(0)] * 11)

    def timeFrom(self, sec):
        (hr, mi) = divmod(sec, 360)
        (mi, sec) = divmod(mi, 60)
        return str(hr) + ':' + str(mi) + ':' + str(sec)

    def stop(self):
        pass

if __name__ == '__main__':
    root = Tk()
    root.title("Cycle Time Calculator")
    app = Control(root)
    root.mainloop()
