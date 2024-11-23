#!/usr/bin/env python3

import tkinter as tk
import subprocess
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.wm_title("Ollama Dashboard")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create a label for the GUI
        self.label = tk.Label(self, font=('Sans-Regular', 21))
        self.label["text"] = "Ollama Dashboard"
        self.label.pack(side="top", pady=(8,0))

        # Create buttons
        self.button1 = tk.Button(self)
        self.button1["text"] = "Turn ON"
        self.button1.config(width=8, height=6)
        self.button1.pack(padx=8, pady=(32,16))
        self.button1.configure(
    bg="#007000",  # Green background
    fg="#FFFFFF",  # White text color
    highlightbackground="#AAAAAA",  # Light gray highlight border
    activebackground="#005500",  # Dark green background when clicked
    activeforeground="#FFFFFF",  # White text color when clicked
)
        self.button1["command"] = self.button1_clicked
        self.button1.pack(side="left")

        self.button2 = tk.Button(self)
        self.button2["text"] = "Turn OFF"
        self.button2.config(width=8, height=6)
        self.button2.pack(padx=8, pady=(32,16))
        self.button2.configure(
    bg="#FF0000",  # Red background
    fg="#FFFFFF",  # White text color
    highlightbackground="#AAAAAA",  # Light gray highlight border
    activebackground="#550000",  # Dark red background when clicked
    activeforeground="#FFFFFF",  # White text color when clicked
)

        self.button2["command"] = self.button2_clicked
        self.button2.pack(side="left")

        self.button3 = tk.Button(self)
        self.button3["text"] = "Open Hollama"
        self.button3.config(width=15, height=6)
        self.button3.pack(padx=8, pady=(32,16))
        self.button3.configure(
    bg="#008000",  # Green background
    fg="#FFFFFF",  # White text color
    highlightbackground="#AAAAAA",  # Light gray highlight border
    activebackground="#005500",  # Dark green background when clicked
    activeforeground="#FFFFFF",  # White text color when clicked
)

        self.button3["command"] = self.button3_clicked
        self.button3.pack(side="left")

    def button1_clicked(self):
        run_command(['systemctl', 'start', 'ollama'])

    def button2_clicked(self):
        run_command(['systemctl', 'stop', 'ollama'])

    def button3_clicked(self):
        hollamaPath = read_hollama_path()
        run_command([hollamaPath])


# Open a file dialog and get the selected file path
def open_file():
    try:
        filepath = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("x-executable", "*.exe"), ("All files", "**"))
    )
        if not filepath:
            return  # No file selected
    
    # Save the filepath on a txt file
        with open("hollama_path.txt", "w") as output_file:
            output_file.write(filepath)
    except Exception as e:
        print(f"An error occurred: {e}")


# Read the Hollama path from a text file
def read_hollama_path():
    try:
        with open("hollama_path.txt", "r") as input_file:
            hollama_filepath = input_file.read().strip()
            return hollama_filepath
    except FileNotFoundError:
        #print("File 'hollama_path.txt' not found.")
        open_file()

 #Executes a shell command and prints the result.
def run_command(command):
    try:
        result = subprocess.run(command, check=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with code {e.returncode}: {e.output}")
      


# Create the main window
root = tk.Tk()

# Set the initial window size
root.geometry("350x200")  # width x height

# Create an instance of our Application class
app = Application(master=root)

# Start the application's main loop
app.mainloop()
