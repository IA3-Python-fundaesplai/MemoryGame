# Clase GameCards para definir, generar y controlar las cartas
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/29
# Última actualización: 2023/09/29
# Versión: 1.0

# Importamos el módulo random
import random
# Importamos la clase Card
from card import Card


class GameCards(Card):
    """
    Clase GameCards
    """

    def __init__(self, suit, value):
        """
        Constructor de la clase GameCards
        """
        super().__init__(suit, value)

    @classmethod
    def generate_random_memory_cards(cards):
        """
        Método para generar una lista al azar de 8 cartas
        """
        # Lista instanciada para guardar 8 cartas al azar
        random_cards = []
        all_suits = cards.SUITS
        all_values = cards.VALUES

        # Hacemos un bucle para generar 4 cartas de la baraja y hacer una copia de cada una
        for _ in range(4):
            suit = random.choice(all_suits)
            value = random.choice(all_values)
            card = cards(suit, value)
            random_cards.extend([card, card])

        random.shuffle(random_cards)
        return random_cards


random_memory_cards = GameCards.generate_random_memory_cards()
for card in random_memory_cards:
    print(card)
