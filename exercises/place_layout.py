import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.geometry("500x500+250+200")

style = ttk.Style()
style.theme_use("clam")

button = ttk.Button(root, text="Das ist ein Button!")
button.place(x=40, y=100)

#width and height
button1 = ttk.Button(root, text="Ein anderer Button")
button1.place(x=30, y= 120, width=200, height=300) #height nicht angezeigt wegen themes

#relative vs. absolute Positionierung

button2 = ttk.Button(root, text="Und noch ein Button")
button2.place(relx=0.5, rely=0.6, relwidth=0.5)


root.mainloop()
