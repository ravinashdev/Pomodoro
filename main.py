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
FONT_PACK = (FONT_NAME, FONT_SIZE, FONT_STYLE)
# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 1
checks = ""
timer_loop = None
pomodoro_sets = 0
# ---------------------------- FUNCTIONS ------------------------------- #
# ---------------------------TIMER MECHANISM -------------------------- #
def start_timer():
    # print("Start Timer...")
    # Retrieve user entries
    work_seconds = work_seconds_entry_getter()
    short_break_seconds = short_break_seconds_entry_getter()
    long_break_seconds = long_break_seconds_entry_getter()
    # Retrieve global variables
    global reps
    # print(reps)
    # Work time blocks are at odd REPS
    if reps in (1, 3, 5, 7):
        count_down_timer(work_seconds)
        action_label.config(text="Work Time", fg=GREEN)
        # create_new_checkmark()
    # Short break blocks are at even REPS
    if reps in (2, 4, 6):
        global checks
        count_down_timer(short_break_seconds)
        action_label.config(text="Short Break Time", fg=PINK)
    # Long break block are at the 8th REPS
    elif reps == 8:
        count_down_timer(long_break_seconds)
        action_label.config(text="Long Break Time", fg=RED)
    # Count the number of times the timer runs to count REPS
    reps += 1
    # ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # print("Reset Timer...")
    # Retrieve global variables
    # Set them each back to the initial state
    global reps, checks, timer_loop
    reps = 1
    checks = ""
    check_mark.config(text=checks)
    # Cancel/Pause the timer
    window.after_cancel(timer_loop)
    action_label.config(text="Pomodoro Timer", fg=GREEN)
    # Set start button state back to normal (disabled on rin to prevent starting another timer while 1 is already running)
    start_button.config(state="normal")
    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down_timer(seconds):
    # seconds = minutes * 60
    minutes_left, seconds_left = divmod(seconds, 60)
    if seconds >= 0:
        # Retrieve global variables
        global timer_loop,pomodoro_sets
        canvas.itemconfig(timer_digital_clock, text=f" {minutes_left:02}:{seconds_left:02}")
        timer_loop = window.after(1000, count_down_timer, seconds - 1)
        canvas.grid(row=1, column=1)
        start_button.config(state="disabled")
    elif seconds < 0:
        global reps, checks, pomodoro_sets
        if reps in (1, 3, 5, 7):
            checks += "✓"
            check_mark.config(text=checks)
        elif reps == 9:
            pomodoro_sets += 1
            action_label.config(text=f"Time's Up")
            pomodoro_sets_complete_label.config(text=f"Pomodoro Sets Complete: {pomodoro_sets}")
        start_timer()
    # ---------------------------- WORK_SECONDS_ENTRY_GETTER ------------------------------- #
def work_seconds_entry_getter():
    work_seconds = int(work_seconds_entry.get())
    return work_seconds
    # ---------------------------- SHORT_BREAK_SECONDS_ENTRY_GETTER ------------------------------- #
def short_break_seconds_entry_getter():
    short_break_seconds = int(short_break_seconds_entry.get())
    return short_break_seconds
    # ---------------------------- LONG_BREAK_SECONDS_ENTRY_GETTER ------------------------------- #
def long_break_seconds_entry_getter():
    long_break_seconds = int(long_break_seconds_entry.get())
    return long_break_seconds
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
# Add a timer
minutes_left = 0
seconds_left = 0
timer_digital_clock = canvas.create_text(120, 150, text=f" {minutes_left:02}:{seconds_left:02}",font=FONT_PACK, fill=FONT_COLOR)
canvas.grid(row=1, column=1)

# BUTTONS
# Add a start and reset button
start_button = Button(text="Start", command=lambda: start_timer(), font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
reset_button = Button(text="Reset", command=lambda: reset_timer(), font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

# ENTRIES & Entry LABELS
# WORK SECONDS
work_seconds_entry = Entry(width=10, highlightthickness=0, justify="center")
work_seconds_entry.insert(END, string="0")
work_seconds_entry.grid(row=4, column=0)
work_seconds_entry_label = Label(text="Work Seconds",font=(FONT_NAME, 18, FONT_STYLE))
work_seconds_entry_label.grid(ipadx=20, ipady=20, row=5, column=0)
# SHORT BREAK SECONDS
short_break_seconds_entry =Entry(width=10, highlightthickness=0, justify="center")
short_break_seconds_entry.insert(END, string="0")
short_break_seconds_entry.grid(row=4, column=1)
short_break_seconds_entry_label = Label(text="Short Break Seconds",font=(FONT_NAME, 18, FONT_STYLE))
short_break_seconds_entry_label.grid(ipadx=20, ipady=20, row=5, column=1)
# LONG BREAK SECONDS
long_break_seconds_entry = Entry(width=10, highlightthickness=0, justify="center")
long_break_seconds_entry.insert(END, string="0")
long_break_seconds_entry.grid(row=4, column=2)
long_break_entry_label = Label(text="Long Break Seconds",font=(FONT_NAME, 18, FONT_STYLE))
long_break_entry_label.grid(ipadx=20, ipady=20, row=5, column=2)

# LABELS
# Add a label Timer Title
action_label= Label(text="Pomodoro Timer", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN)
action_label.grid(row=0, column=1)
# Add a label Checkmark Symbol
check_mark = Label(text=checks, font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN)
check_mark.grid(row=3, column=1)
# Add a Pomodoro sets complete label
pomodoro_sets_complete_label = Label(text=f"Pomodoro Sets Complete (3 ✓'s): {pomodoro_sets}", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN)
pomodoro_sets_complete_label.grid(ipadx=20, ipady=20, row=6, column=1)

# Keep window object open so it doesn't close
window.mainloop()