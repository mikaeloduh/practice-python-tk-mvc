import os
import json
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from importtable import import_table
from gear import Gear
from view import MainView


class Controller:
    def __init__(self, root):
        self.root = root
        self.create_widgets()
        self.new_data()
        self.file_opt = options = {}
        options['defaultextension'] = '.json'
        options['filetypes'] = [('all files', '.json')]
        options['initialdir'] = './'
        options['initialfile'] = 'data.json'
        options['title'] = 'Choose a path'

    def create_widgets(self):
        self.root.title("Cycle Time Calculator")
        self.view = MainView(master=self.root)
        self.view.cycletime_tab.calcuate_button.config(command=self.handle_calcuation)

        self.view.file_menu.add_command(label = "New", command=self.new_data)
        self.view.file_menu.add_command(label = "Open", command=self.open_file)
        self.view.file_menu.add_command(label = "Save", command=self.save_file)
        self.view.file_menu.add_command(label = "Save As...", command=self.save_as)
        self.view.file_menu.add_command(label = "Import", command=self.import_data)
        self.view.file_menu.add_separator()
        self.view.file_menu.add_command(label = "Exit", command=self.root.quit)        
        self.root.config(menu=self.view.menubar)

    def new_data(self):
        try:
            del self.gear
            del self.file_path
        except AttributeError:
            pass
        self.gear = Gear()
        self.gear.addObserver(self.view.setData)
        self.gear.notify()
        self.view.statusbar.config(text = "Please input data.")

    def open_file(self):
        self.file_path = filedialog.askopenfilename(**self.file_opt)
        if self.file_path:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            self.gear.setData(data)
            self.view.statusbar.config(text = "File Loaded!")

    def save_file(self):
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

    def save_as(self):
        self.file_path = filedialog.asksaveasfilename(**self.file_opt)
        if self.file_path:
            with open(self.file_path, 'w') as f:
                data = self.gear.getData()
                json.dump(data, f, indent=4)

    def import_data(self):
        import_path = filedialog.askopenfilename()
        if import_path:
            f = open(import_path, 'r', encoding="big5")
            value = []
            for i in range(0,185,1):
                line = f.readline()
                j = line.find(',')
                value.append(line[j+1:].rstrip())
            f.close()
            data = import_table(value)
            self.new_data()
            self.gear.setData(data)
            self.view.statusbar.config(text = ".dat File Imported!")

    def handle_calcuation(self):
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
    app = Controller(root)
    root.mainloop()
