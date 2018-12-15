import tkinter as tk
from tkinter import ttk
# import tkinter.ttk as ttk


class CycleTimePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.tabs = ttk.Notebook(self)
        self.create_widgets()

    def create_widgets(self):
        self.paned_window = ttk.Panedwindow(self, orient="vertical")
        self.paned_window.grid()

        # row 0: Labelframe - Grinding
        self.grind_frame = ttk.Labelframe(self.paned_window, text = "Grinding")
        self.grind_frame.grid(row=0, column=0)
        # Label 1
        self.label_1 = tk.Label(self.grind_frame, text = "I")
        self.label_1.grid(row=0, column=1)
        # Label 2
        self.label_2 = tk.Label(self.grind_frame, text = "II")
        self.label_2.grid(row=0, column=2)
        # Label 3
        self.label_3 = tk.Label(self.grind_frame, text = "III")
        self.label_3.grid(row=0, column=3)
        # Label 4
        self.label_4 = tk.Label(self.grind_frame, text = "IV")
        self.label_4.grid(row=0, column=4)

        # row 1: Passes
        # label 0
        self.grinding_pass_label = tk.Label(self.grind_frame, text = "                  Passes")
        self.grinding_pass_label.grid(row=1, column=0, sticky="e")
        # Entry 1
        #self.p1 = IntVar()
        self.grinding_pass_input_1 = tk.Entry(self.grind_frame, width=5)#, textvariable = self.p1)
        self.grinding_pass_input_1.grid(row=1, column=1)
        # Entry 2
        self.grinding_pass_input_2 = tk.Entry(self.grind_frame, width=5)
        self.grinding_pass_input_2.grid(row=1, column=2)
        # Entry 3
        self.grinding_pass_input_3 = tk.Entry(self.grind_frame, width=5)
        self.grinding_pass_input_3.grid(row=1, column=3)
        # Entry 4
        self.grinding_pass_input_4 = tk.Entry(self.grind_frame, width=5)
        self.grinding_pass_input_4.grid(row=1, column=4)

        # row 2: Feed-Forward
        # label 0
        self.feed_forward_label = tk.Label(self.grind_frame, text = "Feed-Forward")
        self.feed_forward_label.grid(row=2, column=0, sticky="e")
        # Entry 1
        self.feed_forward_input_1 = tk.Entry(self.grind_frame, width=5)
        self.feed_forward_input_1.grid(row=2, column=1)
        # Entry 2
        self.feed_forward_input_2 = tk.Entry(self.grind_frame, width=5)
        self.feed_forward_input_2.grid(row=2, column=2)
        # Entry 3
        self.feed_forward_input_3 = tk.Entry(self.grind_frame, width=5)
        self.feed_forward_input_3.grid(row=2, column=3)
        # Entry 4
        self.feed_forward_input_4 = tk.Entry(self.grind_frame, width=5)
        self.feed_forward_input_4.grid(row=2, column=4)

        # row 3: Feed-Backward
        # label 0
        self.feed_backward_label = tk.Label(self.grind_frame, text = "Feed-Backward")
        self.feed_backward_label.grid(row=3, column=0, sticky="e")
        # Entry 1
        self.feed_backward_input_1 = tk.Entry(self.grind_frame, width=5)
        self.feed_backward_input_1.grid(row=3, column=1)
        # Entry 2
        self.feed_backward_input_2 = tk.Entry(self.grind_frame, width=5)
        self.feed_backward_input_2.grid(row=3, column=2)
        # Entry 3
        self.feed_backward_input_3 = tk.Entry(self.grind_frame, width=5)
        self.feed_backward_input_3.grid(row=3, column=3)
        # Entry 4
        self.feed_backward_input_4 = tk.Entry(self.grind_frame, width=5)
        self.feed_backward_input_4.grid(row=3, column=4)

        # row 4: Infeed-Forward
        # label 0
        self.infeed_forward_label = tk.Label(self.grind_frame, text = "Infeed-Forward")
        self.infeed_forward_label.grid(row=4, column=0, sticky="e")
        # Entry 1
        self.infeed_forward_input_1 = tk.Entry(self.grind_frame, width=5)
        self.infeed_forward_input_1.grid(row=4, column=1)
        # Entry 2
        self.infeed_forward_input_2 = tk.Entry(self.grind_frame, width=5)
        self.infeed_forward_input_2.grid(row=4, column=2)
        # Entry 3
        self.infeed_forward_input_3 = tk.Entry(self.grind_frame, width=5)
        self.infeed_forward_input_3.grid(row=4, column=3)
        # Entry 4
        self.infeed_forward_input_4 = tk.Entry(self.grind_frame, width=5)
        self.infeed_forward_input_4.grid(row=4, column=4)

        # row 5 : Infeed-Backward
        # Label 0
        self.infeed_backward_label = tk.Label(self.grind_frame, text = "Infeed-Backward")
        self.infeed_backward_label.grid(row=5, column=0, sticky="e")
        # Entry 1
        self.infeed_backward_input_1 = tk.Entry(self.grind_frame, width=5)
        self.infeed_backward_input_1.grid(row=5, column=1)
        # Entry 2
        self.infeed_backward_input_2 = tk.Entry(self.grind_frame, width=5)
        self.infeed_backward_input_2.grid(row=5, column=2)
        # Entry 3
        self.infeed_backward_input_3 = tk.Entry(self.grind_frame, width=5)
        self.infeed_backward_input_3.grid(row=5, column=3)
        # Entry 4
        self.infeed_backward_input_4 = tk.Entry(self.grind_frame, width=5)
        self.infeed_backward_input_4.grid(row=5, column=4)

        # row 6 : Infeed-Total
        # Label 0
        self.infeed_total_label = tk.Label(self.grind_frame, text = "Infeed-Total")
        self.infeed_total_label.grid(row=6, column=0, sticky="e")
        # Entry 1
        self.infeed_total_output_1 = tk.Entry(self.grind_frame, width=5)
        self.infeed_total_output_1.grid(row=6, column=1)
        # Entry 2
        self.infeed_total_output_2 = tk.Entry(self.grind_frame, width=5)
        self.infeed_total_output_2.grid(row=6, column=2)
        # Entry 3
        self.infeed_total_output_3 = tk.Entry(self.grind_frame, width=5)
        self.infeed_total_output_3.grid(row=6, column=3)
        # Entry 4
        self.infeed_total_output_4 = tk.Entry(self.grind_frame, width=5)
        self.infeed_total_output_4.grid(row=6, column=4)

        # row 7: Plung Feed
        # Label 0
        self.plung_feed_label = tk.Label(self.grind_frame, text = "Plung Feed")
        self.plung_feed_label.grid(row=7, column=0, sticky="e")
        # Entry 1
        self.plung_feed_input_1 = tk.Entry(self.grind_frame, width=5)
        self.plung_feed_input_1.grid(row=7, column=1)
        # Entry 2
        self.plung_feed_input_2 = tk.Entry(self.grind_frame, width=5)
        self.plung_feed_input_2.grid(row=7, column=2)
        # Entry 3
        self.plung_feed_input_3 = tk.Entry(self.grind_frame, width=5)
        self.plung_feed_input_3.grid(row=7, column=3)
        # Entry 4
        self.plung_feed_input_4 = tk.Entry(self.grind_frame, width=5)
        self.plung_feed_input_4.grid(row=7, column=4)

        # Labelframe 1 - Dressing
        self.dress_frame = ttk.Labelframe(self.paned_window, text = "Dressing", \
                                          width=10000, height=10000)
        self.dress_frame.grid(row=1, column=0)

        # row 0: Dressing Passes
        # Label 0
        self.dresssing_pass_label = tk.Label(self.dress_frame, text = "                  Passes")
        self.dresssing_pass_label.grid(row=0, column=0, sticky="e")
        # Entry 1
        self.dresssing_pass_input_1 = tk.Entry(self.dress_frame, width=5)
        self.dresssing_pass_input_1.grid(row=0, column=1)
        # Entry 2
        self.dresssing_pass_input_2 = tk.Entry(self.dress_frame, width=5)
        self.dresssing_pass_input_2.grid(row=0, column=2)
        # Entry 3
        self.dresssing_pass_input_3 = tk.Entry(self.dress_frame, width=5)
        self.dresssing_pass_input_3.grid(row=0, column=3)
        # Entry 4
        self.dresssing_pass_input_4 = tk.Entry(self.dress_frame, width=5)
        self.dresssing_pass_input_4.grid(row=0, column=4)

        # row 1: Dressing Infeed
        # Label 0
        self.dressing_infeed_label = tk.Label(self.dress_frame, text = "InFeed")
        self.dressing_infeed_label.grid(row=1, column=0, sticky="e")
        # Entry 1
        self.dresssing_infeed_input_1 = tk.Entry(self.dress_frame, width=5)
        self.dresssing_infeed_input_1.grid(row=1, column=1)
        # Entry 2
        self.dresssing_infeed_input_2 = tk.Entry(self.dress_frame, width=5)
        self.dresssing_infeed_input_2.grid(row=1, column=2)
        # Entry 3
        self.dresssing_infeed_input_3 = tk.Entry(self.dress_frame, width=5)
        self.dresssing_infeed_input_3.grid(row=1, column=3)
        # Entry 4
        self.dresssing_infeed_input_4 = tk.Entry(self.dress_frame, width=5)
        self.dresssing_infeed_input_4.grid(row=1, column=4)

        # row 2: Dressing Feed
        # label 0
        self.dressingFeedLabel = tk.Label(self.dress_frame, text = "Feed")
        self.dressingFeedLabel.grid(row=2, column=0, sticky="e")
        # Entry 1
        self.dressingFeedInput_1 = tk.Entry(self.dress_frame, width=5)
        self.dressingFeedInput_1.grid(row=2, column=1)
        # Entry 2
        self.dressingFeedInput_2 = tk.Entry(self.dress_frame, width=5)
        self.dressingFeedInput_2.grid(row=2, column=2)
        # Entry 3
        self.dressingFeedInput_3 = tk.Entry(self.dress_frame, width=5)
        self.dressingFeedInput_3.grid(row=2, column=3)
        # Entry 4
        self.dressingFeedInput_4 = tk.Entry(self.dress_frame, width=5)
        self.dressingFeedInput_4.grid(row=2, column=4)

        # raw 3: Dressing Frquency
        # label 0
        self.dressing_frquency_Label = tk.Label(self.dress_frame, text = "Dressing Frq.")
        self.dressing_frquency_Label.grid(row=3, column=0, sticky="e")

        # row 4: [drop down]
        # Label 0
        self.dressing_frquency_Label = tk.Label(self.dress_frame, text = "[By Passes]")
        self.dressing_frquency_Label.grid(row=4, column=0, sticky="e")
        # Entry 1
        self.dressing_frquency_input_1 = tk.Entry(self.dress_frame, width=5)
        self.dressing_frquency_input_1.grid(row=4, column=1)
        # Entry 2
        self.dressing_frquency_input_2 = tk.Entry(self.dress_frame, width=5)
        self.dressing_frquency_input_2.grid(row=4, column=2)
        # Entry 3
        self.dressing_frquency_input_3 = tk.Entry(self.dress_frame, width=5)
        self.dressing_frquency_input_3.grid(row=4, column=3)
        # Entry 4
        self.dressing_frquency_input_4 = tk.Entry(self.dress_frame, width=5)
        self.dressing_frquency_input_4.grid(row=4, column=4)

        # Labelframe 2 - Cycle Time
        self.result_frame = ttk.Labelframe(self.paned_window, text = " Cycle Time (h:m:s)")
        self.result_frame.grid(row=2, column=0)
        # row 0
        # label 0
        self.dressing_label_1 = tk.Label(self.result_frame, text = "I")
        self.dressing_label_1.grid(row=0, column=1)
        # label 0
        self.dressing_label_2 = tk.Label(self.result_frame, text = "II")
        self.dressing_label_2.grid(row=0, column=2)
        # label 0
        self.dressing_label_3 = tk.Label(self.result_frame, text = "III")
        self.dressing_label_3.grid(row=0, column=3)
        # label 0
        self.dressing_label_4 = tk.Label(self.result_frame, text = "IV")
        self.dressing_label_4.grid(row=0, column=4)

        # row 1: set dressing time
        # label 0
        self.dressing_time_label = tk.Label(self.result_frame, text = "Set Dressing Time")
        self.dressing_time_label.grid(row=1, column=0, sticky="e")
        # Entry 1
        self.dressing_time_output_1 = tk.Entry(self.result_frame, width=5)
        self.dressing_time_output_1.grid(row=1, column=1)
        # Entry 2
        self.dressing_time_output_2 = tk.Entry(self.result_frame, width=5)
        self.dressing_time_output_2.grid(row=1, column=2)
        # Entry 3
        self.dressing_time_output_3 = tk.Entry(self.result_frame, width=5)
        self.dressing_time_output_3.grid(row=1, column=3)
        # Entry 4
        self.dressing_time_output_4 = tk.Entry(self.result_frame, width=5)
        self.dressing_time_output_4.grid(row=1, column=4)

        # row 2: Set Cycle time (sec.)
        # label 0
        self.cycle_time_set_label = tk.Label(self.result_frame, text = "Set Cycle Time")
        self.cycle_time_set_label.grid(row=2, column=0, sticky="e")
        # Entry 1
        self.cycle_time_set_output_1 = tk.Entry(self.result_frame, width=5)
        self.cycle_time_set_output_1.grid(row=2, column=1)
        # Entry 2
        self.cycle_time_set_output_2 = tk.Entry(self.result_frame, width=5)
        self.cycle_time_set_output_2.grid(row=2, column=2)
        # Entry 3
        self.cycle_time_set_output_3 = tk.Entry(self.result_frame, width=5)
        self.cycle_time_set_output_3.grid(row=2, column=3)
        # Entry 4
        self.cycle_time_set_output_4 = tk.Entry(self.result_frame, width=5)
        self.cycle_time_set_output_4.grid(row=2, column=4)

        # raw 3: Total Cycle time (sec.)
        # label 0
        self.cycle_time_total_label = tk.Label(self.result_frame, text = "Total Cycle time")
        self.cycle_time_total_label.grid(row=3, column=0, sticky="e")
        # Entry 1
        self.cycle_time_total_output = tk.Entry(self.result_frame, width = "11")
        self.cycle_time_total_output.grid(row=3, column=1, columnspan=2)
        # Button - Calcuate
        self.calcuate_button = tk.Button(self.result_frame, width=8, text = "Calcuate")
        self.calcuate_button.grid(row=3, column=3, columnspan=2)

        # Place paned windows
        self.paned_window.add(self.grind_frame)
        self.paned_window.add(self.dress_frame)
        self.paned_window.add(self.result_frame)


    def getData(self):
        data = [{}, {}, {}, {}]
        data[0]["passes"] = int(self.grinding_pass_input_1.get())
        data[0]["feedForw"] = float(self.feed_forward_input_1.get())
        data[0]["feedBack"] = float(self.feed_backward_input_1.get())
        data[0]["infeedForw"] = float(self.infeed_forward_input_1.get())
        data[0]["infeedBack"] = float(self.infeed_backward_input_1.get())
        data[0]["plunge"] = float(self.plung_feed_input_1.get())
        data[0]["dressPass"] = int(self.dresssing_pass_input_1.get())
        data[0]["dressInfeed"] = float(self.dresssing_infeed_input_1.get())
        data[0]["dressFeed"] = float(self.dressingFeedInput_1.get())
        data[0]["dressFrq"] =  int(self.dressing_frquency_input_1.get())

        data[1]["passes"] = int(self.grinding_pass_input_2.get())
        data[1]["feedForw"] = float(self.feed_forward_input_2.get())
        data[1]["feedBack"] = float(self.feed_backward_input_2.get())
        data[1]["infeedForw"] = float(self.infeed_forward_input_2.get())
        data[1]["infeedBack"] = float(self.infeed_backward_input_2.get())
        data[1]["plunge"] = float(self.plung_feed_input_2.get())
        data[1]["dressPass"] = int(self.dresssing_pass_input_2.get())
        data[1]["dressInfeed"] = float(self.dresssing_infeed_input_2.get())
        data[1]["dressFeed"] = float(self.dressingFeedInput_2.get())
        data[1]["dressFrq"] =  int(self.dressing_frquency_input_2.get())

        data[2]["passes"] = int(self.grinding_pass_input_3.get())
        data[2]["feedForw"] = float(self.feed_forward_input_3.get())
        data[2]["feedBack"] = float(self.feed_backward_input_3.get())
        data[2]["infeedForw"] = float(self.infeed_forward_input_3.get())
        data[2]["infeedBack"] = float(self.infeed_backward_input_3.get())
        data[2]["plunge"] = float(self.plung_feed_input_3.get())
        data[2]["dressPass"] = int(self.dresssing_pass_input_3.get())
        data[2]["dressInfeed"] = float(self.dresssing_infeed_input_3.get())
        data[2]["dressFeed"] = float(self.dressingFeedInput_3.get())
        data[2]["dressFrq"] =  int(self.dressing_frquency_input_3.get())

        data[3]["passes"] = int(self.grinding_pass_input_4.get())
        data[3]["feedForw"] = float(self.feed_forward_input_4.get())
        data[3]["feedBack"] = float(self.feed_backward_input_4.get())
        data[3]["infeedForw"] = float(self.infeed_forward_input_4.get())
        data[3]["infeedBack"] = float(self.infeed_backward_input_4.get())
        data[3]["plunge"] = float(self.plung_feed_input_4.get())
        data[3]["dressPass"] = int(self.dresssing_pass_input_4.get())
        data[3]["dressInfeed"] = float(self.dresssing_infeed_input_4.get())
        data[3]["dressFeed"] = float(self.dressingFeedInput_4.get())
        data[3]["dressFrq"] =  int(self.dressing_frquency_input_4.get())

        return data

    def setData(self, data):
        self.grinding_pass_input_1.delete(0, 'end')
        self.grinding_pass_input_1.insert('end', str(data["machining"][0]["passes"]))
        self.feed_forward_input_1.delete(0, 'end')
        self.feed_forward_input_1.insert('end', str(data["machining"][0]["feedForw"]))
        self.feed_backward_input_1.delete(0, 'end')
        self.feed_backward_input_1.insert('end', str(data["machining"][0]["feedBack"]))
        self.infeed_forward_input_1.delete(0, 'end')
        self.infeed_forward_input_1.insert('end', str(data["machining"][0]["infeedForw"]))
        self.infeed_backward_input_1.delete(0, 'end')
        self.infeed_backward_input_1.insert('end', str(data["machining"][0]["infeedBack"]))
        self.plung_feed_input_1.delete(0, 'end')
        self.plung_feed_input_1.insert('end', str(data["machining"][0]["plunge"]))
        self.dresssing_pass_input_1.delete(0, 'end')
        self.dresssing_pass_input_1.insert('end', str(data["machining"][0]["dressPass"]))
        self.dresssing_infeed_input_1.delete(0, 'end')
        self.dresssing_infeed_input_1.insert('end', str(data["machining"][0]["dressInfeed"]))
        self.dressingFeedInput_1.delete(0, 'end')
        self.dressingFeedInput_1.insert('end', str(data["machining"][0]["dressFeed"]))
        self.dressing_frquency_input_1.delete(0, 'end')
        self.dressing_frquency_input_1.insert('end', str(data["machining"][0]["dressFrq"]))

        self.grinding_pass_input_2.delete(0, 'end')
        self.grinding_pass_input_2.insert('end', str(data["machining"][1]["passes"]))
        self.feed_forward_input_2.delete(0, 'end')
        self.feed_forward_input_2.insert('end', str(data["machining"][1]["feedForw"]))
        self.feed_backward_input_2.delete(0, 'end')
        self.feed_backward_input_2.insert('end', str(data["machining"][1]["feedBack"]))
        self.infeed_forward_input_2.delete(0, 'end')
        self.infeed_forward_input_2.insert('end', str(data["machining"][1]["infeedForw"]))
        self.infeed_backward_input_2.delete(0, 'end')
        self.infeed_backward_input_2.insert('end', str(data["machining"][1]["infeedBack"]))
        self.plung_feed_input_2.delete(0, 'end')
        self.plung_feed_input_2.insert('end', str(data["machining"][1]["plunge"]))
        self.dresssing_pass_input_2.delete(0, 'end')
        self.dresssing_pass_input_2.insert('end', str(data["machining"][1]["dressPass"]))
        self.dresssing_infeed_input_2.delete(0, 'end')
        self.dresssing_infeed_input_2.insert('end', str(data["machining"][1]["dressInfeed"]))
        self.dressingFeedInput_2.delete(0, 'end')
        self.dressingFeedInput_2.insert('end', str(data["machining"][1]["dressFeed"]))
        self.dressing_frquency_input_2.delete(0, 'end')
        self.dressing_frquency_input_2.insert('end', str(data["machining"][1]["dressFrq"]))

        self.grinding_pass_input_3.delete(0, 'end')
        self.grinding_pass_input_3.insert('end', str(data["machining"][2]["passes"]))
        self.feed_forward_input_3.delete(0, 'end')
        self.feed_forward_input_3.insert('end', str(data["machining"][2]["feedForw"]))
        self.feed_backward_input_3.delete(0, 'end')
        self.feed_backward_input_3.insert('end', str(data["machining"][2]["feedBack"]))
        self.infeed_forward_input_3.delete(0, 'end')
        self.infeed_forward_input_3.insert('end', str(data["machining"][2]["infeedForw"]))
        self.infeed_backward_input_3.delete(0, 'end')
        self.infeed_backward_input_3.insert('end', str(data["machining"][2]["infeedBack"]))
        self.plung_feed_input_3.delete(0, 'end')
        self.plung_feed_input_3.insert('end', str(data["machining"][2]["plunge"]))
        self.dresssing_pass_input_3.delete(0, 'end')
        self.dresssing_pass_input_3.insert('end', str(data["machining"][2]["dressPass"]))
        self.dresssing_infeed_input_3.delete(0, 'end')
        self.dresssing_infeed_input_3.insert('end', str(data["machining"][2]["dressInfeed"]))
        self.dressingFeedInput_3.delete(0, 'end')
        self.dressingFeedInput_3.insert('end', str(data["machining"][2]["dressFeed"]))
        self.dressing_frquency_input_3.delete(0, 'end')
        self.dressing_frquency_input_3.insert('end', str(data["machining"][2]["dressFrq"]))

        self.grinding_pass_input_4.delete(0, 'end')
        self.grinding_pass_input_4.insert('end', str(data["machining"][3]["passes"]))
        self.feed_forward_input_4.delete(0, 'end')
        self.feed_forward_input_4.insert('end', str(data["machining"][3]["feedForw"]))
        self.feed_backward_input_4.delete(0, 'end')
        self.feed_backward_input_4.insert('end', str(data["machining"][3]["feedBack"]))
        self.infeed_forward_input_4.delete(0, 'end')
        self.infeed_forward_input_4.insert('end', str(data["machining"][3]["infeedForw"]))
        self.infeed_backward_input_4.delete(0, 'end')
        self.infeed_backward_input_4.insert('end', str(data["machining"][3]["infeedBack"]))
        self.plung_feed_input_4.delete(0, 'end')
        self.plung_feed_input_4.insert('end', str(data["machining"][3]["plunge"]))
        self.dresssing_pass_input_4.delete(0, 'end')
        self.dresssing_pass_input_4.insert('end', str(data["machining"][3]["dressPass"]))
        self.dresssing_infeed_input_4.delete(0, 'end')
        self.dresssing_infeed_input_4.insert('end', str(data["machining"][3]["dressInfeed"]))
        self.dressingFeedInput_4.delete(0, 'end')
        self.dressingFeedInput_4.insert('end', str(data["machining"][3]["dressFeed"]))
        self.dressing_frquency_input_4.delete(0, 'end')
        self.dressing_frquency_input_4.insert('end', str(data["machining"][3]["dressFrq"]))

        self.dressing_time_output_1.delete(0, 'end')
        self.dressing_time_output_2.delete(0, 'end')
        self.dressing_time_output_3.delete(0, 'end')
        self.dressing_time_output_4.delete(0, 'end')
        self.cycle_time_set_output_1.delete(0, 'end')
        self.cycle_time_set_output_2.delete(0, 'end')
        self.cycle_time_set_output_3.delete(0, 'end')
        self.cycle_time_set_output_4.delete(0, 'end')
        self.cycle_time_total_output.delete(0, 'end')

    def set_result(self, data):
        self.dressing_time_output_1.delete(0, 'end')
        self.dressing_time_output_2.delete(0, 'end')
        self.dressing_time_output_3.delete(0, 'end')
        self.dressing_time_output_4.delete(0, 'end')
        self.cycle_time_set_output_1.delete(0, 'end')
        self.cycle_time_set_output_2.delete(0, 'end')
        self.cycle_time_set_output_3.delete(0, 'end')
        self.cycle_time_set_output_4.delete(0, 'end')
        self.cycle_time_total_output.delete(0, 'end')

        self.dressing_time_output_1.insert('end', self.time_form(int(data['dressTime_1'])))
        self.cycle_time_set_output_1.insert('end', self.time_form(int(data['grindTime_1'])))
        self.dressing_time_output_2.insert('end', self.time_form(int(data['dressTime_2'])))
        self.cycle_time_set_output_2.insert('end', self.time_form(int(data['grindTime_2'])))
        self.dressing_time_output_3.insert('end', self.time_form(int(data['dressTime_3'])))
        self.cycle_time_set_output_3.insert('end', self.time_form(int(data['grindTime_3'])))
        self.dressing_time_output_4.insert('end', self.time_form(int(data['dressTime_4'])))
        self.cycle_time_set_output_4.insert('end', self.time_form(int(data['grindTime_4'])))
        self.cycle_time_total_output.insert('end', self.time_form(int(data['cycleTime'])))

    def time_form(self, sec):
        (hr, mi) = divmod(sec, 360)
        (mi, sec) = divmod(mi, 60)
        return str(hr) + ':' + str(mi) + ':' + str(sec)