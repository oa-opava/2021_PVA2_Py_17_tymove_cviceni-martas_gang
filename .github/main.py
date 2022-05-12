import tkinter as tk
from tkinter import*
from tkinter import messagebox

w = Tk()
frame = Frame(w)
w.geometry("500x150")

def Jm():
    print("Jméno: " + e1.get() +"\nPříjmení: "+ e2.get()+"\ne-mail:"+ e3.get())

Label(w, text="Pohlaví").grid(row=0)
Label(w, text="datum narození").grid(row=1)
Label(w, text="věk").grid(row=2)

e1 = Entry(w)
e2 = Entry(w)
e3 = Entry(w)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

button= Button(w, text="Zobrazit údaje", width=15, command=Jm,)
button.grid(row=4, column=0)

w.title("tlačítko")
butt = tk.Button(w, text = "zavřít",width=15, command=w.destroy)
butt.grid(row=4, column=1)



mainloop()