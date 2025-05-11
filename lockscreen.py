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
    label = tk.Label(root, text="Oops screen is locked.Nothing is harmed don't worry.", font=("Arial", 24), fg="white", bg="red")
    label.pack(expand=True, fill="both")

    # Prevent exiting with Alt+F4
    root.bind("<Alt-F4>", lambda e: "break")
    # Add a host key (Ctrl+Shift+K) to exit the program
    root.bind("<Control-Shift-K>", lambda e: root.destroy())
    # Run the application
    root.mainloop()
    
    

if __name__ == "__main__":
    lock_screen()
