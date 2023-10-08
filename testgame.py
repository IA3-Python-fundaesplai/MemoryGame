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

    def __init__(self, num_cards):
        """
        Constructor de la clase Game
        """
        self.scoreboard = Scoreboard()
        self.num_cards = num_cards
        self.play_game(self.num_cards)

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

    def calculate_score(self, matched_pairs):
        """
        Calcula la puntuación del jugador en función de los turnos restantes.

        Args:
            matched_pairs (int): El número de parejas acertadas.

        Return:
            int: La puntuación calculada.
        """
        score = matched_pairs * 10
        return round(score)

    def cls(self):
        os.system("cls" if os.name == "nt" else "clear")

    def play_game(self, num_cards):
        """
        Gestiona la lógica del juego de cartas de memoria, incluyendo el número de rondas, turnos y puntuación.

        Args:
            num_cards (int): El número de cartas en el juego.
            max_rondas (int): El número máximo de rondas a jugar.
        """
        current_round = 1
        max_rounds = self.calculate_turns(self.num_cards)
        user_score = 0
        matched_pairs = 0

        print('MEMO GAME')

        game_on = True

        while game_on:
            num_cards_round = num_cards + current_round - 1
            user_turns = self.calculate_turns(num_cards_round)
            cards = MemoryCards.shuffle_pairs(num_cards_round)
            print(cards)
            time.sleep(10)
            self.cls()
            for card in cards:
                card.flipped = False
            print(cards)

            while user_turns > 0:
                card_choice1 = int(input("Elige una carta: ")) - 1
                if cards[card_choice1].flipped:
                    print('Ya has descubierto la carta')
                    time.sleep(1)
                    self.cls()
                    print(cards)
                    continue
                cards[card_choice1].flip()
                print(cards[card_choice1])
                card_choice2 = int(input("Elige otra carta: ")) - 1

                if cards[card_choice2].flipped:
                    print('Ya has descubierto la carta')
                    time.sleep(1)
                    self.cls()
                    cards[card_choice1].flip()
                    print(cards)
                    continue
                cards[card_choice2].flip()
                print(cards[card_choice2])
                time.sleep(1)

                if MemoryCards.is_same_as(cards[card_choice1], cards[card_choice2]):
                    matched_pairs += 1
                    user_score += 1
                    self.cls()
                    print(cards)
                    print("\n------------------------------------\nCorrecto\n------------------------------------\n")

                else:
                    self.cls()
                    cards[card_choice1].flip()
                    cards[card_choice2].flip()
                    print(cards)
                    print("\n------------------------------------\nIncorrecto\n------------------------------------\n")

                if matched_pairs == num_cards // 2:
                    current_round += 1
                    break
                user_turns -= 1

        self.scoreboard.add_score(matched_pairs)
        print('El juego ha finalizado.')


game = Game(4)
