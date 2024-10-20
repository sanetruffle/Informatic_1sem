import tkinter as tk
from tkinter import messagebox

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')  
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return '#' + ''.join(f'{val:02x}' for val in rgb_color)

def get_complementary_color(hex_color):
    rgb = hex_to_rgb(hex_color)
    complementary_rgb = (255 - rgb[0], 255 - rgb[1], 255 - rgb[2])
    return rgb_to_hex(complementary_rgb)

def calculate_color():
    user_input = entry.get()
    if not user_input.startswith('#') or len(user_input) != 7:
        messagebox.showerror("ошибка", "нужен цвет в формате HEX")
        return
    
    try:
        complementary_color = get_complementary_color(user_input)
        result_label.config(text=f"комплементарный цвет: {complementary_color}")
        result_label.config(bg=complementary_color)
    except ValueError:
        messagebox.showerror("ошибка", "формат цвета некоректен")

root = tk.Tk()
root.title("подбор комплементарного цвета")

label = tk.Label(root, text="цвет в формате HEX:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="найти комплементарный цвет", command=calculate_color)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", width=30, height=2)
result_label.pack(pady=10)

root.mainloop()
