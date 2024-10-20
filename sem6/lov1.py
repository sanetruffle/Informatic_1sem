import tkinter as tk
from tkinter import messagebox

def evaluate_expression():
    try:
        expression = entry.get() 
        result = eval(expression) 
        entry.delete(0, tk.END)  
        entry.insert(tk.END, str(result))  
    except Exception as e:
        messagebox.showerror("ошибка", "выражение некоректно") 

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=30, font=("Montserrat", 14))
entry.grid(row=0, column=0, columnspan=4)

def append_to_expression(text):
    entry.insert(tk.END, text)

def clear_entry():
    entry.delete(0, tk.END)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('//', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('%', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Montserrat", 14),
                       command=lambda t=text: append_to_expression(t) if t != '=' else evaluate_expression())
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text="C", width=5, height=2, font=("Montserrat", 14), command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=4)

root.mainloop()
