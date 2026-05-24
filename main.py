import bmi_calculator
from tkinter import *

def submit():
    try:
        weight = int(weight_entry.get())
        height = int(height_entry.get())
    except ValueError as e:
        variable.set(f"You did not enter a number!")
    else:
        if weight > 0 and height > 0:
            bmi = bmi_calculator.Bmi(weight, height)
            variable.set(f"Your bmi {bmi}")
        else:
            variable.set(f"You did not enter a positive number!")


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

variable = StringVar()
variable.set("")

your_bmi = Label(window, textvariable=variable)
your_bmi.pack()

window.iconphoto(True, icon)
window.mainloop()