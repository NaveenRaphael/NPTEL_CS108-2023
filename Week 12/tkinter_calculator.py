import tkinter as tk
from tkinter import ttk


def press_eq():
    '''
    Resets the view in the calculator
    '''
    text.set("")


window = tk.Tk()

text = tk.StringVar(value="Initial value")
show_region = tk.Label(window, textvariable=text)

button_region = tk.Frame(window)

number_buttons = [ttk.Button(button_region, text=f"{i}", command=lambda i=i: text.set(
    text.get()+f"{i}")) for i in range(10)]

operation_button = {i: ttk.Button(button_region, text=f"{i}", command=lambda i=i: text.set(
    text.get()+f"{i}")) for i in [
    ".", "=", "+", "-", "*", r"/"]}

number_buttons[0].grid(row=3, column=1, padx=4, pady=4)
number_buttons[1].grid(row=2, column=0, padx=4, pady=4)
number_buttons[2].grid(row=2, column=1, padx=4, pady=4)
number_buttons[3].grid(row=2, column=2, padx=4, pady=4)
number_buttons[4].grid(row=1, column=0, padx=4, pady=4)
number_buttons[5].grid(row=1, column=1, padx=4, pady=4)
number_buttons[6].grid(row=1, column=2, padx=4, pady=4)
number_buttons[7].grid(row=0, column=0, padx=4, pady=4)
number_buttons[8].grid(row=0, column=1, padx=4, pady=4)
number_buttons[9].grid(row=0, column=2, padx=4, pady=4)

operation_button["="].grid(row=3, column=3, padx=4, pady=4)
operation_button["."].grid(row=3, column=2, padx=4, pady=4)
operation_button["+"].grid(row=0, column=3, padx=4, pady=4)
operation_button["-"].grid(row=1, column=3, padx=4, pady=4)
operation_button["*"].grid(row=2, column=3, padx=4, pady=4)
operation_button[r"/"].grid(row=3, column=0, padx=4, pady=4)

show_region.grid(row=0, column=0)
button_region.grid(row=1, column=0)

operation_button["="].configure(command=press_eq)

text.set("why")

window.title("Broken calculator")
window.mainloop()
