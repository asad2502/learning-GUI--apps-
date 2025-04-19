

import tkinter as tk
lb1 = tk.Label(text="Enter the height of the cube:")
lb1.pack()
edt1 = tk.Entry()
edt1.pack()

lb2 = tk.Label(text="Enter the width of the cube:")
lb2.pack()
edt2 = tk.Entry()
edt2.pack()

lb3 = tk.Label(text="Enter the base area of the cube:")
lb3.pack()
edt3 = tk.Entry()
edt3.pack()


btn = tk.Button(text="Calculate Area", command=lambda: calculate_area(edt1.get(), edt2.get(), edt3.get()))
btn.pack()

def calculate_area(height, width, base):
    try:
        height = float(height)
        width = float(width)
        base = float(base)
        area = height * width * base
        label_result.config(text=f"Area: {area}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")

label_result = tk.Label(text="Area:")
label_result.pack()

tk.mainloop()