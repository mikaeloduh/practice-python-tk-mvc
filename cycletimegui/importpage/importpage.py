import tkinter as tk


class ImportPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        # row 0
        self.partNoLabel = tk.Label(self, text = "Part No.")
        self.partNoLabel.grid(row=0, column=0, sticky="w")
        self.partNoEntry = tk.Entry(self)
        self.partNoEntry.grid(row=0, column=1, columnspan=3)
        # row 1
        self.DPLabel = tk.Label(self, text = "DP")
        self.DPLabel.grid(row=1, column=0, sticky="w")
        self.DPEntry = tk.Entry(self)
        self.DPEntry.grid(row=1, column=1, columnspan=3)
        # row 2
        self.normalPALabel = tk.Label(self, text = "Normal Pressure Angle")
        self.normalPALabel.grid(row=2, column=0, sticky="w")
        self.normalPAEntry1 = tk.Entry(self, width = 6)
        self.normalPAEntry1.grid(row=2, column=1, columnspan=1)
        self.normalPAEntry2 = tk.Entry(self, width = 6)
        self.normalPAEntry2.grid(row=2, column=2, columnspan=1)
        self.normalPAEntry3 = tk.Entry(self, width = 6)
        self.normalPAEntry3.grid(row=2, column=3, columnspan=1)
        # row 3
        self.stratsLabel = tk.Label(self, text = "Starts")
        self.stratsLabel.grid(row=3, column=0, sticky="w")
        self.startEntry = tk.Entry(self)
        self.startEntry.grid(row=3, column=1, columnspan=3)
        # row 4
        self.pitchDiaLable = tk.Label(self, text = "Pitch Diameter")
        self.pitchDiaLable.grid(row=4, column=0, sticky="w")
        self.pitchDiaEntry = tk.Entry(self)
        self.pitchDiaEntry.grid(row=4, column=1, columnspan=3)
        # row 5
        self.outsideDiaLabel = tk.Label(self, text = "Outside Diameter")
        self.outsideDiaLabel.grid(row=5, column=0, sticky="w")
        self.outsideDiaEntry = tk.Entry(self)
        self.outsideDiaEntry.grid(row=5, column=1, columnspan=3)
        # row 6
        self.rooteDiaLable = tk.Label(self, text = "Root Diameter")
        self.rooteDiaLable.grid(row=6, column=0, sticky="w")
        self.rooteDiaEntry = tk.Entry(self)
        self.rooteDiaEntry.grid(row=6, column=1, columnspan=3)
        # row 7
        self.leadAngleLabel = tk.Label(self, text = "Lead Angle")
        self.leadAngleLabel.grid(row=7, column=0, sticky="w")
        self.leadAngleEntry1 = tk.Entry(self, width = 6)
        self.leadAngleEntry1.grid(row=7, column=1, columnspan=1)
        self.leadAngleEntry2 = tk.Entry(self, width = 6)
        self.leadAngleEntry2.grid(row=7, column=2, columnspan=1)
        self.leadAngleEntry3 = tk.Entry(self, width = 6)
        self.leadAngleEntry3.grid(row=7, column=3, columnspan=1)
        # row 8
        self.toothThicknLabel = tk.Label(self, text = "Tooth Thickness (Axial)")
        self.toothThicknLabel.grid(row=8, column=0, sticky="w")
        self.toothThicknEntry = tk.Entry(self)
        self.toothThicknEntry.grid(row=8, column=1, columnspan=3)
        # row 9
        self.threadLengthLabel = tk.Label(self, text = "Thread Length")
        self.threadLengthLabel.grid(row=9, column=0, sticky="w")
        self.threadLengthEntry = tk.Entry(self)
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
