import tkinter
import requests

# making tkinter window
window = tkinter.Tk()
window.geometry("800x600")
window.title("User Registration Form")
window.config(bg="gray")

# making frames for labels
title_frame = tkinter.LabelFrame(window, )

# making labels
tkinter.Label(window, background="white", padx=100, pady=6).place(x=100, y=200)
tkinter.Label(window, background="white", padx=100, pady=6).place(x=100, y=250)
tkinter.Label(window, background="white", padx=100, pady=6).place(x=100, y=300)
tkinter.Label(window, background="white", padx=100, pady=6).place(x=100, y=350)

# titles beside labels
tkinter.Label(window, background="gray", padx=20, pady=6, text="First Name").place(x=20, y=200)
tkinter.Label(window, background="gray", padx=20, pady=6, text="Last Name").place(x=20, y=250)
tkinter.Label(window, background="gray", padx=20, pady=6, text="Email").place(x=20, y=300)
tkinter.Label(window, background="gray", padx=20, pady=6, text="Password").place(x=20, y=350)


window.mainloop()
