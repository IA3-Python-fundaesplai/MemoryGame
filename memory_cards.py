# Clase MemoryCards para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/29
# Última actualización: 2023/10/07
# Versión: 1.0

import math
import random
from typing import List
import copy

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

    def flip(self, card):
        """
        Método para voltear la carta
        """
        self.flipped = not self.flipped

    # def flip_cards(cards_list):
    #     return [card for card in cards_list]

    def is_same_as(card, other_card):
        """
        Método para verificar si dos cartas son iguales
        """
        return card.value == other_card.value and card.suit == other_card.suit

    def is_matched(card):
        """
        Método para verificar si la carta ha sido emparejada
        """
        return card.matched

    def get_flipped_cards(random_memory_cards):
        return [card for card in random_memory_cards if card.flipped]

    @classmethod
    def shuffle_pairs(cls, number_of_cards: int) -> List["Card"]:
        """
        Genera una lista de pares de cartas barajadas.

        Args:
            number_of_cards (int): El número de pares de cartas a generar.

        Devuelve:
            List['Card']: Una lista de pares de cartas barajadas.
        """
        all_cards = Card.generate_all_cards()
        random_cards = []

        for _ in range(number_of_cards):
            card_1 = random.choice(all_cards)
            card_2 = copy.deepcopy(card_1)
            random_cards.extend([card_1, card_2])

        random.shuffle(random_cards)

        return random_cards
