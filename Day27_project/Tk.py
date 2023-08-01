from tkinter import *
window=Tk()
window.minsize(width=500,height=300)
window.title("Mile to kilometer converter")
window.config(padx=20,pady=20)

def miles_to_kilometre():
    miles=float(miles_input.get())
    km= miles * 1.689
    kilometre_value.config(text=f"{km}")
miles_input=Entry(width=10)
miles_input.grid(column=1,row=0)

miles_label=Label(text="miles")
miles_label.grid(column=2,row=0)

is_equal_to=Label(text="Is equal to")
is_equal_to.grid(column=0,row=1)

kilometre_value=Label(text=0)
kilometre_value.grid(column=1,row=1)

kilometres_label=Label(text="km")
kilometres_label.grid(column=2,row=1)


calculate_button=Button(text="Calculate",command=miles_to_kilometre)
calculate_button.grid(column=1,row=2)








window.mainloop()