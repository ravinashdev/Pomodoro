# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_SIZE = 30
FONT_STYLE = "bold"
FONT_COLOR = "white"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- FUNCTIONS ------------------------------- #
def start_timer():
    print("Start Timer...")
def stop_timer():
    print("Stop Timer...")
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Initialize the window
window = Tk()
window.title("Pomodoro")
# Padding to the window
window.config(padx=100, pady=100)
# Create the canvas using the .png
canvas = Canvas(window, width=250, height=250, highlightthickness=0)
# Initialize the image in a PhotoImage class
tomato_png = PhotoImage(file="tomato.png")
# Create the image using a create_image module
canvas.create_image(125, 125, image=tomato_png)
# Add some text on top the image
canvas.create_text(125, 150, text="00:00", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fill=FONT_COLOR)
canvas.grid(row=1, column=1)

# BUTTONS
# Add a start and stop button
start_button = Button(text="Start", command=lambda: start_timer())
stop_button = Button(text="Stop", command=lambda: stop_timer())
start_button.grid(row=2, column=0)
stop_button.grid(row=2, column=2)

# LABELS
# Add a label Timer
timer_label= Label(text="Timer", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN)
timer_label.grid(row=0, column=1)
# Add a label checkmark
check_mark = Label(text="✓", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN)
check_mark.grid(row=0, column=2)
check_mark.config(fg=GREEN)
check_mark.grid(row=3, column=1)



# Keep window object open so it doesn't close
window.mainloop()