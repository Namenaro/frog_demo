import os
from pprint import pprint
import tkinter as tk

class MainScreen(tk.Frame):
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack()
        self.parent = parent

        folder = "frog_muskle"
        self.image_0 = tk.PhotoImage(file=os.path.join(folder, "zero_freq.png"))
        self.image_1 = tk.PhotoImage(file=os.path.join(folder, "one_freq.png"))
        self.image_27 = tk.PhotoImage(file=os.path.join(folder, "two_7_freq.png"))
        self.image_8 = tk.PhotoImage(file=os.path.join(folder, "tetanus.png"))
        self.pic_freq = {0: self.image_0,
                    1: self.image_1,
                    2: self.image_27,
                    3: self.image_27,
                    4: self.image_27,
                    5: self.image_27,
                    6: self.image_27,
                    7: self.image_27,
                    8: self.image_8}

        self.panel_frame = tk.Frame(self.frame)
        self.panel_frame.grid(row=0, column=0, padx=25, pady=25)


        # статическая подпись про герцы
        self.freq_static_var = tk.StringVar()
        self.freq_static_label = tk.Label(self.panel_frame, textvariable=self.freq_static_var, relief=tk.RAISED)
        self.freq_static_var.set(" Гц ")
        self.freq_static_label.grid(row=0, column=2, padx=5)

        # статическая подпись про милливольты
        self.voltage_static_var = tk.StringVar()
        self.voltage_static_label = tk.Label(self.panel_frame, textvariable=self.voltage_static_var, relief=tk.RAISED)
        self.voltage_static_var.set(" мВ ")
        self.voltage_static_label.grid(row=3, column=2, padx=5)

        # поле ввода про милливольты
        self.voltage_var = tk.StringVar()
        self.voltage_var.set("1.5")
        self.voltage_entry = tk.Entry(self.panel_frame, width=4, state=tk.DISABLED, textvariable=self.voltage_var)
        self.voltage_entry.grid(row=3, column=1, padx=5)

        # статическая картинка лягушки
        frog_pic = os.path.join(folder, "frog.png")
        self.frog_img = tk.PhotoImage(file=frog_pic)
        self.label_frog = tk.Label(self.frame, image=self.frog_img, relief=tk.RAISED)
        self.label_frog.grid(row=0, column=2, padx=25, pady=25)

        # меняющаяся картика с графиком
        self.label_graph = tk.Label(self.frame, image=self.pic_freq[0], relief=tk.RAISED)
        self.label_graph.grid(row=0, column=1, padx=25, pady=25)

        # ползунок
        self.freq_var = tk.IntVar()
        self.scale = tk.Scale(self.panel_frame, variable=self.freq_var, to=8, showvalue=False, command=self.slider_moved)
        self.scale.grid(row=0, column=0, rowspan=4,
               sticky=tk.W, padx=5)

        # поле ввода про герцы
        self.freq_entry = tk.Entry(self.panel_frame, width=4, textvariable=self.freq_var)
        self.freq_entry.grid(row=0, column=1, padx=5)

    def slider_moved(self,value_slider):
        # сменим картинку
        self.label_graph.configure(image=self.pic_freq[int(value_slider)])
        self.label_graph.image = self.pic_freq[int(value_slider)]

def main():
    root = tk.Tk()
    app = MainScreen(root)
    app.parent.title("Лягушка - демо")
    root.mainloop()

if __name__ == '__main__':
    main()

