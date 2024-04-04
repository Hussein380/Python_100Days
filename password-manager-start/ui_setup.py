from tkinter import Tk, Canvas, Label, Entry, Button, PhotoImage
from password_generator import generate_password
from password_saver import save_password

WINDOW_COLOR = "#211951"

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "huznigarane@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=lambda: save_password(website_entry.get(), email_entry.get(), password_entry.get()))
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
