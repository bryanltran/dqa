# This code was mainly written and setup by Ethan Nguyen from Capstone Team B
# It serves as the UI (aka. Front End) for the Project

# Additional Credits & roles:
# Peace Nabwonya Kalamya ~ Front End Coding / Refinements
# Mannie Hammond ~ Back End Coding
# Zin (Thanh Hai) Nguyen ~ Back End Coding
# Byran Tran ~ Back End Coding

import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog

# Aquire Assets like images and Title
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Create the Root window
root = tk.Tk()
root.title("Dispatch Quality Assurance")
root.geometry("1600x960")
root.configure(bg = "#FFFFFF")

# Canvas for the entire UI
canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = 960,
    width = 1600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# Functionality for the top menu (PLACEHOLDERS)
def on_file_click(cmd):

    # Opens a file dialog window to open/upload WAV files
    if (cmd == "open"):
        file_path = filedialog.askopenfilename(
            title = "Open WAV File",
            filetype=[("WAV Files", "*.wav")],
            defaultextension=".wav"
        )
        
        if file_path:
            print(f"Selected file: {file_path}")

    # Save an analysis as a text document (may change to a different file format)
    elif (cmd == "save"):
        print("test")
        
def on_help_click(cmd):
    
    # Open the help window
    if (cmd == "help"):
        help_window = tk.Toplevel(root)
        help_window.title("Help")
        help_window.geometry("500x400")
        help_window.configure(bg="#FFFFFF")
        
        # Add help title text to window
        help_title_label = tk.Label(
            help_window,
            text="Help",
            bg="#FFFFFF",
            font=("Inter", 16, "bold"), 
            justify="center"             
        )
        help_title_label.pack(pady=(20, 10))
        
        # Add the help contents to the window
        help_label = tk.Label(
            help_window,
            text=("To get started, Please upload any WAV files you want to use to for analysis by either navigating to the upload page or on the top "
                  "right, click on the file drop down menu."),
 
            bg="#FFFFFF",
            font=("Inter", 12),
            justify="left",
            wraplength=450
        )
        help_label.pack(pady=0, padx=20)    
    
    # Open the about window    
    elif (cmd == "about"):
        about_window = tk.Toplevel(root)
        about_window.title("About")
        about_window.geometry("500x400")
        about_window.configure(bg="#FFFFFF")
        
        # Add about title text
        about_title_label = tk.Label(
            about_window,
            text="About",
            bg="#FFFFFF",
            font=("Inter", 16, "bold"), 
            justify="center"             
        )
        about_title_label.pack(pady=(20, 10))
        
        # Add main about contents
        about_label = tk.Label(
            about_window,
            text=(" This application listens to dispatch calls and will tell if the call needs further reviewing. This will insure that the "
                  "appropriate questions are asked and helps in quality assurance. The application mainly uses WAV files to analyze the dispatch call.\n\n"
                  "For confidentiality sake, we advise not to disclose any calls and the analysis to anyone outside of the Norman Police Department. "
                  "Thank you for using the Dispatch Quality Assurance (DQA)!"),
            
            bg="#FFFFFF",
            font=("Inter", 12),
            justify="left",
            wraplength=450
        )
        about_label.pack(pady=0, padx=20)    

def on_settings_click(cmd):

    # Open user Preferences
    if (cmd == "Preferences"):
        print("test")
        
    # Open Credit window
    elif (cmd == "credit"):
        credit_window = tk.Toplevel(root)
        credit_window.title("Credits")
        credit_window.geometry("500x500")
        credit_window.configure(bg="#FFFFFF")

    
        credit_title_label = tk.Label(
            credit_window,
            text="Credits",
            bg="#FFFFFF",
            font=("Inter", 16, "bold"), 
            justify="center"             
        )
        credit_title_label.pack(pady=(20, 10))
        
        # Add credit text
        credit_label = tk.Label(
            credit_window,
            text=("Norman Police Department:\n"
                "John Stege - Mentor\n\n"
                "FALL2024 Capstone Team B:\n"
                "Ethan Nguyen - Front End Coding, Team Manager\n"
                "Peace Nabwonya Kalamya - Front End Coding, Refinements\n"
                "Mannie Hammond - Back End Coding\n"
                "Zin (Thanh Hai) Nguyen - Back End Coding\n"
                "Byran Tran - Back End Coding"),
            bg="#FFFFFF",
            font=("Inter", 12),
            justify="center"
        )
        credit_label.pack(pady=0, padx=20)
    
