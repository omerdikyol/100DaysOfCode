from tkinter import *

window = Tk()

window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

inp = Entry(width=7)
inp.grid(column=1, row=0)

miles = Label(text="miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

converted = Label(text=0)
converted.grid(column=1, row=1)

km = Label(text="km")
km.grid(column=2, row=1)


def convert():
    mile = float(inp.get())
    converted.config(text=f"{mile * 1.609}")


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=4)

window.mainloop()
