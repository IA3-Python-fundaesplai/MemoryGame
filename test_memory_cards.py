# # Clase TestMemoryCards para hacer test sobre la clase MemoryCards
# Creado por: Aitor & Jon
# GitHub: https://www.github.com/aitorias | https://www.github.com/jonfdz
# Fecha creación: 2023/10/07
# Última actualización: 2023/10/07
# Versión: 1.0


import pytest

from memory_cards import MemoryCards


class TestMemoryCards:

    def test_create_memory_cards_instance(self):
        suit = "Corazones"
        value = "As"
        memory_card = MemoryCards(suit, value)

        assert memory_card.suit == suit
        assert memory_card.value == value

    # Flip a MemoryCards instance
    def test_flip_memory_card_instance(self):
        suit = "Corazones"
        value = "As"
        memory_card = MemoryCards(suit, value)

        assert not memory_card.flipped
        memory_card.flip()
        assert memory_card.flipped
