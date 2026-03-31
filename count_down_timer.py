# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
DEFAULT_TIME = 300
FONT_NAME = "Courier"
FONT_SIZE = 30
FONT_STYLE = "bold"
FONT_COLOR = "white"
# ---------------------------- FUNCTIONS ------------------------------- #
class CountDownTimer(Tk):
    def __init__(self, canvas):
        super().__init__()
        self.seconds = DEFAULT_TIME
        self.canvas = canvas
        self.countdown(self.seconds)

    def countdown(self, seconds):
        self.config(text="")
        if seconds > 0:
            # Using divmod to return minutes_left and seconds_left in a tuple
            minutes_left, seconds_left = divmod(seconds, 60)
            # Display current time with a 1 leading zero in seconds and minutes
            # self.config( text=f" {minutes_left:02}:{seconds_left:02}")
            self.canvas.create_text(125, 150, text=f" {minutes_left:02}:{seconds_left:02}", font=(FONT_NAME, FONT_SIZE, FONT_STYLE), fill=FONT_COLOR)
            # Schedule the next update in 1000ms (1 second)
            self.canvas.ontimer(lambda: self.countdown(seconds - 1), 1000)