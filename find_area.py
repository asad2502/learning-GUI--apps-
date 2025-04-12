x = 1

if x == 0:
    # to show asad next time 
    height  = int(input("Enter the height of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    area = height * width
    print("The area of the rectangle is:", area)


if x == 1:
    import tkinter as tk
    lb1 = tk.Label(text="Enter the height of the rectangle:")
    lb1.pack()
    edt1 = tk.Entry()
    edt1.pack()

    lb2 = tk.Label(text="Enter the width of the rectangle:")
    lb2.pack()
    edt2 = tk.Entry()
    edt2.pack()


    btn = tk.Button(text="Calculate Area", command=lambda: calculate_area(edt1.get(), edt2.get())) 
    btn.pack()

    def calculate_area(height, width):
        try:
            height = float(height)
            width = float(width)
            area = height * width
            label_result.config(text=f"Area: {area}")
        except ValueError:
            label_result.config(text="Please enter valid numbers.")

    label_result = tk.Label(text="Area:")
    label_result.pack()

    tk.mainloop()
