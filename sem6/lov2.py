import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())  
        height = float(entry_height.get()) / 100  
        
        bmi = weight / (height ** 2)  
        bmi = round(bmi, 2)  
        
        result_label.config(text=f"Твой ИМТ: {bmi}")  
        
        if bmi <= 16:
            interpretation = "Выраженный дефицит массы тела"
        elif 16 < bmi <= 18.5:
            interpretation = "Недостаточная масса тела"
        elif 18.5 < bmi <= 25:
            interpretation = "Норма"
        elif 25 < bmi <= 30:
            interpretation = "Избыточная масса тела (предожирение)"
        elif 30 < bmi <= 35:
            interpretation = "Ожирение 1 степени"
        elif 35 < bmi <= 40:
            interpretation = "Ожирение 2 степени"
        else:
            interpretation = "Ожирение 3 степени"
        
        interpretation_label.config(text=f"Твоя судьба: {interpretation}")
    
    except ValueError:
        messagebox.showerror("ошибка", "просьба ввести нормальные значения")

root = tk.Tk()
root.title("Калькулятор ИМТ")

label_weight = tk.Label(root, text="Вес (кг):", font=("Montserrat", 12))
label_weight.grid(row=0, column=0, padx=10, pady=10)

entry_weight = tk.Entry(root, width=10, font=("Montserrat", 12))
entry_weight.grid(row=0, column=1, padx=10, pady=10)

label_height = tk.Label(root, text="Рост (см):", font=("Montserrat", 12))
label_height.grid(row=1, column=0, padx=10, pady=10)

entry_height = tk.Entry(root, width=10, font=("Montserrat", 12))
entry_height.grid(row=1, column=1, padx=10, pady=10)

calc_button = tk.Button(root, text="Рассчитать ИМТ", font=("Montserrat", 12), command=calculate_bmi)
calc_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Твой ИМТ: ", font=("Montserrat", 12))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

interpretation_label = tk.Label(root, text="Твоя судьба: ", font=("Montserrat", 12))
interpretation_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
