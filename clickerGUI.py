import tkinter as tk
import keyListener
import mouseListener

class ClickerGUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Auto Clicker")
        self.window.geometry("600x400")
        self.label = tk.Label(text="Advanced Autoclicker")
        self.label.pack()
        self.button = "a"
        self.keyListener = tk.Button(self.window, text=f"Key Clicked: {self.button}", command=)
        self.key = tk.IntVar()
        self.key_check_box = tk.Checkbutton(self.window, text="Key", variable=self.key)
        self.key_check_box.pack()
        self.hold = tk.IntVar()
        self.hold_check_box = tk.Checkbutton(self.window, text="Hold", variable=self.hold)
        self.hold_check_box.pack()
        self.window.mainloop()

    def start_listening(self):
        """Enable key listening and update the button text to indicate listening mode."""
        self.listening = True
        self.start_button.config(text="Listening for next key press...")
        self.root.bind("<Key>", self.key_pressed)  # Bind the key press event to key_pressed

    def key_pressed(self, event):
        """Handle key press events when listening is enabled."""
        if self.listening:
            # Save the key symbol and update the button text
            self.saved_key = event.keysym
            self.start_button.config(text=f"Saved key: {self.saved_key}")
            self.listening = False
            self.root.unbind("<Key>")  # Stop listening after one key press