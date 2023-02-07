import tkinter
import requests

# making tkinter window
window = tkinter.Tk()
window.geometry("600x600")
window.title("User Registration Form")
window.config(bg="gray")


# making Entries
First_name = tkinter.Entry(window, background="white")
First_name.place(x=130, y=50)
Last_name = tkinter.Entry(window, background="white")
Last_name.place(x=130, y=100)
Email = tkinter.Entry(window, background="white")
Email.place(x=130, y=150)
Password = tkinter.Entry(window, background="white")
Password.place(x=130, y=200)
Repeat_password = tkinter.Entry(window, background="white")
Repeat_password.place(x=130, y=250)
Country = tkinter.Entry(window, background="white")
Country.place(x=130, y=300)
City = tkinter.Entry(window, background="white")
City.place(x=130, y=350)
Adress = tkinter.Entry(window, background="white")
Adress.place(x=130, y=400)



# titles beside labels
tkinter.Label(window, background="gray", padx=5, pady=6, text="First Name").place(x=25, y=45)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Last Name").place(x=25, y=95)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Email").place(x=25, y=145)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Password").place(x=25, y=195)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Repeat Password").place(x=25, y=245)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Country").place(x=25, y=295)
tkinter.Label(window, background="gray", padx=5, pady=6, text="City").place(x=25, y=345)
tkinter.Label(window, background="gray", padx=5, pady=6, text="Adress").place(x=25, y=395)


user_list = []


def save():
    a = First_name.get()
    b = Last_name.get()
    c = Email.get()
    d = Password.get()
    e = Repeat_password.get()
    f = Country.get()
    g = City.get()
    h = Adress.get()
    if any(c in x for x in user_list):
        print("this email already exists")
    elif d != e:
        print("password doesn't match")
    else:
        user_list.append([a, b, c, d, f, g, h])
        print(user_list)
        print(len(user_list))
        print("registered succesfully")

# making buttons
save_button = tkinter.Button(window, text="Register", width=10, height=2, background="green", command=save)
save_button.place(x=200, y=500)



window.mainloop()
