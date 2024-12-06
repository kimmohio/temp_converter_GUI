import tkinter as ttk

simba = ttk.Tk() 
simba.title("This is temperatrue converter")
simba.geometry("500x400")

a = ttk.StringVar()
e1 = ttk.Entry(master=simba, textvar=a)
e1.place(x=50, y=100)

label1 = ttk.Label(master=simba, text='Celsius / Farenheit')
label1.place(x=150, y=100)

def convert_to_farenheit():
    try:
        value = float(a.get())
        if conversion_type.get() == "C to F":

            faren = (value*1.8) + 32 #faren is float number
            bvar.set(str(faren))
        else:
            cel = (value-32)/1.8 #cel is float number
            bvar.set(str(cel))
    
    except ValueError:
        bvar.set("Type only numbers")

#dropdown menu
conversion_type = ttk.StringVar(value="C to F")
options = ["C to F", "F to C"]
dropdown = ttk.OptionMenu(simba, conversion_type, *options)
dropdown.place(x=50, y=170)

b1 = ttk.Button(master=simba, text="Convert", command=convert_to_farenheit)
b1.place(x=100, y=200)

bvar = ttk.StringVar()
#ans1 = ttk.Label(simba, textvar=bvar)
#ans1.place(x=100, y=300)
e2 = ttk.Entry(simba, textvar=bvar)
e2.place(x = 50, y=300)

label2 = ttk.Label(simba, text="Farenheit / Celsius")
label2.place(x=150, y=300)

simba.mainloop()
