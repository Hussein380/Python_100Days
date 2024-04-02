import tkinter

window = tkinter.Tk()
window.title("My First GuI programme")
window.minsize(width=500, height=300)

#label
my_label = tkinter.Label(text="I am Huzni-label", font=("Aeriel", 15, "bold"))
my_label.pack()



def button_click():
    print("I get clicked")
    my_label.config(text="Button Got clicked")

button = tkinter.Button(text="Click Me", command=button_click)
button.pack()

#entry

input = tkinter.Entry(width=10)
print(input.get())
input.pack()

button.pack()









window.mainloop()