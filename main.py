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

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
REPS = 1
CHECKS = ""
TIMER_LOOP = None
POMODORO_SETS = 0

# ---------------------------- FUNCTIONS ------------------------------- #
# ---------------------------TIMER MECHANISM -------------------------- #
def start_timer():
    # print("Start Timer...")
    WORK_SECONDS = work_seconds_entry_getter()
    SHORT_BREAK_SECONDS = short_break_seconds_entry_getter()
    LONG_BREAK_SECONDS = long_break_seconds_entry_getter()
    # Count the number of times the timer runs to count REPS
    global REPS
    print(REPS)
    # Work time blocks are at odd REPS
    if REPS in (1,3,5,7):
        count_down_timer(WORK_SECONDS)
        timer_label.config(text="Work Time", fg=GREEN)
        # create_new_checkmark()
    # Short break times are at even REPS
    if REPS in (2,4,6):
        global CHECKS
        count_down_timer(SHORT_BREAK_SECONDS)
        timer_label.config(text="Short Break Time", fg=PINK)
    # Long break time is at the 8th REPS
    elif REPS == 8:
        count_down_timer(LONG_BREAK_SECONDS)
        timer_label.config(text="Long Break Time", fg=RED)
    REPS += 1
    # ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # print("Reset Timer...")
    global REPS, CHECKS, TIMER_LOOP
    REPS = 1
    CHECKS = ""
    check_mark.config(text=CHECKS)
    window.after_cancel(TIMER_LOOP)
    timer_label.config(text="Pomodoro Timer", fg=GREEN)
    start_button.config(state="normal")
    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down_timer(seconds):
    # seconds = minutes * 60
    minutes_left, seconds_left = divmod(seconds, 60)
    if seconds >= 0:
        global TIMER_LOOP,POMODORO_SETS
        canvas.itemconfig(timer_digital_clock, text=f" {minutes_left:02}:{seconds_left:02}")
        TIMER_LOOP = window.after(1000, count_down_timer, seconds - 1)
        canvas.grid(row=1, column=1)
        start_button.config(state="disabled")
    elif seconds < 0:
        global REPS, CHECKS, POMODORO_SETS
        if REPS in (1,3,5,7):
            CHECKS += "✓"
            check_mark.config(text=CHECKS)
        elif REPS == 9:
            POMODORO_SETS += 1
            timer_label.config(text=f"Time's Up")
            pomodoro_sets_complete_label.config(text=f"Pomodoro Sets Complete: {POMODORO_SETS}")
        start_timer()
def work_seconds_entry_getter():
    work_seconds = int(work_seconds_entry.get())
    return work_seconds
def short_break_seconds_entry_getter():
    short_break_seconds = int(short_break_seconds_entry.get())
    return short_break_seconds
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
# timer_digital_clock = canvas.create_text(125, 150, text="00:00", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fill=FONT_COLOR)
minutes_left = 0
seconds_left = 0
timer_digital_clock = canvas.create_text(120, 150, text=f" {minutes_left:02}:{seconds_left:02}",font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fill=FONT_COLOR)
canvas.grid(row=1, column=1)

# BUTTONS
# Add a start and stop button
start_button = Button(text="Start", command=lambda: start_timer(), font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
reset_button = Button(text="Reset", command=lambda: reset_timer(), font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

# ENTRIES & Entry LABELS
work_seconds_entry = Entry(width=10, highlightthickness=0)
work_seconds_entry.insert(END, string="0")
work_seconds_entry.grid(row=4, column=0)
work_seconds_entry_label = Label(text="Work Seconds",font=(FONT_NAME, 18, FONT_STYLE))
work_seconds_entry_label.grid(ipadx=20, ipady=20, row=5, column=0)

short_break_seconds_entry =Entry(width=10, highlightthickness=0)
short_break_seconds_entry.insert(END, string="0")
short_break_seconds_entry.grid(row=4, column=1)
short_break_seconds_entry_label = Label(text="Short Break Seconds",font=(FONT_NAME, 18, FONT_STYLE))
short_break_seconds_entry_label.grid(ipadx=20, ipady=20, row=5, column=1)

long_break_seconds_entry = Entry(width=10, highlightthickness=0)
long_break_seconds_entry.insert(END, string="0")
long_break_seconds_entry.grid(row=4, column=2)
long_break_entry_label = Label(text="Long Break Seconds",font=(FONT_NAME, 18, FONT_STYLE))
long_break_entry_label.grid(ipadx=20, ipady=20, row=5, column=2)

# LABELS
# Add a label Timer Title
timer_label= Label(text="Pomodoro Timer", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN)
timer_label.grid(row=0, column=1)
# Add a label Checkmark Symbol
check_mark = Label(text=CHECKS, font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN)
check_mark.grid(row=3, column=1)
# Add a Pomodoro sets complete label
pomodoro_sets_complete_label = Label(text=f"Pomodoro Sets Complete 3 ✓'s: {POMODORO_SETS}", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fg=GREEN)
pomodoro_sets_complete_label.grid(ipadx=20, ipady=20, row=6, column=1)


# Keep window object open so it doesn't close
window.mainloop()