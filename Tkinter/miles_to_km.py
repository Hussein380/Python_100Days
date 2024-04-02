

import tkinter

def  calculate_km():
    try:
        # Get the value entered by the user in miles
        miles_str = input_entry.get()
        if miles_str:
            miles = float(miles_str)
            km = miles * 1.60934

            result_label.config(text=f"{km:.2f} km")
       


    except ValueError:
        result_label.config(text="invalid input")




window = tkinter.Tk()
window.title("Miles to km converter")
window.minsize(width=500, height=300)

# Entry widget for user input
input_entry = tkinter.Entry(width=10)
input_entry.grid(row=0, column=1)

miles_label = tkinter.Label(window, text="Miles")
miles_label.grid(row=0, column=2)

# Label indicating "is equal to"
is_equal_label = tkinter.Label(text="Is equal to")
is_equal_label.grid(row=1, column=0)
# Label for displaying the result
result_label = tkinter.Label(text="", width=20)
result_label.grid(row=1, column=1)


is_dash_label = tkinter.Label(text="km")
is_dash_label.grid(row=1, column=2)


is_calculate_label = tkinter.Label(text="km")
is_calculate_label.grid(row=1, column=2)

button = tkinter.Button(text="calculate", command=calculate_km)
button.grid(row=2, column=1)

# Label to display the result
#result_label = tkinter.Label(window, text="")
#result_label.grid(row=1, column=1)

window.mainloop()

