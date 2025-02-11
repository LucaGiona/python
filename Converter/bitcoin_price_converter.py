import tkinter as tk
from tkinter import ttk
from tkinter import font
import requests


def calculate_price():
    try:
        response = requests.get(COINDESK_API_URL)
        respone_dict= response.json()
        #print(type(response))
        #print((respone_dict))
        current_bitcoin_price_euro = respone_dict["bitcoin"]["eur"]
        #print(current_bitcoin_price_euro)

        calculate_price_euro=float(bitcoin_entry.get()) * current_bitcoin_price_euro
        print(calculate_price_euro)
        euro_value.set("{:.2f}".format(calculate_price_euro))


    except ValueError:
        print("Bitte einen gültigen Zahlenwert eingeben!")

style_var = {"side": "top", "fill": "x", "padx": 5, "pady": 2}

root = tk.Tk()
#print(font.families())
root.geometry("400x250+550+150")
root.title("Bitcoin Price Calculator")

COINDESK_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur"
euro_value= tk.StringVar(value="Hier wird der Preis in € angezeigt: ")

bitcoin_label = ttk.Label(root, text="Anzahl Bitcoin: ", font=('Andale Mono', 16))
bitcoin_label.pack(**style_var)

bitcoin_entry = ttk.Entry(root, font=("Arial", 15))
bitcoin_entry.pack(side="top", fill="x", padx= 5, pady=2)

euro_label = ttk.Label(root, text="Preis in Euro: ", font=('Andale Mono', 16) )
euro_label.pack(side="top", fill="x", padx= 5, pady=2)

euro_display = ttk.Label(root, textvariable=euro_value, font="Arial")
euro_display.pack(**style_var)

calculate_button = ttk.Button(root, text="Berechnung durchführen", command=calculate_price)
calculate_button.pack(side="bottom", fill="x", padx=10, pady=10)



root.mainloop()