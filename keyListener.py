import tkinter as tk

class KeyListener:
    def __init__(self, root):
        self.root = root
        self.root.title("Save Next Key Press")

        # Initialize the listening state and saved key variable
        self.listening = False
        self.saved_key = None

        # Set up the button which will also show feedback
        self.start_button = tk.Button(self.root, text="Start Listening", command=self.start_listening)
        self.start_button.pack()

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

