from tkinter import Tk, StringVar,ttk
from tkinter import *


import requests

import itertools
HEIGHT = 400
WIDTH = 600

root = Tk()
API_KEY = "e3bec228073897d42c9052c6f274349e"              # THIS IS THE API KEY BY CURRENCY FIXER
URL = "http://data.fixer.io/api/latest"                        # THE IS THE URL TAKEN FROM CURRENCY FIXER
currency = "EUR"                                            # THE BASE CURRENCY IS EURO ONLY, BECAUSE THE SYSTEM DOES NOT GIVE US ACCESS TO FULL PREMIUM VERSION TO
                                                             # USE ALL CURRENCY AS A BASE CURRENCY
PARAM = {"access_key": "e3bec228073897d42c9052c6f274349e", "base": currency}      # THIS HOLDS THE PREVIOUSLY DEFINED VARIABLES IN THE FORM OF DICTIONARY
RESPONSE = requests.get(URL, params=PARAM)               # USING REQUEST MODULE TO FETCH THE DATA FROM THE SERVER
JSON_FORM = RESPONSE.json()                             #  CONVERTS OUR FETCHED DATA INTO JSON
convert_to_chunk = JSON_FORM['rates']        #
variable = StringVar(root)                        # the variable string used later in the frame
variable.set('Currency')

chunkform = dict(itertools.islice(convert_to_chunk.items(), 7))       #  THE DATA IS VERY HUGE, SO this takes only some part of the data






class CurrencyConverter():

    def __init__(self,master):
        """

        :param master: this is the root window taken as a parameter
        """

        self.master = master



        self.master.title("currency exchange")           # this is the title of the window
        self.canvas = Canvas(self.master,height=HEIGHT, width=WIDTH)     # canvas for drawing our frames and shapes
        self.canvas.pack()       # it packs our canvas on the root window


        # This is the images and the header section of our tkinter

        frame = Frame(self.master, bg = '#009999',bd = 5,relief = FLAT)
        frame.place(relx = 0.03,rely = 0.03,relwidth = 0.94, relheight = 0.94)
        title = Label(self.master, text = "Currency",font = "Mothius 30 bold italic",bg = '#009999',bd = 5)
        title.place(relx = 0.04, rely = 0.1,relwidth = 0.3, relheight = 0.2)
        self.introImage = PhotoImage(file = "images/money (2).png")
        self.logoImage = Label(image = self.introImage)
        self.logoImage.place(relx = 0.4,rely = 0.1)
        titlePart = Label(self.master, text = "Exchange",font = "Mothius 30 bold italic",bg = '#ffccff',bd = 5)
        titlePart.place(relx=0.66, rely=0.1, relwidth=0.3, relheight=0.2)



        # frame for putting the choose country
        framethree = Frame(self.master, bg = "#a539ff")
        framethree.place(relx = 0.10, rely = 0.45,relwidth = 0.20,relheight = 0.10)

        # label text
        label = Label(framethree, text = "choose currency:", font = ("arial",9, "bold"),fg = "black")
        label.place(relx = 0.06, rely = 0.25)


        #frame for label

        framefour = Frame(self.master, bg="#a539ff")
        framefour.place(relx=0.10, rely=0.60, relwidth=0.20, relheight=0.10)

        # label text
        label = Label(framefour, text="Enter euro amount:", font=("arial", 9, "bold"), fg="black")
        label.place(relx=0.06, rely=0.25)

        # optionmenu

        currency_frame = Frame(self.master, bg='#a539ff', bd=5)
        currency_frame.place(relx=0.35, rely=0.45, relwidth=0.30, relheight=0.10)
        currency_menu = OptionMenu(currency_frame, variable, *chunkform)
        currency_menu.place(relwidth = 0.99)



        # button portion


        button = Button(self.master,text = 'convert',fg ='blue',font = ('calibri',20),bg = 'powder blue',command = self.currency_conversion_mechanism)
        button.place(relx = 0.65,rely = 0.60,relwidth = 0.20,relheight = 0.10)

        # entry portion
        entry_frame = Frame(self.master, bg='#a539ff', bd=5)
        entry_frame.place(relx=0.35, rely=0.60, relwidth=0.30, relheight=0.10)
        self.entries = Entry(entry_frame, font=50,bd = 5)
        self.entries.place(relwidth=0.99, relheight=0.95)




        # text box

        self.result = Text(self.master, height=5, width=50, font=("arial", 10, "bold"), bd=5)
        self.result.place(relx=0.20, rely=0.75)

    def currency_conversion_mechanism(self):
        """

        :return: None
        """


        try:

            entry_input = self.entries.get()                # this gives us the entry box input

            answer = variable.get()               # this gets us the currency we select in the optionmenu
            print(answer)
            DICT = chunkform.get(answer,None)       # this gives us the value of the currency key which is stored in the chunkform dictionary
            print(DICT)
            converted = float(DICT) * float(entry_input)           # this converts the value of the key into float and the entryinput into float

            self.result.delete(1.0, END)
            self.result.insert(INSERT, "The converted currency in: ", INSERT, answer, INSERT, "=", INSERT, converted)
        except:


            self.result.insert(INSERT, "enter a valid currency")



application = CurrencyConverter(root)
root.mainloop()

