import tkinter
import requests

# making tkinter window
window = tkinter.Tk()
window.geometry("800x600")
window.title("User Registration Form")
window.config(bg="gray")


# making Entries
First_name = tkinter.Entry(window, background="white").place(x=130, y=50)
Last_name = tkinter.Entry(window, background="white").place(x=130, y=100)
Email = tkinter.Entry(window, background="white").place(x=130, y=150)
Password = tkinter.Entry(window, background="white").place(x=130, y=200)
Repeat_password = tkinter.Entry(window, background="white").place(x=130, y=250)
tkinter.Entry(window, background="white").place(x=130, y=300)
tkinter.Entry(window, background="white").place(x=130, y=350)
tkinter.Entry(window, background="white").place(x=130, y=400)

# titles beside labels
tkinter.Label(window, background="gray", padx=5, pady=6, text="First Name").place(x=25, y=45)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Last Name").place(x=25, y=95)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Email").place(x=25, y=145)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Password").place(x=25, y=195)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Repeat Password").place(x=25, y=245)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Country").place(x=25, y=295)
tkinter.Label(window, background="gray", padx=5, pady=6, text="City").place(x=25, y=345)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Adress").place(x=25, y=395)


window.mainloop()
