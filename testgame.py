from memory_cards import MemoryCards
from scoreboard import Scoreboard
import time
import os


class Game(MemoryCards):
    """
    Clase que gestiona la lógica de un juego de tarjetas de memoria.

    Atributos:
        scoreboard (Scoreboard): Una instancia de la clase Scoreboard utilizada para gestionar las puntuaciones de los jugadores.
    """

    def __init__(self):
        """
        Constructor de la clase Game
        """
        self.scoreboard = Scoreboard()

    def calculate_turns(self, number_of_cards):
        """
        Calcula el número de turnos necesarios para completar una ronda en función del número de cartas.

        Args:
            number_of_cards (int): El número de cartas de la ronda.

        Return:
            int: El número de turnos necesarios para completar la ronda.
        """
        num_pairs = number_of_cards // 2
        minimum_turns = num_pairs + 2

        return minimum_turns

    def calculate_score(self, turns_left, max_turns, max_score):
        """
        Calcula la puntuación del jugador en función de los turnos restantes.

        Args:
            turns_left (int): El número de turnos restantes.
            max_turns (int): El número máximo de turnos permitidos.
            max_score (int): La puntuación máxima posible.

        Return:
            int: La puntuación calculada.
        """
        turns_left = max(0, min(turns_left, max_turns))
        score = max_score * (turns_left / max_turns)
        return round(score)

    def cls(self):
        os.system("cls" if os.name == "nt" else "clear")

    def play_game(self, num_cards, max_rounds):
        """
        Gestiona la lógica del juego de cartas de memoria, incluyendo el número de rondas, turnos y puntuación.

        Args:
            num_cards (int): El número de cartas en el juego.
            max_rondas (int): El número máximo de rondas a jugar.
        """
        current_round = 1

        while current_round <= max_rounds:
            user_turns = self.calculate_turns(num_cards)
            cards = MemoryCards.shuffle_pairs(num_cards)
            print(cards)
            time.sleep(3)
            self.cls()
            for card in cards:
                card.flipped = False
            print(cards)

            while user_turns > 0:
                card_choice1 = int(input("Elige una carta: ")) - 1
                cards[card_choice1].flip()
                print(cards[card_choice1])
                card_choice2 = int(input("Elige otra carta: ")) - 1
                cards[card_choice2].flip()
                print(cards[card_choice2])

                if MemoryCards.is_same_as(cards[card_choice1], cards[card_choice2]):
                    print("Correcto")
                    print(cards)

                else:
                    print("Incorrecto")
                    cards[card_choice1].flip()
                    cards[card_choice2].flip()
                    print(cards)

                user_turns -= 1


game = Game()
game.play_game(4, 4)
