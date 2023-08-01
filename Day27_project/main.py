from tkinter import *
window =Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#label
my_label=Label(text="I'm a label", font=("Arial",24,"italic"))
my_label.config(text="New text")
my_label.grid(column=0,row=0)
my_label.config(padx=20,pady=20)

#grid
# button = Button(text="Click me",command=button_clicked)
# button.grid(column=1,row=1)

#my_label.pack()

#configure
#my_label["text"]= "New Text"

#Button
def button_clicked():
    print("Clicked")
    new_text=input.get()
    my_label.config(text=new_text)

button = Button(text="Click me",command=button_clicked)
button.grid(column=1,row=1)


button = Button(text="Click me")
button.grid(column=2,row=0)

#Entry
input=Entry(width=10)
print(input.get())
input.grid(column=3,row=2)





window.mainloop()