# Create a menu bar
menubar = tk.Menu(root)

# Create a "File" menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open/Upload", command=lambda: on_file_click("open"))
file_menu.add_command(label="Save", command=lambda: on_file_click("save"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Files", menu=file_menu)

# Create a "Help" menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="View Help", command=lambda: on_help_click("help"))
help_menu.add_command(label="About", command=lambda: on_help_click("about"))
menubar.add_cascade(label="Help", menu=help_menu)

# Create a "Settings" menu
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command(label="Preferences", command=lambda: on_settings_click("preferences"))
settings_menu.add_command(label="Credit", command=lambda: on_settings_click("credit"))
menubar.add_cascade(label="Settings", menu=settings_menu)

# Create a "Settings" menu

# Configure the menu bar on the main window
root.config(menu=menubar)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    924.0,
    22.0,
    image=image_image_1
)

canvas.create_text(
    874.0,
    11.0,
    anchor="nw",
    text="Home",
    fill="#000000",
    font=("Inter", 20 * -1)
)

# Sidebar Canvas
sidebar_img = PhotoImage(
    file=relative_to_assets("image_2.png"))
sidebar = canvas.create_image(
    124.0,
    479.0,
    image=sidebar_img
)

# Sidebar Logo
sidebar_logo_img = PhotoImage(
    file=relative_to_assets("image_3.png"))
sidebar_logo = canvas.create_image(
    122.0,
    24.0,
    image=sidebar_logo_img
)

# Side Menu Button Commands
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=0.0,
    y=131.33834838867188,
    width=249.0,
    height=44.66165542602539
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=0.0,
    y=87.66917419433594,
    width=249.0,
    height=44.66165542602539
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=0.0,
    y=44.0,
    width=249.0,
    height=44.66165542602539
)

# Welcome Logo
welcome_img = PhotoImage(
    file=relative_to_assets("image_4.png"))
welcome_title = canvas.create_image(
    904.0,
    197.0,
    image=welcome_img
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    905.0,
    444.0,
    image=image_image_5
)

# Start Menu Button Commands
# Transcribe Button (Start)
trans_btn_img = PhotoImage(
    file=relative_to_assets("button_4.png"))
st_trans_btn = Button(
    image=trans_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Start transcribe button clicked"),
    relief="flat",
    background="#FFFFFF"
)
st_trans_btn.place(
    x=819.0,
    y=383.0,
    width=104.0,
    height=39.0
)

# Upload Button (Start)
upload_btn_img = PhotoImage(
    file=relative_to_assets("button_3.png"))
st_upload_btn = Button(
    image=upload_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Start Upload button clicked"),
    relief="flat",
    background="#FFFFFF"
)
st_upload_btn.place(
    x=822.0,
    y=431.0,
    width=77.0,
    height=24.0
)

# Setup Button (Start)
setup_btn_img = PhotoImage(
    file=relative_to_assets("button_2.png"))
st_setup_btn = Button(
    image=setup_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Start Setup button clicked"),
    relief="flat",
    background="#FFFFFF"
)
st_setup_btn.place(
    x=819.0,
    y=472.0,
    width=70.0,
    height=26.0
)

# Guide Button (Start)
guide_btn_img = PhotoImage(
    file=relative_to_assets("button_1.png"))
st_guide_btn = Button(
    image=guide_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Start guide button clicked"),
    relief="flat",
    background="#FFFFFF"
)
st_guide_btn.place(
    x=818.0,
    y=511.0,
    width=71.0,
    height=31.0
)
# Canvas for the start menu
canvas.create_rectangle(
    812.0,
    374.0,
    999.0,
    375.0,
    fill="#000000",
    outline="")

canvas.create_text(
    818.0,
    344.0,
    anchor="nw",
    text="Start",
    fill="#000000",
    font=("Inter", 18 * -1)
)


root.resizable(False, False)
root.mainloop()
