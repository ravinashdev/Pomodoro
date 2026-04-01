# ---------------------------- IMPORTS ------------------------------- #
import tkinter
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
WORK_SECONDS = 10
SHORT_BREAK_SECONDS = 20
LONG_BREAK_SECONDS = 30
REPS = 1
# ---------------------------- FUNCTIONS ------------------------------- #
# ---------------------------- TIMER RESET ------------------------------- #
def start_timer():
    # print("Start Timer...")
    global REPS
    print(REPS)
    if REPS  == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        count_down_timer(WORK_SECONDS)
        timer_label.config(text="Work Time")
        # create_new_checkmark()
    if REPS == 2 or REPS == 4 or REPS == 6:
        count_down_timer(SHORT_BREAK_SECONDS)
        timer_label.config(text="Short Break Time")
    elif REPS == 8:
        count_down_timer(LONG_BREAK_SECONDS)
        timer_label.config(text="Long Break Time")
    REPS += 1
    # ---------------------------- TIMER MECHANISM ------------------------------- #
def stop_timer():
    print("Stop Timer...")
    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down_timer(seconds):
    minutes_left, seconds_left = divmod(seconds, 60)
    if seconds >= 0:
        window.after(1000, count_down_timer, seconds-1)
        canvas.itemconfig(timer_digital_clock, text=f" {minutes_left:02}:{seconds_left:02}")
        canvas.grid(row=1, column=1)
        start_button.config(state="disabled")
    elif seconds < 0:
        timer_label.config(text="Time's Up Hit Start to Continue")
        start_button.config(state="normal")
def create_new_checkmark():
    global REPS
    tkinter.Label(text="✓", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN).grid(row=0, column=REPS).grid(row=3, column=REPS)

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

# TIMER
# timer_digital_clock = canvas.create_text(125, 150, text="00:00", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fill=FONT_COLOR)
minutes_left = 0
seconds_left = 0
timer_digital_clock = canvas.create_text(120, 150, text=f" {minutes_left:02}:{seconds_left:02}",font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fill=FONT_COLOR)
canvas.grid(row=1, column=1)


# BUTTONS
# Add a start and stop button
start_button = Button(text="Start", command=lambda: start_timer())
stop_button = Button(text="Stop", command=lambda: stop_timer())

start_button.grid(row=2, column=0)
stop_button.grid(row=2, column=2)

# LABELS
# Add a label Timer Title
timer_label= Label(text="Timer", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN)
timer_label.grid(row=0, column=1)
# Add a label Checkmark Symbol
check_mark = Label(text="✓", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN)
check_mark.grid(row=3, column=1)

# Keep window object open so it doesn't close
window.mainloop()