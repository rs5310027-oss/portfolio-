from tkinter import *

# Create window
root = Tk()
root.title("Calculator App")
root.geometry("300x400")

# Entry box
entry = Entry(root, width=20, font=("Arial", 20), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Button click function
def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))

# Clear function
def clear():
    entry.delete(0, END)

# Equal function
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=5, height=2, font=("Arial", 16),
               command=equal).grid(row=row, column=col)
    else:
        Button(root, text=text, width=5, height=2, font=("Arial", 16),
               command=lambda t=text: click(t)).grid(row=row, column=col)

# Clear button
Button(root, text="C", width=22, height=2, font=("Arial", 16),
       command=clear).grid(row=5, column=0, columnspan=4)

root.mainloop()