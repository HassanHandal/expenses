import requests
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from api import api
amount_list = []
currency_list = []
category_list = []
payment_list = []
date_list = []
def show_error_message(message):
    error_label.config(text=message)

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
def not_select(text):
    return text != "select"

def add_expense():
    t1 = t.get()
    t2 = so1.get()
    t3 = so2.get()
    t4 = so3.get()
    t5 = dt.get()
    if is_integer(t1) and int(t1) > 0  and t1!="" and not_select(t2) and not_select(t3) and not_select(t4):
        if error_label.cget("text") != "":
            error_label.config(text="")
        if amount_list:
            amount_list.pop()
        if currency_list:
            currency_list.pop()
        amount_list.append(t1)
        currency_list.append(t2)
        category_list.append(t3)
        payment_list.append(t4)
        date_list.append(t5)
        total_amount = 0
        for b in range(len(amount_list)):
            from_curr = currency_list[b]
            to_curr = "USD"
            amount = amount_list[b]
            url = f"https://api.apilayer.com/fixer/convert?to={to_curr}&from={from_curr}&amount={amount}"

            headers = {
                "apikey": api()
            }

            response = requests.get(url, headers=headers)

            status_code = response.status_code
            result = response.json()
            total_amount += round(float(result["result"]),2)
        amount_list.append(round(float(total_amount),2))
        currency_list.append("USD")
        for item in tree.get_children():
            tree.delete(item)
        for i in range(len(payment_list)):
            tree.insert("", "end", values=(amount_list[i], currency_list[i], category_list[i], payment_list[i], date_list[i]))
        tag_name = f"tag{len(amount_list)}"
        tree.insert("", "end", values=(amount_list[len(amount_list)-1], currency_list[len(amount_list)-1]),tags=tag_name)
        tree.tag_configure(tag_name, background="yellow",font=('TkDefaultFont', 9, 'bold'))
    else:
        show_error_message("Invalid input. Please check your entries.")

    
  

        
































window = tk.Tk()
window.title("Expense Tracker")
window.minsize(width=1000,height=700)
lframe = tk.Frame(window,relief="raised")
lframe.grid(column=0,row=0,sticky="nsew")

so1=tk.StringVar()
d1=ttk.Combobox(lframe,textvariable=so1,values=["SAR","EGP","USD"],state="readonly",width=40,justify="center")
d1.grid(column=1,row=1,padx=1,pady=10)
d1.set("select")

so2=tk.StringVar()
d2=ttk.Combobox(lframe,textvariable=so2,values=["SuperMarket","Apartment Expenses","Gam3ya","Car rent","Installments","Others"],state="readonly",width=40,justify="center")
d2.grid(column=1,row=2,padx=1,pady=10)
d2.set("select")

so3=tk.StringVar()
d3=ttk.Combobox(lframe,textvariable=so3,values=["Cash","Hassan Visa","Credit","Menna Visa"],state="readonly",width=40,justify="center")
d3.grid(column=1,row=3,padx=1,pady=10)
d3.set("select")

l1 = tk.Label(lframe,text="Amount")
l1.grid(column=0,row=0,padx=1,pady=1,sticky="nsew")
t=tk.Entry(lframe,width=40,justify="center",)
t.grid(column=1,row=0,padx=1,pady=10)
l2 = tk.Label(lframe,text="Currency")
l2.grid(column=0,row=1,padx=1,pady=1,sticky="nsew")
l3 = tk.Label(lframe,text="Category")
l3.grid(column=0,row=2,padx=1,pady=1,sticky="nsew")
l4 = tk.Label(lframe,text="Payment Method")
l4.grid(column=0,row=3,padx=1,pady=1,sticky="nsew")
l5 = tk.Label(lframe,text="Date")
l5.grid(column=0,row=4,padx=1,pady=1,sticky="nsew")
dt = DateEntry(lframe, width=40, background='darkblue', foreground='white', borderwidth=2,state = "readonly", date_pattern="yyyy-mm-dd",justify="center")
dt.grid(column = 1,row = 4,padx=1,pady=10)
button = tk.Button(window,text="Add Expense",command=add_expense)
button.grid(column=0,row=1,sticky="ew")
tree = ttk.Treeview(window,columns=("Amount","Currency","Category","Payment Method","Date"),show="headings")
for col in ("Amount", "Currency", "Category", "Payment Method", "Date"):
    tree.heading(col, text=col, anchor="center")
    tree.column(col, anchor="center")
tree.grid(column=0,row=2,sticky="nsew")
scrollbar = ttk.Scrollbar(window, orient='vertical', command=tree.yview)
scrollbar.grid(row=2, column=1, sticky='ns')
error_label = tk.Label(window, text="", foreground="red")
error_label.grid(column=0, row=3, sticky="ew")

window.columnconfigure(0, weight=1)
window.rowconfigure(2, weight=2)
lframe.columnconfigure(0,weight=1)
lframe.columnconfigure(1,weight=1)

lframe.rowconfigure(0,weight=1)
lframe.rowconfigure(1,weight=1)
lframe.rowconfigure(2,weight=1)
lframe.rowconfigure(3,weight=1)
lframe.rowconfigure(4,weight=1)
window.mainloop()