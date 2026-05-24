import bmi_calculator
import bmi_indicator
from tkinter import *

def submit():
    try:
        weight = int(weight_entry.get())
        height = int(height_entry.get())
    except ValueError as e:
        bmi_variable.set(f"You did not enter a number!")
        indicator_variable.set("")
    else:
        if weight > 0 and height > 0:
            bmi = bmi_calculator.calculator(weight, height)
            bmi_variable.set(f"Your bmi {bmi}")
            indicator_variable.set(bmi_indicator.indicator(bmi))
        else:
            bmi_variable.set(f"You did not enter a positive number!")
            indicator_variable.set("")


window = Tk()
window.geometry("420x420")
window.title("BMI calculator")
icon = PhotoImage(file='logo.png')
button = Button(window, text="Check")

header = Label(window, text = "Bmi calculator", font=('Arial', 20, 'bold'), fg='green')
header.pack()

weight_label = Label(window, text = "Insert your weight: ")
weight_label.pack()
weight_entry = Entry(window, font=('Arial', 10, 'bold'))
weight_entry.pack()

height_label = Label(window, text = "Insert your height (cm): ")
height_label.pack()

height_entry = Entry(window, font=('Arial', 10, 'bold'))
height_entry.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

bmi_variable = StringVar()
bmi_variable.set("")

your_bmi = Label(window, textvariable=bmi_variable)
your_bmi.pack()

indicator_variable = StringVar()
indicator_variable.set("")

your_indicator = Label(window, textvariable=indicator_variable)
your_indicator.pack()

window.iconphoto(True, icon)
window.mainloop()