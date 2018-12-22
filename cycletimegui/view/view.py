import tkinter as tk
from tkinter import ttk
from .importpage import ImportPage
from .cycletimepage import CycleTimePage


class MainView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.workIdEntry = tk.Label(self, justify="center")
        self.workIdEntry.pack()

        self.tabbar = ttk.Notebook(self)
        self.tabbar.pack()
        self.import_tab = ImportPage(self.tabbar)
        self.cycletime_tab = CycleTimePage(self.tabbar)
        self.tabbar.add(self.import_tab, text="Gear Data")
        self.tabbar.add(self.cycletime_tab, text="Machining Cycle")

        self.menubar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menubar, tearoff=0)        
        self.menubar.add_cascade(label = "File", menu=self.file_menu)

        self.statusbar = StatusBar(master)

    def getData(self):
        data = {}
        data['parts'] = self.import_tab.getData()
        data['machining'] = self.cycletime_tab.getData()
        return data

    def setData(self, data):
        self.import_tab.setData(data)
        self.cycletime_tab.setData(data)
        self.workIdEntry.config(text = str(data["workID"]))


class StatusBar(tk.Label):
    def __init__(self, master):
        super().__init__(master)
        self.config(text = "Welcome~~", relief="sunken", anchor="w")
        self.pack(side="bottom", fill="x")
        