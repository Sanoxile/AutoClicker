import tkinter as tk

class MouseListener:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Button Listener")

        # Initialize the listening state and saved button variable
        self.listening = False
        self.saved_button = None

        # Set up the button which will also show feedback
        self.start_button = tk.Button(self.root, text="Start Listening", command=self.start_listening)
        self.start_button.pack()

    def start_listening(self):
        """Enable mouse listening and update the button text to indicate listening mode."""
        self.listening = True
        self.start_button.config(text="Listening...")
        
        # Bind mouse button events 1 through 5 (to avoid errors on out-of-range buttons)
        for i in range(1, 6):
            self.root.bind(f"<Button-{i}>", self.mouse_pressed)

    def mouse_pressed(self, event):
        """Handle mouse button press events when listening is enabled."""
        if self.listening:
            # Save the mouse button number and update the button text directly
            self.saved_button = f"Button {event.num}"
            self.start_button.config(text=f"Saved: {self.saved_button}")
            self.listening = False
            
            # Unbind mouse button events 1 through 5 to stop listening after one click
            for i in range(1, 6):
                self.root.unbind(f"<Button-{i}>")

