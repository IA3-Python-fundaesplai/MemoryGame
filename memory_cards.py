# Clase MemoryCards para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/29
# Última actualización: 2023/09/30
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

    @classmethod
    def generate_random_memory_cards(cards, number_of_cards):
        """
        Método para generar una lista al azar de 8 cartas
        """
        # Lista instanciada para guardar 8 cartas al azar
        random_cards = []
        # Instanciamos dos variables para los palos y otra para los valores
        all_suits = cards.SUITS
        all_values = cards.VALUES

        # Hacemos un bucle para generar cartas de la baraja y hacer una copia de cada una
        for _ in range(number_of_cards // 2):
            # Instanciamos un generador al azar para los palos
            suit = random.choice(all_suits)
            # Hacemos lo mismo para los valores
            value = random.choice(all_values)
            # Instanciamos una variable de la clase Cards con los valores al azar
            card = cards(suit, value)
            # Guardamos en la lista de cartas dos cartas exactamente iguales
            random_cards.extend([card, card])

        # Mezclamos los elementos de la lista, en este caso, las cartas y las retornamos
        random.shuffle(random_cards)

        # Calculamos el número mínimo de turnos para finalizar el juego en base al número de cartas
        num_pairs = number_of_cards // 2
        minimum_turns = num_pairs

        # Retornamos las cartas generadas y el número de turnos requeridos
        return random_cards, minimum_turns

    def calculate_score(turns_left, max_turns, max_score):
        """
        Método para calcular la puntuación del usuario basada en los turnos restantes.
        """
        # Instanciamos una variable para calcular los turnos restantes del usuario
        turns_left = max(0, min(turns_left, max_turns))

        # Instanciamos una puntuación máxima
        max_score = max_score
        # Calculamos al puntuación del usuario según los turnos
        score = max_score * (turns_left / max_turns)

        # Retornamos la puntuación
        return round(score)

    def is_game_over(random_memory_cards):
        """
        Check if the game is over by checking if all cards are matched.
        """
        return all(card.is_matched() for card in random_memory_cards)

    def get_flipped_cards(random_memory_cards):
        return [card for card in random_memory_cards if card.flipped]
