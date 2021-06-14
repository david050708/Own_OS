import tkinter as tk
from tkinter import *

root = Tk()
root.title("OS")
root.geometry("500x500")

label1 = Label(root,text="Login").pack()
login = Entry(root,width="50",bg="white",fg="black")
login.pack()

label2 = Label(root,text="Password").pack()
password = Entry(root,width="50",bg="white",fg="black")
password.pack()



def go():
    if login.get() == "DJ050708":
        if password.get() == "david050708":
            r = Tk()
            r.title("OS Entered")
            r.geometry("300x300")
            def start():
                    r = Tk()
                    r.title("Start options")

                    r.mainloop()

            b1 = tk.Button(root,text="Start",bg="grey",fg="black",command=start).pack()

            r.mainloop()

    else:
        label2 = Label(root,text="Password or Login is Incorrect\nPlease try again").pack()


b1 = tk.Button(root,text="Go",bg="grey",fg="black",command=go).pack()
b1 = tk.Button(root,text="ShutDown",bg="grey",fg="black",command=exit).pack()

root.mainloop()
