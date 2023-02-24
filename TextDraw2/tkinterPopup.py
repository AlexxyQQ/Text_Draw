import tkinter as tk

from array_to_txt_gen import downsample_array


def popupmsg(msg, title, grid_state):
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    root.title(title)
    label = tk.Label(root, text=msg)
    label.grid(row=0, column=0, columnspan=4)
    B1 = tk.Button(root, text="10",
                   command=lambda: downsample_array(5, grid_state), padx=3, pady=3)
    B1.grid(row=1, column=0)
    B2 = tk.Button(root, text="12",
                   command=lambda: downsample_array(4, grid_state), padx=3, pady=3)
    B2.grid(row=1, column=1)
    B3 = tk.Button(root, text="16",
                   command=lambda: downsample_array(3, grid_state), padx=3, pady=3)
    B3.grid(row=1, column=2)
    B4 = tk.Button(root, text="25",
                   command=lambda: downsample_array(2, grid_state), padx=3, pady=3)
    B4.grid(row=1, column=3)
    B5 = tk.Button(root, text="50",
                   command=lambda: downsample_array(1, grid_state), padx=3, pady=3)
    B5.grid(row=1, column=4)
    root.mainloop()
