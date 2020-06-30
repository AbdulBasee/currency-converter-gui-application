import tkinter as tk
from tkinter import *
import tkinter.messagebox

root = tk.Tk()

root.title("GUI : Currency Conversion")

Tops = Frame(root, bg='#663300', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='      Pypower Project   :    Currency Converter  ',
                     bg='#663300', fg='white')
headlabel.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("currency")
variable2.set("currency")
m = DoubleVar()
entry_frame = tk.Frame(root, bg='#a539ff', bd=5)
entry_frame.place(relx=0.35, rely=0.60, relwidth=0.30, relheight=0.10)
entries = tk.Entry(entry_frame,textvariable= m, font=50)
entries.place(relwidth=0.65, relheight=0.95)

somtdict = {"IND": 23.45, "USD": 34.23, "EUR": 89.2, "PKR": 34.21}
def some():
    y = float(entries.get())
    print(y)


    variable.set("currency")
    answer = variable.get()
    variable2 = DoubleVar()

    DICT = somtdict.get(answer, None)
    print(DICT)




variable = StringVar(root)
variable.set(None)


root.mainloop()