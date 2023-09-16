import tkinter as tk
from tkinter import ttk

button_status = 0


def convert():
    input = entry_int.get()
    if button_status == 0:
        km_output = input * 1.61  # 1 mile = 1.61 km
        output_string.set(km_output)
    if button_status == 1:
        mi_output = input / 1.61
        output_string.set(mi_output)

def swap():
    global button_status
    if button_status == 0:
        button_status = 1
    else:
        button_status = 0
    title_creator()  # Update the title when the button is pressed


def title_creator():
    if button_status == 0:
        title_label.config(text='Miles to kilometers')
    elif button_status == 1:
        title_label.config(text='Kilometers to miles')


# window
window = tk.Tk()  # Use Tk() instead of ttk.Window
window.title('Demo')
window.geometry("350x150")

# title
title_label = ttk.Label(master=window, text='Miles to kilometers', font='Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')

input_frame.pack(pady=10)

swap_frame = ttk.Frame(master=window)
button2 = ttk.Button(master=swap_frame, text='Swap', command=swap)
button2.pack()
swap_frame.pack()

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='Output', font='Calibri 24', textvariable=output_string)
output_label.pack()

# run
window.mainloop()
