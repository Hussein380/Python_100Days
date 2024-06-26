from tkinter import *
from tkinter import messagebox
import random


WINDOW_COLOR = "#211951"
BG_COLOR_CHANGE_INTERVAL = 5000  # milliseconds


# Password Generator Function
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pasword_entry.delete(0, END)
    pasword_entry.insert(0, password)

# Save Password Function
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = pasword_entry.get()

    if not website or not password:
        if not website and not password:
            messagebox.showerror("Error", "Please enter both website and password")
        elif not website:
            messagebox.showerror("Error", "Please enter the website")
        else:
            messagebox.showerror("Error", "Please enter the password")
        return
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Confirm your details:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            messagebox.showinfo("Success", "Password saved successfully")

            website_entry.delete(0, END)
            pasword_entry.delete(0, END)


def change_backgroud_color():
    color = "#{:06x}".format(random.randint(0,  0xFFFFFF))
    window.config(bg=color)
    window.after(BG_COLOR_CHANGE_INTERVAL)
# UI Setup
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

#background_color change
change_backgroud_color()


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

pasword_entry = Entry(width=21)
pasword_entry.grid(row=3, column=1, columnspan=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
