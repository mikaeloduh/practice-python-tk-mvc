import tkinter as tk


class ImportPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        # row 0
        self.part_no_label = tk.Label(self, text = "Part No.")
        self.part_no_label.grid(row=0, column=0, sticky="w")
        self.part_no_entry = tk.Entry(self)
        self.part_no_entry.grid(row=0, column=1, columnspan=3)
        # row 1
        self.dp_label = tk.Label(self, text = "DP")
        self.dp_label.grid(row=1, column=0, sticky="w")
        self.dp_entry = tk.Entry(self)
        self.dp_entry.grid(row=1, column=1, columnspan=3)
        # row 2
        self.normal_pa_label = tk.Label(self, text = "Normal Pressure Angle")
        self.normal_pa_label.grid(row=2, column=0, sticky="w")
        self.normal_pa_entry_1 = tk.Entry(self, width = 6)
        self.normal_pa_entry_1.grid(row=2, column=1, columnspan=1)
        self.normal_pa_entry_2 = tk.Entry(self, width = 6)
        self.normal_pa_entry_2.grid(row=2, column=2, columnspan=1)
        self.normal_pa_entry_3 = tk.Entry(self, width = 6)
        self.normal_pa_entry_3.grid(row=2, column=3, columnspan=1)
        # row 3
        self.strats_label = tk.Label(self, text = "Starts")
        self.strats_label.grid(row=3, column=0, sticky="w")
        self.start_entry = tk.Entry(self)
        self.start_entry.grid(row=3, column=1, columnspan=3)
        # row 4
        self.pitch_dia_lable = tk.Label(self, text = "Pitch Diameter")
        self.pitch_dia_lable.grid(row=4, column=0, sticky="w")
        self.pitch_dia_entry = tk.Entry(self)
        self.pitch_dia_entry.grid(row=4, column=1, columnspan=3)
        # row 5
        self.outside_dia_label = tk.Label(self, text = "Outside Diameter")
        self.outside_dia_label.grid(row=5, column=0, sticky="w")
        self.outside_dia_entry = tk.Entry(self)
        self.outside_dia_entry.grid(row=5, column=1, columnspan=3)
        # row 6
        self.roote_dia_lable = tk.Label(self, text = "Root Diameter")
        self.roote_dia_lable.grid(row=6, column=0, sticky="w")
        self.roote_dia_entry = tk.Entry(self)
        self.roote_dia_entry.grid(row=6, column=1, columnspan=3)
        # row 7
        self.lead_angle_label = tk.Label(self, text = "Lead Angle")
        self.lead_angle_label.grid(row=7, column=0, sticky="w")
        self.lead_angle_entry_1 = tk.Entry(self, width = 6)
        self.lead_angle_entry_1.grid(row=7, column=1, columnspan=1)
        self.lead_angle_entry_2 = tk.Entry(self, width = 6)
        self.lead_angle_entry_2.grid(row=7, column=2, columnspan=1)
        self.lead_angle_entry_3 = tk.Entry(self, width = 6)
        self.lead_angle_entry_3.grid(row=7, column=3, columnspan=1)
        # row 8
        self.tooth_thicken_label = tk.Label(self, text = "Tooth Thickness (Axial)")
        self.tooth_thicken_label.grid(row=8, column=0, sticky="w")
        self.tooth_thickn_entry = tk.Entry(self)
        self.tooth_thickn_entry.grid(row=8, column=1, columnspan=3)
        # row 9
        self.thread_length_label = tk.Label(self, text = "Thread Length")
        self.thread_length_label.grid(row=9, column=0, sticky="w")
        self.thread_length_entry = tk.Entry(self)
        self.thread_length_entry.grid(row=9, column=1, columnspan=3)

    def getData(self):
        # Try to make it a float
        self.data["parts"]["productID"] = self.part_no_entry.get()
        self.data["parts"]["module"] = float(self.dp_entry.get())
        self.data["parts"]["normPressAng_d"] = int(self.normal_pa_entry_1.get())
        self.data["parts"]["normPressAng_m"] = int(self.normal_pa_entry_2.get())
        self.data["parts"]["normPressAng_s"] = int(self.normal_pa_entry_3.get())
        self.data["parts"]["starts"] = int(self.start_entry.get())
        self.data["parts"]["pitchDia"] = float(self.pitch_dia_entry.get())
        self.data["parts"]["outDia"] = float(self.outside_dia_entry.get())
        self.data["parts"]["rootDia"] = float(self.roote_dia_entry.get())
        self.data["parts"]["leadAng_d"] = int(self.lead_angle_entry_1.get())
        self.data["parts"]["leadAng_m"] = int(self.lead_angle_entry_2.get())
        self.data["parts"]["leadAng_s"] = int(self.lead_angle_entry_3.get())
        self.data["parts"]["toothThick"] = float(self.tooth_thickn_entry.get())
        self.data["parts"]["threadLen"] = float(self.thread_length_entry.get())

        return self.data

    def setData(self, data):
        self.data = data

        self.part_no_entry.delete(0, 'end')
        self.part_no_entry.insert('end', str(self.data["parts"]["productID"]))
        self.dp_entry.delete(0, 'end')
        self.dp_entry.insert('end', str(self.data["parts"]["module"]))
        self.normal_pa_entry_1.delete(0, 'end')
        self.normal_pa_entry_1.insert('end', str(self.data["parts"]["normPressAng_d"]))
        self.normal_pa_entry_2.delete(0, 'end')
        self.normal_pa_entry_2.insert('end', str(self.data["parts"]["normPressAng_m"]))
        self.normal_pa_entry_3.delete(0, 'end')
        self.normal_pa_entry_3.insert('end', str(self.data["parts"]["normPressAng_s"]))
        self.start_entry.delete(0, 'end')
        self.start_entry.insert('end', str(self.data["parts"]["starts"]))
        self.pitch_dia_entry.delete(0, 'end')
        self.pitch_dia_entry.insert('end', str(self.data["parts"]["pitchDia"]))
        self.outside_dia_entry.delete(0, 'end')
        self.outside_dia_entry.insert('end', str(self.data["parts"]["outDia"]))
        self.roote_dia_entry.delete(0, 'end')
        self.roote_dia_entry.insert('end', str(self.data["parts"]["rootDia"]))
        self.lead_angle_entry_1.delete(0, 'end')
        self.lead_angle_entry_1.insert('end', str(self.data["parts"]["leadAng_d"]))
        self.lead_angle_entry_2.delete(0, 'end')
        self.lead_angle_entry_2.insert('end', str(self.data["parts"]["leadAng_m"]))
        self.lead_angle_entry_3.delete(0, 'end')
        self.lead_angle_entry_3.insert('end', str(self.data["parts"]["leadAng_s"]))
        self.tooth_thickn_entry.delete(0, 'end')
        self.tooth_thickn_entry.insert('end', str(self.data["parts"]["toothThick"]))
        self.thread_length_entry.delete(0, 'end')
        self.thread_length_entry.insert('end', str(self.data["parts"]["threadLen"]))
