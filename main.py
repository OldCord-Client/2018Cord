import os
import tkinter as tk
from tkinter import messagebox

# Change the background color to a cool color
BACKGROUND_COLOR = "#13294b"

class Installer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("2018cord")
        self.root.configure(bg=BACKGROUND_COLOR)
        self.create_ui()
        self.root.mainloop()

    def create_ui(self):
        # Create the install button
        self.install_button = tk.Button(self.root, text="Install", bg="#61c7d8", command=self.install)
        self.install_button.pack(pady=30)

        # Create the uninstall button
        self.uninstall_button = tk.Button(self.root, text="Uninstall", bg="#e84c3d", command=self.uninstall)
        self.uninstall_button.pack(pady=30)

    def install(self):
        # Show loading screen while installing
        self.loading_screen = tk.Toplevel(self.root)
        self.loading_screen.title("Loading...")
        self.loading_screen.geometry("150x150")
        self.loading_screen.configure(bg=BACKGROUND_COLOR)

        # Show message and destroy loading screen after 2 seconds
        message = tk.Label(self.loading_screen, text="Installing...")
        message.pack(pady=20)
        os.system(
            "CssInstaller\\Injector.exe --css template.css"
        )
        self.root.after(2000, lambda: [self.loading_screen.destroy(), messagebox.showinfo("2018cord", "Installation completed!")])

    def uninstall(self):
        # Show loading screen while uninstalling
        self.loading_screen = tk.Toplevel(self.root)
        self.loading_screen.title("Loading...")
        self.loading_screen.geometry("150x150")
        self.loading_screen.configure(bg=BACKGROUND_COLOR)

        # Show message and destroy loading screen after 2 seconds
        message = tk.Label(self.loading_screen, text="Uninstalling...")
        message.pack(pady=20)
        os.system(
            "CssInstaller\\Injector.exe --revert"
        )
        self.root.after(2000, lambda: [self.loading_screen.destroy(), messagebox.showinfo("2018cord", "Uninstallation completed!")])

# Create and run the installer
Installer()