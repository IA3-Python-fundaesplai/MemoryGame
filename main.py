from tkinter import *
from cards import Cards


# Constants
BACKGROUND_COLOR = "#B1DDC6"


# UI

window = Tk()
window.title("Memory")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
MEMORY_IMAGE = PhotoImage(file="images/memory.jpg")
canvas = Canvas(width=1200, height=900, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(image=MEMORY_IMAGE)
canvas.grid(row=0, column=0)

game_on = "s"

while game_on == "s":

    cards = Cards()
    cards.master_buttons(canvas)
    flip_timer = window.after(3000, cards.flip_cards)
    game_on = input("Escribe")

cards.destroy_cards()
canvas = Canvas(width=1225, height=835, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)




window.mainloop()