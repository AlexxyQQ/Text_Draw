""" A Gui program that lets you draw images and transform it into text so you can send it to anyone. """
from tkinter import *


def main():
    """finds the size of the window"""
    def program_window(w, h):
        win_size.withdraw()
        screen = Tk()
        screen.title("Text Draw")
        screen.geometry(f"{w}x{h}+500+250")
        screen.resizable(False, False)

        for i in range(h // 20):
            for j in range(w // 60):
                Entry(screen, width=10).grid(row=i, column=j)
        mainloop()

    win_size = Tk()
    win_size.geometry("500x500+0+0")
    width = IntVar()
    width.set(200)
    height = IntVar()
    height.set(200)
    dpi = IntVar()
    dpi.set(10)

    w = Entry(
        win_size,
        text=width,
    )
    w.place(x=50, y=50)

    h = Entry(
        win_size,
        text=height,
    )
    h.place(x=50, y=100)

    def calling_main():

        if width.get() and height.get() >= 200:
            program_window(width.get(), height.get())

        else:
            program_window(200, 200)

    Button(win_size, text='confirm', command=calling_main).place(x=50, y=200)
    mainloop()


main()
