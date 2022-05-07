from tkinter import *


def increase():
    global account
    account += 1
    label['text'] = f'{account} $'


def decrease():
    global account
    account -= 1
    label['text'] = f'{account} $'


app = Tk()
app.title('Clicker')
app.geometry('300x400')
account = 0

bt1 = Button(app, text='+', padx=30, pady=10, font=32, command=increase)
bt1.pack()
bt1.place(x=110, y=80)

label = Label(app, text=f'{account} $', font='Helvetica 20')
label.pack()
label.place(x=130, y=140)


bt2 = Button(app, text='-', padx=30, pady=10, font=32, command=decrease)
bt2.pack()
bt2.place(x=110, y=200)


mainloop()