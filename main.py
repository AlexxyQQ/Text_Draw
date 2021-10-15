from tkinter import *


def first_window():
    WIN = Tk()
    WIN.geometry('500x500')
    WIN.config(bg='black')

    Frame_bg = PhotoImage(file='Images\Frame 1.png')
    Label(WIN, image=Frame_bg).place(x=0, y=0)

    HEIGHT = StringVar()
    HEIGHT.set('250')
    WIDTH = StringVar()
    WIDTH.set('250')
    PPI = StringVar()
    PPI.set('50')
    H = Entry(WIN,
              text=HEIGHT,
              font=('Arial', 25),
              width=4,
              bg='#42C9B5',
              fg='white',
              bd=0).place(x=166, y=150)
    W = Entry(WIN,
              text=WIDTH,
              font=('Arial', 25),
              width=4,
              bg='#44C5BB',
              fg='white',
              bd=0).place(x=166, y=229)
    P = Entry(WIN,
              text=PPI,
              font=('Arial', 25),
              width=4,
              bg='#46C1BC',
              fg='white',
              bd=0).place(x=166, y=306)

    Button(WIN, text='Generate', font=('Arial', 25)).place(x=170, y=400)

    WIN.mainloop()


first_window()