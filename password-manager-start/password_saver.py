from tkinter import messagebox

def save_password(website, email, password):
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
