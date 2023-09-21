from tkinter import *
from cards import Cards

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# UI

window = Tk()
window.title("Memory")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



label = Label

cards = Cards()
#cards_list = cards.generate_cards(0, 8, card_back_img)

window.mainloop()