import customtkinter as ctk
from cards import App, Menu, Cards


# Constants
BACKGROUND_COLOR = "#B1DDC6"


# UI

app = App((1200,900))
# frame = Menu(app)
# cards = Cards(app)


# menu.pack(expand=True)


app.mainloop()
# cards = Cards(app)

# window = ctk.CTk()
# window.geometry("1200x800")
# window.minsize(1200, 800)
# window.configure(padx=50, pady=50, fg_color=BACKGROUND_COLOR)
# window.grid_columnconfigure(0, weight=1)
# window.grid_rowconfigure(0, weight=1)

# game_on = "s"

# while game_on == "s":

#     cards = Cards(window)
#     flip_timer = window.after(3000, cards.flip_cards)
#     game_on = input("Escribe")

# cards.destroy_cards()

# window.mainloop()