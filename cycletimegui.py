import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import json
from cycletimegui import Gear
# from importpage import ImportPage
# from cycletimepage import CycleTimePage
from cycletimegui import MainView


# class MainView(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()

#         self.workIdEntry = tk.Label(self, justify="center")
#         self.workIdEntry.pack()

#         self.tabbar = ttk.Notebook(self)
#         self.tabbar.pack()
#         self.import_tab = ImportPage(self.tabbar)
#         self.cycletime_tab = CycleTimePage(self.tabbar)
#         self.tabbar.add(self.import_tab, text="Gear Data")
#         self.tabbar.add(self.cycletime_tab, text="Machining Cycle")

#         self.menubar = tk.Menu(self)
#         self.file_menu = tk.Menu(self.menubar, tearoff=0)        
#         self.menubar.add_cascade(label = "File", menu=self.file_menu)

#         self.statusbar = StatusBar(master)

#     def getData(self):
#         data = {}
#         data['parts'] = self.import_tab.getData()
#         data['machining'] = self.cycletime_tab.getData()
#         return data

#     def setData(self, data):
#         self.import_tab.setData(data)
#         self.cycletime_tab.setData(data)
#         self.workIdEntry.config(text = str(data["workID"]))


# class StatusBar(tk.Label):
#     def __init__(self, master):
#         super().__init__(master)
#         self.config(text = "Welcome~~", relief="sunken", anchor="w")
#         self.pack(side="bottom", fill="x")


class Control:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

        self.newData()
        self.file_opt = options = {}
        options['defaultextension'] = '.json'
        options['filetypes'] = [('all files', '.json')]
        options['initialdir'] = './'
        options['initialfile'] = 'data.json'
        options['title'] = 'Choose a path'

    def create_widgets(self):
        self.root.title("Cycle Time Calculator")

        self.view = MainView(master=self.root)
        self.view.cycletime_tab.calcuate_button.config(command=self.doCalcuate)

        self.view.file_menu.add_command(label = "New", command=self.newData)
        self.view.file_menu.add_command(label = "Open", command=self.openData)
        self.view.file_menu.add_command(label = "Save", command=self.saveData)
        self.view.file_menu.add_command(label = "Save As...", command=self.saveAs)
        self.view.file_menu.add_command(label = "Import", command=self.loadData)
        self.view.file_menu.add_separator()
        self.view.file_menu.add_command(label = "Exit", command=self.root.quit)        
        self.root.config(menu=self.view.menubar)

    def newData(self):
        try:
            del self.gear
            del self.file_path
        except AttributeError:
            pass
        self.gear = Gear()
        self.gear.addObserver(self.view.setData)
        self.gear.notify()
        self.view.statusbar.config(text = "Please input data.")

    def openData(self):
        self.file_path = filedialog.askopenfilename(**self.file_opt)
        if self.file_path:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            self.gear.setData(data)
            self.view.statusbar.config(text = "File Loaded!")

    def saveData(self):
        data  = self.view.getData()
        try:
            with open(self.file_path, 'w') as f:
                data = self.gear.getData()
                json.dump(data, f, indent=4)
                self.statusbar.config(text = self.file_path + ' Saved!')
        except (AttributeError, FileNotFoundError):
            self.file_path = filedialog.asksaveasfilename(**self.file_opt)
            if self.file_path:
                with open(self.file_path, 'w') as f:
                    data = self.gear.getData()
                    json.dump(data, f, indent=4)
                    self.view.statusbar.config(text = self.file_path + ' Saved!')

    def saveAs(self):
        self.file_path = filedialog.asksaveasfilename(**self.file_opt)
        if self.file_path:
            with open(self.file_path, 'w') as f:
                data = self.gear.getData()
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

            self.newData()
            self.gear.setData(data)
            self.view.statusbar.config(text = ".dat File Imported!")

    def doCalcuate(self):
        try:
            data = self.view.getData()
        except ValueError:
            self.view.statusbar.config(text = "Invalid input!")
        else:
            self.gear.setData(data)
            result = self.gear.toCalculate()
            self.view.cycletime_tab.set_result(result)
            self.view.statusbar.config(text = "Success!")


if __name__ == '__main__':
    root = tk.Tk()
    app = Control(root)
    root.mainloop()
