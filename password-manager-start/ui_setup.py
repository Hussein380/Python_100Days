from tkinter import Tk, Canvas, Label, Entry, Button, PhotoImage
from password_generator import generate_password
from password_saver import save_password

def setup_ui():
    WINDOW_COLOR = "#211951"
    BG_COLOR_CHANGE_INTERVAL = 5000  # milliseconds

    window = Tk()
    window.config(padx=50, pady=50)
    window.title("Password Manager")

    canvas = Canvas(width=200, height=200, bg=WINDOW_COLOR)
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    website_label = Label(text="Website")
    website_label.grid(row=1, column=0)

    email_label = Label(text="Email/Username")
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

    def generate_and_insert_password():
        password = generate_password()
        password_entry.delete(0, 'end')  # Clear previous password
        password_entry.insert(0, password)

    generate_password_button = Button(text="Generate Password", command=generate_and_insert_password)
    generate_password_button.grid(row=3, column=2)

    def add_and_clear_fields():
        save_password(website_entry.get(), email_entry.get(), password_entry.get())
        website_entry.delete(0, 'end')  # Clear website entry
        password_entry.delete(0, 'end')  # Clear password entry

    add_button = Button(text="Add", width=30, command=add_and_clear_fields)
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()
