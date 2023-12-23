import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_value = so1.get()
    print(f"Selected currency: {selected_value}")

window = tk.Tk()
window.title("Expense Tracker")
window.minsize(width=1000, height=700)

lframe = tk.Frame(window, relief="raised")
lframe.grid(column=0, row=0, sticky="nsew")

so1 = tk.StringVar()
so2 = tk.StringVar()
so3 = tk.StringVar()

d1 = ttk.Combobox(lframe, textvariable=so1, values=["SAR", "EGP", "USD"])
d1.pack(pady=20)
d1.set("select")
d1.bind("<<ComboboxSelected>>", on_select)

l1 = tk.Label(lframe, text="Amount")
l1.grid(column=0, row=0, padx=1, pady=1, sticky="nsew")

l2 = tk.Label(lframe, text="Currency")
l2.grid(column=0, row=1, padx=1, pady=1, sticky="nsew")

l3 = tk.Label(lframe, text="Category")
l3.grid(column=0, row=2, padx=1, pady=1, sticky="nsew")

l4 = tk.Label(lframe, text="Payment Method")
l4.grid(column=0, row=3, padx=1, pady=1, sticky="nsew")

l5 = tk.Label(lframe, text="Date")
l5.grid(column=0, row=4, padx=1, pady=1, sticky="nsew")

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
lframe.columnconfigure(0, weight=1)
lframe.columnconfigure(1, weight=1)
lframe.rowconfigure(0, weight=1)
lframe.rowconfigure(1, weight=1)
lframe.rowconfigure(2, weight=1)
lframe.rowconfigure(3, weight=1)
lframe.rowconfigure(4, weight=1)

window.mainloop()
