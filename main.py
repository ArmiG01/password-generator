from tkinter import *
import pyperclip
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def search():
    web = entryweb.get()
    web = web.title()
    with open("pass.json") as it:
        data = json.load(it)
    try:
        datasm = data[web]["email"]
        datasp = data[web]["password"]
        messagebox.showinfo(title="Email and Password", message=f"{web}\nmail is: {datasm}\npassword is: {datasp}?")
    except KeyError:
        messagebox.showinfo(title="Error", message=f"There is no data for {web}")
    finally:
        entryweb.delete(0, END)
        entrymail.delete(0, END)
        entrymail.insert(END, "ArmanKarapetyan02@yandex.ru")
        entrypass.delete(0, END)
def generate():
  password_list = []
  while len(password_list) < 8:
    nr_letters = random.randint(4,6)
    nr_symbols = random.randint(1,2)
    nr_numbers = random.randint(1,2)

    for char in range(1, nr_letters + 1):
      password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
      password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
      password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = ""
    for char in password_list:
      password += char
    entrypass.delete(0, END)
    entrypass.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def saveii(web, mail, password):
    exy = {
    "Example": {
        "email": "Example",
        "password": "Example"
    }
}
    new_data = {
        web: {
            "email": mail,
            "password": password,
        }
    }
    if messagebox.askokcancel(title="Info", message=f"Your Website is {web}\nmail is {mail}\npassword is {password}?"):
        try:
            with open("pass.json", "r") as it:
                data = json.load(it)
                data.update(new_data)
            with open("pass.json", "w") as it:
                json.dump(data, it, indent=4)
        except FileNotFoundError:
            with open("pass.json", "w") as it:
                json.dump(exy, it, indent=4)
        else:
            with open("pass.json", "r") as it:
                data = json.load(it)
                data.update(new_data)
            with open("pass.json", "w") as it:
                json.dump(data, it, indent=4)

        finally:
            entryweb.delete(0, END)
            entrymail.delete(0, END)
            entrymail.insert(END, "ArmanKarapetyan02@yandex.ru")
            entrypass.delete(0, END)

    else:
        messagebox.showinfo(title="Info", message="You cancelled the operation!")
        entryweb.delete(0, END)
        entrymail.delete(0, END)
        entrymail.insert(END, "ArmanKarapetyan02@yandex.ru")
        entrypass.delete(0, END)
def save():
    web = entryweb.get()
    web = web.title()
    mail = entrymail.get()
    password = entrypass.get()
    if len(web) < 1 or len(mail) < 1 or len(password) < 1:
        messagebox.showinfo(title="Inccorect!", message="You missed something")
    else:
        saveii(web, mail, password)
# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password!")
windows.config(bg="#fcf8e8", padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="#fcf8e8", highlightthickness=0)
PIC = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=PIC)
canvas.grid(column=1, row=0)

labelweb = Label(text="Website:", font=("Courier", 12, "bold"), bg="#fcf8e8")
labelweb.grid(column=0, row=1)

labelemail = Label(text="Email/Username:", font=("Courier", 12, "bold"), bg="#fcf8e8")
labelemail.grid(column=0, row=2)

labelpass = Label(text="Password:", font=("Courier", 12, "bold"), bg="#fcf8e8")
labelpass.grid(column=0, row=3)

entryweb = Entry(width=25)
entryweb.place(x=180,y=200)
entryweb.focus()
buttons = Button(text="Search", command=search)
buttons.place(x=338,y=195)

entrymail = Entry(width=35)
entrymail.grid(column=1, row=2, columnspan=2)
entrymail.insert(END, "ArmanKarapetyan02@yandex.ru")

entrypass = Entry(width=25)
entrypass.place(x=180,y=250)

button = Button(text="Generate", command=generate)
button.place(x=338,y=250)

labelweb1 = Label(bg="#fcf8e8")
labelweb1.grid(column=1, row=4)

buttonadd = Button(width=36, text="Add", command=save)
buttonadd.grid(column=1, row=5, columnspan=2)


windows.mainloop()