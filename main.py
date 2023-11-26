import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import pandas as pd
import numpy as np
import urllib
import json

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 18)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '87a3588f-647b-4b1d-bd0f-a85fb1d80c0e',
    }

    json = requests.get(url, params=parameters, headers=headers).json()
    coins = json["data"]
    for x in coins:
        if x['symbol'] == 'BTC':
            x['quote']['USD']['price']
            print(x['symbol'], x['quote']['USD']['price'])

    a.clear()
    a.plot(xList, yList)
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Data of the Day")
        tk.Tk.wm_iconbitmap(self, default="01_logobachkhoatoi2.ico")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, BTCe_page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def qf(param):
    print(param)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="""ALPHA BTC trading use at your warranty""", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Agree",
                            command=lambda: controller.show_frame(BTCe_page))
        button.pack()

        button2 = ttk.Button(self, text="DisAgree",
                            command=quit)
        button2.pack()



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       label = ttk.Label(self, text="Page One!!", font=LARGE_FONT)
       label.pack(pady=10, padx=10)

       button1 = ttk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame(StartPage))
       button1.pack()

       button2 = ttk.Button(self, text="Visit Page 2",
                           command=lambda: controller.show_frame(BTCe_page))
       button2.pack()


class BTCe_page(tk.Frame):
    def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       label = ttk.Label(self, text="Graph Page", font=LARGE_FONT)
       label.pack(pady=10, padx=10)

       button1 = ttk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame(StartPage))
       button1.pack()

       canvas = FigureCanvasTkAgg(f, self)
       canvas
       canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH, expand=True)

       toolbar = NavigationToolbar2Tk(canvas, self)
       toolbar.update()
       canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=5000)
app.mainloop()
