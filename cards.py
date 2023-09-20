from tkinter import *


def choice_card(index):
    return cards[index].configure(highlightthickness=5, highlightbackground="red")


def generate_card(index, image):
    return Button(image=image, highlightthickness=5, highlightbackground="#B1DDC6",
                  command=lambda: choice_card(index))


# Constants
BACKGROUND_COLOR = "#B1DDC6"

# UI

window = Tk()
window.title("Memory")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file="images/back_card.png")
card_front_img = PhotoImage(file="images/ace_of_hearts.png")
# canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=1, column=4, columnspan=4)

cards = []

for number in range(0, 8):
    if number < 4:
        cards.append(generate_card(number, card_front_img))
        cards[number].grid(row=0, column=number, rowspan=2, pady=20, padx=20)
    else:
        cards.append(generate_card(number, card_front_img))
        cards[number].grid(row=3, column=number - 4, rowspan=2, pady=20, padx=20)


window.mainloop()
