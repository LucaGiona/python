import tkinter as tk
from tkinter import ttk

def add_task():
    if task.get() != "":
        task_treeview.insert(parent="", index="end", values=(task.get().replace(" ", "\ ")))
        #replace weil sonst nur das erste Wort gespeichert wird
        task_entry.delete(0, tk.END)
        #entry automatisch löschen

    else:
        print("Bitte einen Task eingeben!")

def remove_task():
    selected_item = task_treeview.selection()
    if selected_item != ():
        # if selected item != leeres tuple
        task_treeview.delete(selected_item)
    else:
        print("Bitte einen Task markieren!")

root = tk.Tk()
root.title("ToDo_List")

root.geometry("688x390")
root.columnconfigure(0, weight=1)

task = tk.StringVar()

style = ttk.Style()
style.theme_use("clam")

#Frames
user_input_frame = ttk.Frame(root)
user_input_frame.grid(row=0, column=0, pady=20)
task_frame = ttk.Frame(root)
task_frame.grid(row=1, column=0, pady=10)

#Widgets user_input_frame
task_label = ttk.Label(user_input_frame, text="Task: ")
task_label.grid(row=0, column=0)
task_entry = ttk.Entry(user_input_frame, width=60, textvariable=task)
task_entry.grid(row=0, column=1)

add_task_button = ttk.Button(user_input_frame, text="Task hinzufügen", command=add_task)
add_task_button.grid(row=1, column=0, columnspan=2, sticky="ew", pady=2)

# Widgets task frame
task_treeview = ttk.Treeview(task_frame, selectmode="browse")
task_treeview.grid(sticky="ew", row=0, column=0)

#Spalten definieren und konfigurieren
task_treeview.configure(columns=("task"))
task_treeview.column("#0", width=0, stretch=tk.NO)
task_treeview.heading("task", text="Tasks")
task_treeview.column("task", width=575)

#scrollbar für treeview Widget erzeugen und an task_treeview knüpfen
task_treeview_scroll= ttk.Scrollbar(task_frame, orient="vertical", command=task_treeview.yview)
task_treeview_scroll.grid(row=0, column=1, sticky="ns")
task_treeview.configure(yscrollcommand=task_treeview_scroll.set)

delete_task_button = ttk.Button(task_frame, text="markierten Task entfernen",
                                command=remove_task)
delete_task_button.grid(row=1, column=0, columnspan=2, sticky="ew")


root.mainloop()