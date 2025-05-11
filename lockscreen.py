import tkinter as tk

def lock_screen():
    # Create the main application window
    root = tk.Tk()
    root.title("Locked Screen")

    # Make the window fullscreen
    root.attributes("-fullscreen", True)

    # Disable closing the window
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    # Add a label to display a message
    label = tk.Label(root, text="Screen is locked. Contact the administrator.", font=("Arial", 24), fg="white", bg="black")
    label.pack(expand=True, fill="both")

    # Prevent exiting with Alt+F4
    root.bind("<Alt-F4>", lambda e: "break")

    # Run the application
    root.mainloop()
    # Hide the taskbar
    root.overrideredirect(True)

if __name__ == "__main__":
    lock_screen()