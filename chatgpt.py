import requests
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

amount_list = []
currency_list = []
category_list = []
payment_list = []
date_list = []
sum_usd = []

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

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {
        "apikey": "DMunyZazMOy2HKxKCkh7EfRSWdOtyoX3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()
        return round(float(result["result"]), 2)
    except requests.exceptions.RequestException as e:
        show_error_message(f"Error: {e}")
        return None

def add_expense():
    amount = amount_entry.get()
    currency = d1.get()
    category = d2.get()
    payment_method = d3.get()
    date = date_entry.get()

    if is_integer(amount) and int(amount) > 0 and amount != "" and not_select(currency) and not_select(category) and not_select(payment_method):
        if error_label.cget("text") != "":
            error_label.config(text="")

        if amount_list:
            amount_list.pop()

        amount_list.append(amount)
        currency_list.append(currency)
        category_list.append(category)
        payment_list.append(payment_method)
        date_list.append(date)

        from_curr = currency_list[-1]
        to_curr = "USD"

        converted_amount = convert_currency(amount, from_curr, to_curr)

        if converted_amount is not None:
            sum_usd.append(converted_amount)
            total_amount = sum(sum_usd)
            amount_list.append(round(total_amount, 2))
            currency_list.append("USD")

            tree.delete(*tree.get_children())

            for i in range(len(payment_list)):
                tree.insert("", "end", values=(amount_list[i], currency_list[i], category_list[i], payment_list[i], date_list[i]))

            tag_name = f"tag{len(amount_list)}"
            tree.insert("", "end", values=(amount_list[-1], currency_list[-1]), tags=tag_name)
            tree.tag_configure(tag_name, background="yellow", font=('TkDefaultFont', 9, 'bold'))
    else:
        show_error_message("Invalid input. Please check your entries.")

window = tk.Tk()
window.title("Expense Tracker")
window.minsize(width=1000, height=700)

# Left Frame
lframe = tk.Frame(window, relief="raised")
lframe.grid(column=0, row=0, sticky="nsew")

so1 = tk.StringVar()
d1 = ttk.Combobox(lframe, textvariable=so1, values=["SAR", "EGP", "USD"], state="readonly", width=40, justify="center")
d1.grid(column=1, row=1, padx=1, pady=10)
d1.set("select")

so2 = tk.StringVar()
d2 = ttk.Combobox(lframe, textvariable=so2, values=["SuperMarket", "Apartment Expenses", "Gam3ya", "Car rent", "Installments", "Others"], state="readonly", width=40, justify="center")
d2.grid(column=1, row=2, padx=1, pady=10)
d2.set("select")

so3 = tk.StringVar()
d3 = ttk.Combobox(lframe, textvariable=so3, values=["Cash", "Hassan Visa", "Credit", "Menna Visa"], state="readonly", width=40, justify="center")
d3.grid(column=1, row=3, padx=1, pady=10)
d3.set("select")

l1 = tk.Label(lframe, text="Amount")
l1.grid(column=0, row=0, padx=1, pady=1, sticky="nsew")
amount_entry = tk.Entry(lframe, width=40, justify="center")
amount_entry.grid(column=1, row=0, padx=1, pady=10)
l2 = tk.Label(lframe, text="Currency")
l2.grid(column=0, row=1, padx=1, pady=1, sticky="nsew")
l3 = tk.Label(lframe, text="Category")
l3.grid(column=0, row=2, padx=1, pady=1, sticky="nsew")
l4 = tk.Label(lframe, text="Payment Method")
l4.grid(column=0, row=3, padx=1, pady=1, sticky="nsew")
l5 = tk.Label(lframe, text="Date")
l5.grid(column=0, row=4, padx=1, pady=1, sticky="nsew")
date_entry = DateEntry(lframe, width=40, background='darkblue', foreground='white', borderwidth=2, state="readonly", date_pattern="yyyy-mm-dd", justify="center")
date_entry.grid(column=1, row=4, padx=1, pady=10)
button = tk.Button(window, text="Add Expense", command=add_expense)
button.grid(column=0, row=1, sticky="ew")

# Treeview
tree = ttk.Treeview(window, columns=("Amount", "Currency", "Category", "Payment Method", "Date"), show="headings")
for col in ("Amount", "Currency", "Category", "Payment Method", "Date"):
    tree.heading(col, text=col, anchor="center")
    tree.column(col, anchor="center")
tree.grid(column=0, row=2, sticky="nsew")
scrollbar = ttk.Scrollbar(window, orient='vertical', command=tree.yview)
scrollbar.grid(row=2, column=1, sticky='ns')

# Error Label
error_label = tk.Label(window, text="", foreground="red")
error_label.grid(column=0, row=3, sticky="ew")

window.columnconfigure(0, weight=1)
window.rowconfigure(2, weight=2)
lframe.columnconfigure(0, weight=1)
lframe.columnconfigure(1, weight=1)

lframe.rowconfigure(0, weight=1)
lframe.rowconfigure(1, weight=1)
lframe.rowconfigure(2, weight=1)
lframe.rowconfigure(3, weight=1)
lframe.rowconfigure(4, weight=1)

window.mainloop()
