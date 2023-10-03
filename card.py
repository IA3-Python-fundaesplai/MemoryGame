# Clase Card para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/29
# Última actualización: 2023/10/03
# Versión: 1.0

import random


class Card():
    """
    Clase Card
    """
    SUITS = ["Corazones", "Diamantes", "Picas", "Tréboles"]
    VALUES = ["2", "3", "4", "5", "6", "7", "8",
              "9", "10", "Jota", "Reina", "Rey", "As"]

    def __init__(self, suit, value):
        """
        Constructor de la clase Card
        """
        if suit in self.SUITS and value in self.VALUES:
            self.suit = suit
            self.value = value
        else:
            raise ValueError("Error en el palo o valor de la carta")

    def __repr__(self):
        """
        Representación de una instancia de la clase Card
        """
        return f'Carta: {self.value} de {self.suit}'

    def __str__(self):
        """
        Representación de un objeto de la clase Card
        """
        return f'Carta: {self.value} de {self.suit}\n'

    def generate_all_cards():
        """
        Función para generar todas las cartas
        """
        deck = [Card(suit, value)
                for suit in Card.SUITS for value in Card.VALUES]
        return deck

    def shuffle_pairs(number_of_cards):
        """
        Método para generar una lista de cartas al azar 
        """
        # Lista instanciada para guardar cartas al azar
        random_cards = []
        # Instanciamos dos variables para los palos y otra para los valores
        all_suits = Card.SUITS
        all_values = Card.VALUES

        # Hacemos un bucle para generar cartas de la baraja y hacer una copia de cada una
        for _ in range(number_of_cards):
            # Instanciamos un generador al azar para los palos
            suit = random.choice(all_suits)
            # Hacemos lo mismo para los valores
            value = random.choice(all_values)
            # Instanciamos una variable de la clase Cards con los valores al azar
            card = Card(suit, value)
            # Guardamos en la lista de cartas dos cartas exactamente iguales
            random_cards.extend([card, card])

        # Mezclamos la lista de cartas
        random.shuffle(random_cards)

        # Y retornamos la lista de cartas al azar
        return random_cards
