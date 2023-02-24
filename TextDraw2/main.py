from tkinter import *

from second_window import second_window

def first_window():

    WIN = Tk()
    WIN.geometry('500x500')
    WIN.config(bg='black')
    WIN.iconbitmap('Images/icon.ico')
    WIN.title('Text Draw')
    Frame_bg = PhotoImage(file='Images\Frame 1.png')
    Label(WIN, image=Frame_bg).place(x=0, y=0)
  

   

    def gen_windows():

        WIN.withdraw()
        second_window()


    Button_image = PhotoImage(file='Images\Button Grn.png')

    Button(
        WIN,
        image=Button_image,
        bg='#48BEBF',
        bd=0,
        activebackground='#48BEBF',
        command=gen_windows,
    ).place(x=76, y=400)

    WIN.mainloop()


first_window()