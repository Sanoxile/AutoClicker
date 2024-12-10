import tkinter as tk

# Initialize the main window
window = tk.Tk()
window.title("Checkbutton Example")
window.geometry("300x200")

# Variable to store the state of the checkbutton (1 for checked, 0 for unchecked)
check_var = tk.IntVar()

# Function to display the checkbutton status
def show_status():
    if check_var.get() == 1:
        label.config(text="Checkbox is checked!")
    else:
        label.config(text="Checkbox is unchecked!")

# Create a Checkbutton widget
checkbutton = tk.Checkbutton(window, text="Check me!", variable=check_var, command=show_status)
checkbutton.pack()

# Label to show status
label = tk.Label(window, text="Checkbox is unchecked!")
label.pack()

window.mainloop()
