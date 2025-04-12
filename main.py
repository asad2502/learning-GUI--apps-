# a window with 1 editor 1 button and 1 label
import tkinter as tk


window = tk.Tk()
window.title("My First GUI")
window.geometry("400x300")

label = tk.Label(window, text="Hello World")
label.pack()

editor = tk.Text(window, height=10, width=30)
editor.pack()


def on_button_click():
    text = editor.get("1.0", tk.END)
    label.config(text=text)

button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()



tk.mainloop()



