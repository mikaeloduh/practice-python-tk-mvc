from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from gear import Gear

import os
import json


class MainView(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=None)
        #frame = Frame(master)
        self.pack()
        #self.createWidgets()

        self.l = Label(self, text = "test02")
        self.l.pack()

    #def createWidgets(self):
        self.nb = Notebook(self)
        self.nb.pack()
        self.notebook1 = ImportGUI(self.nb)
        self.notebook2 = CycleTimeGUI(self.nb)
        self.nb.add(self.notebook1, text="Gear Data")
        self.nb.pack()
        self.nb.add(self.notebook2, text="Machining Cycle")
        self.nb.pack()


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

        self.normalPAEntry = Entry(self)
        self.normalPAEntry.grid(row=2, column=1, columnspan=3)

        # row 3
        self.stratsLabel = Label(self, text = "Starts")
        self.stratsLabel.grid(row=3, column=0, sticky=W)

        self.startEntry = Entry(self)
        self.startEntry.grid(row=3, column=1, columnspan=3)

        # row 4
        self.pitchDiaLable = Label(self, text = "Pitch Diameter")
        self.pitchDiaLable.grid(row=4, column=0, sticky=W)

        self.pitchDiaEntry1 = Entry(self, width = 6)
        self.pitchDiaEntry1.grid(row=4, column=1, columnspan=1)
        self.pitchDiaEntry2 = Entry(self, width = 6)
        self.pitchDiaEntry2.grid(row=4, column=2, columnspan=1)
        self.pitchDiaEntry3 = Entry(self, width = 6)
        self.pitchDiaEntry3.grid(row=4, column=3, columnspan=1)

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
        self.data["module"] = float(self.DPEntry.get())
        self.data["start"] = float(self.startEntry.get())
        self.data["tLength"] = float(self.threadLengthEntry.get())

        return self.data

    def setData(self, data):
        self.data = data
        self.DPEntry.delete(0, 'end')
        self.DPEntry.insert('end', str(self.data["module"]))

        self.startEntry.delete(0, 'end')
        self.startEntry.insert('end', str(self.data["start"]))

        self.threadLengthEntry.delete(0, 'end')
        self.threadLengthEntry.insert('end', str(self.data["tLength"]))


class CycleTimeGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.tabs = Notebook(self)
        self.createWidgets()
        self.data = {}#[float(0)] * 11

    def createWidgets(self):
        self.pw = Panedwindow(self, orient=VERTICAL)
        self.pw.grid()

        # row 0: Set
        ########## Labelframe: Grinding ############
        self.lnotebook1 = Labelframe(self.pw, text = "Grinding")
        self.lnotebook1.grid(row=0, column=0)
        # Label 0

        # Label 1
        self.iLabel = Label(self.lnotebook1, text = "I")
        self.iLabel.grid(row=0, column=1)
        # Label 2
        self.iiLabel = Label(self.lnotebook1, text = "II")
        self.iiLabel.grid(row=0, column=2)
        # Label 3
        self.iiiLabel = Label(self.lnotebook1, text = "III")
        self.iiiLabel.grid(row=0, column=3)
        # Label 4
        self.ivLabel = Label(self.lnotebook1, text = "IV")
        self.ivLabel.grid(row=0, column=4)

        # row 1: passes
        # label 0
        self.grindingPassLabel = Label(self.lnotebook1, text = "                  Passes")
        self.grindingPassLabel.grid(row=1, column=0, sticky=E)
        # Entry 1
        #self.p1 = IntVar()
        self.grindingPassInput_1 = Entry(self.lnotebook1, width=5)#, textvariable = self.p1)
        self.grindingPassInput_1.grid(row=1, column=1)
        # Entry 2
        self.grindingPassInput_2 = Entry(self.lnotebook1, width=5)
        self.grindingPassInput_2.grid(row=1, column=2)
        # Entry 3
        self.grindingPassInput_3 = Entry(self.lnotebook1, width=5)
        self.grindingPassInput_3.grid(row=1, column=3)
        # Entry 4
        self.grindingP4Input = Entry(self.lnotebook1, width=5)
        self.grindingP4Input.grid(row=1, column=4)

        # row 2: Feed-Forward
        # label 0
        self.feedForwardLabel = Label(self.lnotebook1, text = "Feed-Forward")
        self.feedForwardLabel.grid(row=2, column=0, sticky=E)
        # Entry 1
        self.q1 = IntVar()
        self.feedForwardInput_1 = Entry(self.lnotebook1, width=5, textvariable = self.q1)
        self.feedForwardInput_1.grid(row=2, column=1)
        # Entry 2
        self.feedForwardInput_2 = Entry(self.lnotebook1, width=5)
        self.feedForwardInput_2.grid(row=2, column=2)
        # Entry 3
        self.feedForwardInput_3 = Entry(self.lnotebook1, width=5)
        self.feedForwardInput_3.grid(row=2, column=3)
        # Entry 4
        self.feedForwardInput_4 = Entry(self.lnotebook1, width=5)
        self.feedForwardInput_4.grid(row=2, column=4)

        # row 3: Feed-Backward
        # label 0
        self.feedBackwardLabel = Label(self.lnotebook1, text = "Feed-Backward")
        self.feedBackwardLabel.grid(row=3, column=0, sticky=E)
        # Entry 1
        self.r1 = IntVar()
        self.feedBackwardInput_1 = Entry(self.lnotebook1, width=5, textvariable = self.r1)
        self.feedBackwardInput_1.grid(row=3, column=1)
        # Entry 2
        self.feedBackwardInput_2 = Entry(self.lnotebook1, width=5)
        self.feedBackwardInput_2.grid(row=3, column=2)
        # Entry 3
        self.feedBackwardInput_3 = Entry(self.lnotebook1, width=5)
        self.feedBackwardInput_3.grid(row=3, column=3)
        # Entry 4
        self.feedBackwardInput_4 = Entry(self.lnotebook1, width=5)
        self.feedBackwardInput_4.grid(row=3, column=4)
        # row 4: Infeed-Forward
        # label 0
        self.infeedForwardLabel = Label(self.lnotebook1, text = "Infeed-Forward")
        self.infeedForwardLabel.grid(row=4, column=0, sticky=E)
        # Entry 1
        self.s1 = IntVar()
        self.infeedForwardInput_1 = Entry(self.lnotebook1, width=5, textvariable = self.s1)
        self.infeedForwardInput_1.grid(row=4, column=1)
        # Entry 2
        self.infeedForwardInput_2 = Entry(self.lnotebook1, width=5)
        self.infeedForwardInput_2.grid(row=4, column=2)
        # Entry 3
        self.infeedForwardInput_3 = Entry(self.lnotebook1, width=5)
        self.infeedForwardInput_3.grid(row=4, column=3)
        # Entry 4
        self.infeedForwardInput_4 = Entry(self.lnotebook1, width=5)
        self.infeedForwardInput_4.grid(row=4, column=4)

        # row 5 : Infeed-Backward
        self.infeedBackwardLabel = Label(self.lnotebook1, text = "Infeed-Backward")
        self.infeedBackwardLabel.grid(row=5, column=0, sticky=E)
        # Entry 1
        self.t1 = IntVar()
        self.infeedBackwardInput_1 = Entry(self.lnotebook1, width=5, textvariable = self.t1)
        self.infeedBackwardInput_1.grid(row=5, column=1)
        # Entry 2
        self.infeedBackwardInput_2 = Entry(self.lnotebook1, width=5)
        self.infeedBackwardInput_2.grid(row=5, column=2)
        # Entry 3
        self.infeedBackwardInput_3 = Entry(self.lnotebook1, width=5)
        self.infeedBackwardInput_3.grid(row=5, column=3)
        # Entry 4
        self.infeedBackwardInput_4 = Entry(self.lnotebook1, width=5)
        self.infeedBackwardInput_4.grid(row=5, column=4)

        # row 6 : Infeed-Total
        # label 0
        self.totalInfeedLabel = Label(self.lnotebook1, text = "Infeed-Total")
        self.totalInfeedLabel.grid(row=6, column=0, sticky=E)
        # Entry 1
        self.u1 = IntVar()
        self.totalInfeedOutput_1 = Entry(self.lnotebook1, width=5, textvariable = self.u1)
        self.totalInfeedOutput_1.grid(row=6, column=1)
        # Entry 2
        self.totalInfeedOutput_2 = Entry(self.lnotebook1, width=5)
        self.totalInfeedOutput_2.grid(row=6, column=2)
        # Entry 3
        self.totalInfeedOutput_3 = Entry(self.lnotebook1, width=5)
        self.totalInfeedOutput_3.grid(row=6, column=3)
        # Entry 4
        self.totalInfeedOutput_4 = Entry(self.lnotebook1, width=5)
        self.totalInfeedOutput_4.grid(row=6, column=4)

        # row 7: Plung Feed
        # label 0
        self.plungFeedLabel = Label(self.lnotebook1, text = "Plung Feed")
        self.plungFeedLabel.grid(row=7, column=0, sticky=E)
        # Entry 1
        self.v1 = IntVar()
        self.plungFeedInput_1 = Entry(self.lnotebook1, width=5, textvariable = self.v1)
        self.plungFeedInput_1.grid(row=7, column=1)
        # Entry 2
        self.plungFeedInput_2 = Entry(self.lnotebook1, width=5)
        self.plungFeedInput_2.grid(row=7, column=2)
        # Entry 3
        self.plungFeedInput_3 = Entry(self.lnotebook1, width=5)
        self.plungFeedInput_3.grid(row=7, column=3)
        # Entry 4
        self.plungFeedInput_4 = Entry(self.lnotebook1, width=5)
        self.plungFeedInput_4.grid(row=7, column=4)

        ############# row  Labelframe  ##############
        self.lnotebook2 = Labelframe(self.pw, text = "Dressing", width=10000, height=10000)
        self.lnotebook2.grid(row=1, column=0)
        # row 9: Dressing

        # row 10: Dressing Passes
        # label 0
        self.dresssingPassLabel = Label(self.lnotebook2, text = "                  Passes")
        self.dresssingPassLabel.grid(row=10, column=0, sticky=E)
        # Entry 1
        self.w1 = IntVar()
        self.dresssingPassInput_1 = Entry(self.lnotebook2, width=5, textvariable = self.w1)
        self.dresssingPassInput_1.grid(row=10, column=1)
        # Entry 2
        self.dresssingPassInput_2 = Entry(self.lnotebook2, width=5)
        self.dresssingPassInput_2.grid(row=10, column=2)
        # Entry 3
        self.dresssingPassInput_3 = Entry(self.lnotebook2, width=5)
        self.dresssingPassInput_3.grid(row=10, column=3)
        # Entry 4
        self.dresssingPassInput_4 = Entry(self.lnotebook2, width=5)
        self.dresssingPassInput_4.grid(row=10, column=4)

        # row 11: Dressing InFeed
        # label 0
        self.dressingInfeedLabel = Label(self.lnotebook2, text = "InFeed")
        self.dressingInfeedLabel.grid(row=11, column=0, sticky=E)
        # Entry 1
        self.x1 = IntVar()
        self.dresssingInfeedInput_1 = Entry(self.lnotebook2, width=5, textvariable = self.x1)
        self.dresssingInfeedInput_1.grid(row=11, column=1)
        # Entry 2
        self.dresssingInfeedInput_2 = Entry(self.lnotebook2, width=5)
        self.dresssingInfeedInput_2.grid(row=11, column=2)
        # Entry 3
        self.dresssingInfeedInput_3 = Entry(self.lnotebook2, width=5)
        self.dresssingInfeedInput_3.grid(row=11, column=3)
        # Entry 4
        self.dresssingInfeedInput_4 = Entry(self.lnotebook2, width=5)
        self.dresssingInfeedInput_4.grid(row=11, column=4)

        # row 12: Dressing Feed
        # label 0
        self.dressingFeedLabel = Label(self.lnotebook2, text = "Feed")
        self.dressingFeedLabel.grid(row=12, column=0, sticky=E)
        # Entry 1
        self.y1 = IntVar()
        self.dressingFeedInput_1 = Entry(self.lnotebook2, width=5, textvariable = self.y1)
        self.dressingFeedInput_1.grid(row=12, column=1)
        # Entry 2
        self.dressingFeedInput_2 = Entry(self.lnotebook2, width=5)
        self.dressingFeedInput_2.grid(row=12, column=2)
        # Entry 3
        self.dressingFeedInput_3 = Entry(self.lnotebook2, width=5)
        self.dressingFeedInput_3.grid(row=12, column=3)
        # Entry 4
        self.dressingFeedInput_4 = Entry(self.lnotebook2, width=5)
        self.dressingFeedInput_4.grid(row=12, column=4)

        # raw 13: Dressing frq.
        # label 0
        self.dressingFrqLabel = Label(self.lnotebook2, text = "Dressing frq.")
        self.dressingFrqLabel.grid(row=13, column=0, sticky=E)

        # raw 14: [drop down]
        # label 0
        self.dressingFrqLabel = Label(self.lnotebook2, text = "[By Passes]")
        self.dressingFrqLabel.grid(row=14, column=0, sticky=E)
        # Entry 1
        self.z1 = IntVar()
        self.dressingFrqInput_1 = Entry(self.lnotebook2, width=5, textvariable = self.z1)
        self.dressingFrqInput_1.grid(row=14, column=1)
        # Entry 2
        self.dressingFrqInput_2 = Entry(self.lnotebook2, width=5)
        self.dressingFrqInput_2.grid(row=14, column=2)
        # Entry 3
        self.dressingFrqInput_3 = Entry(self.lnotebook2, width=5)
        self.dressingFrqInput_3.grid(row=14, column=3)
        # Entry 4
        self.dressingFrqInput_4 = Entry(self.lnotebook2, width=5)
        self.dressingFrqInput_4.grid(row=14, column=4)

        # 15
        self.lf3 = Labelframe(self.pw, text = " Cycle Time")
        self.lf3.grid(row=2, column=0)

        # label 0
        self.dressingSetLabel_1 = Label(self.lf3, text = "I")
        self.dressingSetLabel_1.grid(row=15, column=1)
        # label 0
        self.dressingSetLabel_2 = Label(self.lf3, text = "II")
        self.dressingSetLabel_2.grid(row=15, column=2)
        # label 0
        self.dressingSetLabel_3 = Label(self.lf3, text = "III")
        self.dressingSetLabel_3.grid(row=15, column=3)
        # label 0
        self.dressingSetLabel_4 = Label(self.lf3, text = "IV")
        self.dressingSetLabel_4.grid(row=15, column=4)

        # raw 16: set dressing time
        # label 0
        self.dressingTimeLabel = Label(self.lf3, text = "Set Dressing Time")
        self.dressingTimeLabel.grid(row=16, column=0, sticky=E)
        # Entry 1
        self.dressingTimeOutput_1 = Entry(self.lf3, width=5)
        self.dressingTimeOutput_1.grid(row=16, column=1)
        # Entry 2
        self.dressingTimeOutput_2 = Entry(self.lf3, width=5)
        self.dressingTimeOutput_2.grid(row=16, column=2)
        # Entry 3
        self.dressingTimeOutput_3 = Entry(self.lf3, width=5)
        self.dressingTimeOutput_3.grid(row=16, column=3)
        # Entry 4
        self.dressingTimeOutput_4 = Entry(self.lf3, width=5)
        self.dressingTimeOutput_4.grid(row=16, column=4)

        # 17
        # raw 18:

        # raw 19: Set Cycle time (sec.)
        # label 0
        self.setCycleTimeLabel = Label(self.lf3, text = "Set Cycle Time")
        self.setCycleTimeLabel.grid(row=19, column=0, sticky=E)
        # Entry 1
        self.setCycleTimeOutput_1 = Entry(self.lf3, width=5)
        self.setCycleTimeOutput_1.grid(row=19, column=1)
        # Entry 2
        self.setCycleTimeOutput_2 = Entry(self.lf3, width=5)
        self.setCycleTimeOutput_2.grid(row=19, column=2)
        # Entry 3
        self.setCycleTimeOutput_3 = Entry(self.lf3, width=5)
        self.setCycleTimeOutput_3.grid(row=19, column=3)
        # Entry 4
        self.setCycleTimeOutput_4 = Entry(self.lf3, width=5)
        self.setCycleTimeOutput_4.grid(row=19, column=4)

        # raw 20: Total Cycle time (sec.)
        # label 0
        self.totalCycleTimeLabel = Label(self.lf3, text = "Total Cycle time")
        self.totalCycleTimeLabel.grid(row=20, column=0, sticky=E)
        # Entry 1
        self.totalCycleTimeOutput = Entry(self.lf3, width = "11")
        self.totalCycleTimeOutput.grid(row=20, column=1, columnspan=2)
        ################# Button 2 : Calcuate ###################
        self.calcuateBtn = Button(self.lf3, width=8, text = "Calcuate")
        self.calcuateBtn.grid(row=20, column=3, columnspan=2)

        # Place 3 Paned window
        self.pw.add(self.lnotebook1)
        self.pw.add(self.lnotebook2)
        self.pw.add(self.lf3)


    def getData(self):
        # Try to make it a float
        self.data["passes"] = float(self.grindingPassInput_1.get())
        self.data["ffeed"] = float(self.feedForwardInput_1.get())
        self.data["dressPass"] = float(self.dresssingPassInput_1.get())
        self.data["dressFeed"] = float(self.dressingFeedInput_1.get())
        self.data["byPass"] =  float(self.dressingFrqInput_1.get())
        #self.statusbar.config(text = "Bad input!")
        return self.data

    def setData(self, data):
        self.data = data
        self.grindingPassInput_1.delete(0, 'end')
        self.grindingPassInput_1.insert('end', str(self.data["passes_1"]))

        self.feedForwardInput_1.delete(0, 'end')
        self.feedForwardInput_1.insert('end', str(self.data["ffeed_1"]))

        self.dresssingPassInput_1.delete(0, 'end')
        self.dresssingPassInput_1.insert('end', str(self.data["dressPass_1"]))

        self.dressingFeedInput_1.delete(0, 'end')
        self.dressingFeedInput_1.insert('end', str(self.data["dressFeed_1"]))

        self.dressingFrqInput_1.delete(0, 'end')
        self.dressingFrqInput_1.insert('end', str(self.data["byPass_1"]))

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
        self.view.notebook2.calcuateBtn.config(command=self.doCalcuate)
        self.newData()

    def newData(self):
        try:
            del self.g
        except AttributeError:
            pass
        self.g = Gear()
        self.g.addObserver(self.dataUpdate)
        self.g.notify()
        self.statusbar.config(text = "Please input data.")

    def openData(self):
        self.file_path = filedialog.askopenfilename()
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        self.g.setData(data)
        self.statusbar.config(text = "File Loaded!")

    # input: config file
    # output: CycleTime.data, Gear.data
    def loadData(self):
        #data = {"module":14, "start":1, "tLength":4.91, "passes":4, "ffeed":150, "dressPass":3, "dressFeed":4, "byPass":3}

        file = open("./Bodine24202376.dat", 'r', encoding="big5")
        value = []
        #with open("./Bodine24202376.dat", 'r', encoding="big5") as file:
        #while file.readline():
        for i in range(0,185,1):
            line = file.readline()
            j = line.find(',')
            value.append(line[j+1:].rstrip())
        file.close()

        data = {
        "partNo":value[1],
        "module":float(value[4]),
        "normPresAng1":float(value[4]),
        "normPresAng3":float(value[5]),
        "normPresAng3":float(value[6]),
        "start":float(value[9]),
        "pitchDia":float(value[7]),
        "ODia":float(value[8]),
        "rootDia":float(value[10]),
        "leadAng1":float(value[12]),
        "leadAng2":float(value[13]),
        "leadAng3":float(value[14]),
        "toothThick":float(value[22]),
        "tLength":float(value[20]),
        "passes_1":float(value[77]), #1
        "ffeed_1":float(value[79]),
        "bfeed_1":float(value[80]),
        "finfeed_1":float(value[82]),
        "binfeed_1":float(value[84]),
        "plung_1":float(value[123]),
        "dressPass_1":float(value[68]),
        "dressInfeed_1":float(value[70]),
        "dressFeed_1":float(value[72]),
        "byPass_1":float(value[75]),
        "passes_2":float(value[78]), #2
        "ffeed_2":float(value[106]),
        "bfeed_2":float(value[107]),
        "finfeed_2":float(value[9]),
        "binfeed_2":float(value[83]),
        "plung_2":float(value[85]),
        "dressPass_2":float(value[69]),
        "dressInfeed_2":float(value[71]),
        "dressFeed_2":float(value[73]),
        "byPass_2":float(value[76]),
        "passes_3":float(value[134]), #3
        "ffeed_3":float(value[135]),
        "bfeed_3":float(value[136]),
        "finfeed_3":float(value[137]),
        "binfeed_3":float(value[138]),
        "plung_3":float(value[140]),
        "dressPass_3":float(value[142]),
        "dressInfeed_3":float(value[143]),
        "dressFeed_3":float(value[144]),
        "byPass_3":float(value[145]),
        "passes_4":float(value[146]), #4
        "ffeed_4":float(value[147]),
        "bfeed_4":float(value[148]),
        "finfeed_4":float(value[150]),
        "binfeed_4":float(value[151]),
        "plung_4":float(value[152]),
        "dressPass_4":float(value[154]),
        "dressInfeed_4":float(value[155]),
        "dressFeed_4":float(value[156]),
        "byPass_4":float(value[157]),
        }

        self.g.setData(data)

        self.statusbar.config(text = ".dat File Imported!")

    # input: CycleTime.data, Gear.data
    # output: config file
    def saveData(self):
        if self.file_path:
            with open(self.file_path, 'w') as f:
                data = self.g.getData()
                json.dump(data, f, indent=4)
        else:
            self.file_path = filedialog.asksaveasfilename()
            with open(self.file_path, 'w') as f:
                data = self.g.getData()
                json.dump(data, f, indent=4)

    def saveAs(self):
        self.file_path = filedialog.asksaveasfilename()
        with open(self.file_path, 'w') as f:
            data = self.g.getData()
            json.dump(data, f, indent=4)
        #self.file_path = filedialog.askopenfilename()

    # input:
    def doCalcuate(self):
        self.view.notebook2.dressingTimeOutput_1.delete(0, 'end')
        self.view.notebook2.setCycleTimeOutput_1.delete(0, 'end')
        self.view.notebook2.totalCycleTimeOutput.delete(0, 'end')
        try:
            data = self.view.notebook2.getData()
            data.update(self.view.notebook1.getData())
        except ValueError:
            self.statusbar.config(text = "Invalid input!")
        else:
            self.g.setData(data)
            self.g.toCalculate()
            self.view.notebook2.dressingTimeOutput_1.insert('end', self.g.setDressingTime1)
            self.view.notebook2.setCycleTimeOutput_1.insert('end', self.g.result1)
            self.view.notebook2.totalCycleTimeOutput.insert('end', self.g.result1)
            self.statusbar.config(text = "Success!")

    def dataUpdate(self, data):
        self.view.notebook2.setData(data)
        self.view.notebook1.setData(data)

    def statusText(self, text):
        self.statusbar.config(text = text)

    def readFile(self):
        filename = askopenfilename()
        file = open(filename, 'r', encoding="big5")
        item = data = []
        for i in range(185):
            line = file.readline()
            j = line.find(',')
            item.append(line[0:j])
            value.append(line[j+1:])
        file.close()

        self.app.notebook2.setData()
        self.g.setData([float(0)] * 11)

    def stop(self):
        pass

if __name__ == '__main__':
    root = Tk()
    root.title("Cycle Time Calculator")
    app = Control(root)
    root.mainloop()
