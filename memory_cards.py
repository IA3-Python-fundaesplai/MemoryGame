# Clase MemoryCards para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/29
# Última actualización: 2023/10/03
# Versión: 1.0

import math
import random
# Importamos la clase Card
from card import Card


class MemoryCards(Card):
    """
    Clase MemoryCards
    """

    def __init__(self, suit, value):
        """
        Constructor de la clase MemoryCards
        """
        super().__init__(suit, value)
        self.flipped = False
        self.matched = False

    def __str__(self):
        """
        Override the __str__ method to show card state.
        """
        if self.flipped:
            return super().__str__()
        else:
            return "Card: [Flipped Down]"

    def flip(self):
        """
        Método para voltear la carta
        """
        self.flipped = not self.flipped

    def is_same_as(self, other_card):
        """
        Método para verificar si dos cartas son iguales
        """
        return self.value == other_card.value and self.suit == other_card.suit

    def is_matched(self):
        """
        Método para verificar si la carta ha sido emparejada
        """
        return self.matched

    def get_flipped_cards(random_memory_cards):
        return [card for card in random_memory_cards if card.flipped]
