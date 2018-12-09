# from tkinter import *
# from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk


class CycleTimePage(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.tabs = ttk.Notebook(self)
        self.createWidgets()
        self.data = {}#[float(0)] * 11

    def createWidgets(self):
        self.panedWindow = ttk.Panedwindow(self, orient="vertical")
        self.panedWindow.grid()

        ########## Labelframe: Grinding ############
        self.grindFrame = ttk.Labelframe(self.panedWindow, text = "Grinding")
        self.grindFrame.grid(row=0, column=0)
        # Label 1
        self.label_I = tk.Label(self.grindFrame, text = "I")
        self.label_I.grid(row=0, column=1)
        # Label 2
        self.label_II = tk.Label(self.grindFrame, text = "II")
        self.label_II.grid(row=0, column=2)
        # Label 3
        self.label_III = tk.Label(self.grindFrame, text = "III")
        self.label_III.grid(row=0, column=3)
        # Label 4
        self.label_IV = tk.Label(self.grindFrame, text = "IV")
        self.label_IV.grid(row=0, column=4)

        # row 1: passes
        # label 0
        self.grindingPassLabel = tk.Label(self.grindFrame, text = "                  Passes")
        self.grindingPassLabel.grid(row=1, column=0, sticky="e")
        # Entry 1
        #self.p1 = IntVar()
        self.grindingPassInput_1 = tk.Entry(self.grindFrame, width=5)#, textvariable = self.p1)
        self.grindingPassInput_1.grid(row=1, column=1)
        # Entry 2
        self.grindingPassInput_2 = tk.Entry(self.grindFrame, width=5)
        self.grindingPassInput_2.grid(row=1, column=2)
        # Entry 3
        self.grindingPassInput_3 = tk.Entry(self.grindFrame, width=5)
        self.grindingPassInput_3.grid(row=1, column=3)
        # Entry 4
        self.grindingPassInput_4 = tk.Entry(self.grindFrame, width=5)
        self.grindingPassInput_4.grid(row=1, column=4)

        # row 2: Feed-Forward
        # label 0
        self.feedForwardLabel = tk.Label(self.grindFrame, text = "Feed-Forward")
        self.feedForwardLabel.grid(row=2, column=0, sticky="e")
        # Entry 1
        self.feedForwardInput_1 = tk.Entry(self.grindFrame, width=5)
        self.feedForwardInput_1.grid(row=2, column=1)
        # Entry 2
        self.feedForwardInput_2 = tk.Entry(self.grindFrame, width=5)
        self.feedForwardInput_2.grid(row=2, column=2)
        # Entry 3
        self.feedForwardInput_3 = tk.Entry(self.grindFrame, width=5)
        self.feedForwardInput_3.grid(row=2, column=3)
        # Entry 4
        self.feedForwardInput_4 = tk.Entry(self.grindFrame, width=5)
        self.feedForwardInput_4.grid(row=2, column=4)

        # row 3: Feed-Backward
        # label 0
        self.feedBackwardLabel = tk.Label(self.grindFrame, text = "Feed-Backward")
        self.feedBackwardLabel.grid(row=3, column=0, sticky="e")
        # Entry 1
        self.feedBackwardInput_1 = tk.Entry(self.grindFrame, width=5)
        self.feedBackwardInput_1.grid(row=3, column=1)
        # Entry 2
        self.feedBackwardInput_2 = tk.Entry(self.grindFrame, width=5)
        self.feedBackwardInput_2.grid(row=3, column=2)
        # Entry 3
        self.feedBackwardInput_3 = tk.Entry(self.grindFrame, width=5)
        self.feedBackwardInput_3.grid(row=3, column=3)
        # Entry 4
        self.feedBackwardInput_4 = tk.Entry(self.grindFrame, width=5)
        self.feedBackwardInput_4.grid(row=3, column=4)

        # row 4: Infeed-Forward
        # label 0
        self.infeedForwardLabel = tk.Label(self.grindFrame, text = "Infeed-Forward")
        self.infeedForwardLabel.grid(row=4, column=0, sticky="e")
        # Entry 1
        self.infeedForwardInput_1 = tk.Entry(self.grindFrame, width=5)
        self.infeedForwardInput_1.grid(row=4, column=1)
        # Entry 2
        self.infeedForwardInput_2 = tk.Entry(self.grindFrame, width=5)
        self.infeedForwardInput_2.grid(row=4, column=2)
        # Entry 3
        self.infeedForwardInput_3 = tk.Entry(self.grindFrame, width=5)
        self.infeedForwardInput_3.grid(row=4, column=3)
        # Entry 4
        self.infeedForwardInput_4 = tk.Entry(self.grindFrame, width=5)
        self.infeedForwardInput_4.grid(row=4, column=4)

        # row 5 : Infeed-Backward
        # Label 0
        self.infeedBackwardLabel = tk.Label(self.grindFrame, text = "Infeed-Backward")
        self.infeedBackwardLabel.grid(row=5, column=0, sticky="e")
        # Entry 1
        self.infeedBackwardInput_1 = tk.Entry(self.grindFrame, width=5)
        self.infeedBackwardInput_1.grid(row=5, column=1)
        # Entry 2
        self.infeedBackwardInput_2 = tk.Entry(self.grindFrame, width=5)
        self.infeedBackwardInput_2.grid(row=5, column=2)
        # Entry 3
        self.infeedBackwardInput_3 = tk.Entry(self.grindFrame, width=5)
        self.infeedBackwardInput_3.grid(row=5, column=3)
        # Entry 4
        self.infeedBackwardInput_4 = tk.Entry(self.grindFrame, width=5)
        self.infeedBackwardInput_4.grid(row=5, column=4)

        # row 6 : Infeed-Total
        # Label 0
        self.totalInfeedLabel = tk.Label(self.grindFrame, text = "Infeed-Total")
        self.totalInfeedLabel.grid(row=6, column=0, sticky="e")
        # Entry 1
        self.totalInfeedOutput_1 = tk.Entry(self.grindFrame, width=5)
        self.totalInfeedOutput_1.grid(row=6, column=1)
        # Entry 2
        self.totalInfeedOutput_2 = tk.Entry(self.grindFrame, width=5)
        self.totalInfeedOutput_2.grid(row=6, column=2)
        # Entry 3
        self.totalInfeedOutput_3 = tk.Entry(self.grindFrame, width=5)
        self.totalInfeedOutput_3.grid(row=6, column=3)
        # Entry 4
        self.totalInfeedOutput_4 = tk.Entry(self.grindFrame, width=5)
        self.totalInfeedOutput_4.grid(row=6, column=4)

        # row 7: Plung Feed
        # Label 0
        self.plungFeedLabel = tk.Label(self.grindFrame, text = "Plung Feed")
        self.plungFeedLabel.grid(row=7, column=0, sticky="e")
        # Entry 1
        self.plungFeedInput_1 = tk.Entry(self.grindFrame, width=5)
        self.plungFeedInput_1.grid(row=7, column=1)
        # Entry 2
        self.plungFeedInput_2 = tk.Entry(self.grindFrame, width=5)
        self.plungFeedInput_2.grid(row=7, column=2)
        # Entry 3
        self.plungFeedInput_3 = tk.Entry(self.grindFrame, width=5)
        self.plungFeedInput_3.grid(row=7, column=3)
        # Entry 4
        self.plungFeedInput_4 = tk.Entry(self.grindFrame, width=5)
        self.plungFeedInput_4.grid(row=7, column=4)

        ############# Labelframe 1: Dressing  ##############
        self.dressFrame = ttk.Labelframe(self.panedWindow, text = "Dressing", width=10000, height=10000)
        self.dressFrame.grid(row=1, column=0)

        # row 0: Dressing Passes
        # Label 0
        self.dresssingPassLabel = tk.Label(self.dressFrame, text = "                  Passes")
        self.dresssingPassLabel.grid(row=0, column=0, sticky="e")
        # Entry 1
        self.dresssingPassInput_1 = tk.Entry(self.dressFrame, width=5)
        self.dresssingPassInput_1.grid(row=0, column=1)
        # Entry 2
        self.dresssingPassInput_2 = tk.Entry(self.dressFrame, width=5)
        self.dresssingPassInput_2.grid(row=0, column=2)
        # Entry 3
        self.dresssingPassInput_3 = tk.Entry(self.dressFrame, width=5)
        self.dresssingPassInput_3.grid(row=0, column=3)
        # Entry 4
        self.dresssingPassInput_4 = tk.Entry(self.dressFrame, width=5)
        self.dresssingPassInput_4.grid(row=0, column=4)

        # row 1: Dressing Infeed
        # Label 0
        self.dressingInfeedLabel = tk.Label(self.dressFrame, text = "InFeed")
        self.dressingInfeedLabel.grid(row=1, column=0, sticky="e")
        # Entry 1
        self.dresssingInfeedInput_1 = tk.Entry(self.dressFrame, width=5)
        self.dresssingInfeedInput_1.grid(row=1, column=1)
        # Entry 2
        self.dresssingInfeedInput_2 = tk.Entry(self.dressFrame, width=5)
        self.dresssingInfeedInput_2.grid(row=1, column=2)
        # Entry 3
        self.dresssingInfeedInput_3 = tk.Entry(self.dressFrame, width=5)
        self.dresssingInfeedInput_3.grid(row=1, column=3)
        # Entry 4
        self.dresssingInfeedInput_4 = tk.Entry(self.dressFrame, width=5)
        self.dresssingInfeedInput_4.grid(row=1, column=4)

        # row 2: Dressing Feed
        # label 0
        self.dressingFeedLabel = tk.Label(self.dressFrame, text = "Feed")
        self.dressingFeedLabel.grid(row=2, column=0, sticky="e")
        # Entry 1
        self.dressingFeedInput_1 = tk.Entry(self.dressFrame, width=5)
        self.dressingFeedInput_1.grid(row=2, column=1)
        # Entry 2
        self.dressingFeedInput_2 = tk.Entry(self.dressFrame, width=5)
        self.dressingFeedInput_2.grid(row=2, column=2)
        # Entry 3
        self.dressingFeedInput_3 = tk.Entry(self.dressFrame, width=5)
        self.dressingFeedInput_3.grid(row=2, column=3)
        # Entry 4
        self.dressingFeedInput_4 = tk.Entry(self.dressFrame, width=5)
        self.dressingFeedInput_4.grid(row=2, column=4)

        # raw 3: Dressing frq.
        # label 0
        self.dressingFrqLabel = tk.Label(self.dressFrame, text = "Dressing Frq.")
        self.dressingFrqLabel.grid(row=3, column=0, sticky="e")

        # row 4: [drop down]
        # Label 0
        self.dressingFrqLabel = tk.Label(self.dressFrame, text = "[By Passes]")
        self.dressingFrqLabel.grid(row=4, column=0, sticky="e")
        # Entry 1
        self.dressingFrqInput_1 = tk.Entry(self.dressFrame, width=5)
        self.dressingFrqInput_1.grid(row=4, column=1)
        # Entry 2
        self.dressingFrqInput_2 = tk.Entry(self.dressFrame, width=5)
        self.dressingFrqInput_2.grid(row=4, column=2)
        # Entry 3
        self.dressingFrqInput_3 = tk.Entry(self.dressFrame, width=5)
        self.dressingFrqInput_3.grid(row=4, column=3)
        # Entry 4
        self.dressingFrqInput_4 = tk.Entry(self.dressFrame, width=5)
        self.dressingFrqInput_4.grid(row=4, column=4)

        ############# Labelframe 2: Cycle Time  ##############
        self.resultFrame = ttk.Labelframe(self.panedWindow, text = " Cycle Time")
        self.resultFrame.grid(row=2, column=0)
        # row 0
        # label 0
        self.dressingSetLabel_1 = tk.Label(self.resultFrame, text = "I")
        self.dressingSetLabel_1.grid(row=0, column=1)
        # label 0
        self.dressingSetLabel_2 = tk.Label(self.resultFrame, text = "II")
        self.dressingSetLabel_2.grid(row=0, column=2)
        # label 0
        self.dressingSetLabel_3 = tk.Label(self.resultFrame, text = "III")
        self.dressingSetLabel_3.grid(row=0, column=3)
        # label 0
        self.dressingSetLabel_4 = tk.Label(self.resultFrame, text = "IV")
        self.dressingSetLabel_4.grid(row=0, column=4)

        # row 1: set dressing time
        # label 0
        self.dressingTimeLabel = tk.Label(self.resultFrame, text = "Set Dressing Time")
        self.dressingTimeLabel.grid(row=1, column=0, sticky="e")
        # Entry 1
        self.dressingTimeOutput_1 = tk.Entry(self.resultFrame, width=5)
        self.dressingTimeOutput_1.grid(row=1, column=1)
        # Entry 2
        self.dressingTimeOutput_2 = tk.Entry(self.resultFrame, width=5)
        self.dressingTimeOutput_2.grid(row=1, column=2)
        # Entry 3
        self.dressingTimeOutput_3 = tk.Entry(self.resultFrame, width=5)
        self.dressingTimeOutput_3.grid(row=1, column=3)
        # Entry 4
        self.dressingTimeOutput_4 = tk.Entry(self.resultFrame, width=5)
        self.dressingTimeOutput_4.grid(row=1, column=4)

        # row 2: Set Cycle time (sec.)
        # label 0
        self.setCycleTimeLabel = tk.Label(self.resultFrame, text = "Set Cycle Time")
        self.setCycleTimeLabel.grid(row=2, column=0, sticky="e")
        # Entry 1
        self.setCycleTimeOutput_1 = tk.Entry(self.resultFrame, width=5)
        self.setCycleTimeOutput_1.grid(row=2, column=1)
        # Entry 2
        self.setCycleTimeOutput_2 = tk.Entry(self.resultFrame, width=5)
        self.setCycleTimeOutput_2.grid(row=2, column=2)
        # Entry 3
        self.setCycleTimeOutput_3 = tk.Entry(self.resultFrame, width=5)
        self.setCycleTimeOutput_3.grid(row=2, column=3)
        # Entry 4
        self.setCycleTimeOutput_4 = tk.Entry(self.resultFrame, width=5)
        self.setCycleTimeOutput_4.grid(row=2, column=4)

        # raw 3: Total Cycle time (sec.)
        # label 0
        self.totalCycleTimeLabel = tk.Label(self.resultFrame, text = "Total Cycle time")
        self.totalCycleTimeLabel.grid(row=3, column=0, sticky="e")
        # Entry 1
        self.totalCycleTimeOutput = tk.Entry(self.resultFrame, width = "11")
        self.totalCycleTimeOutput.grid(row=3, column=1, columnspan=2)
        ################# Button 2 : Calcuate ###################
        self.calcuateBtn = tk.Button(self.resultFrame, width=8, text = "Calcuate")
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
