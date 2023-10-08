# Clase Game para gestionar la lógica del juego
# Creado por: Aitor & Jon
# GitHub: https://www.github.com/aitorias | https://www.github.com/jonfdz
# Fecha creación: 2023/09/29
# Última actualización: 2023/10/08
# Versión: 1.0

import art
import os
import sqlite3
import time


from memory_cards import MemoryCards
from scoreboard import Scoreboard


class Game(MemoryCards):
    """
    Clase que gestiona la lógica de un juego de tarjetas de memoria.

    Atributos:
        scoreboard (Scoreboard): Una instancia de la clase Scoreboard utilizada para gestionar las puntuaciones de los jugadores.
        num_cards (int): El número de cartas en el juego.
    """

    def __init__(self) -> None:
        """
        Constructor de la clase Game.

        Args:
            num_cards (int): El número de cartas en el juego.
        """
        self.scoreboard = Scoreboard()
        self.num_cards = 8
        self.card_pairs = self.num_cards // 2

        self.conn = sqlite3.connect("scores.db")
        self.cursor = self.conn.cursor()

        self.play_game()

    def calculate_turns(self) -> int:
        """
        Calcula el número de turnos necesarios para completar una ronda en función del número de cartas.

        Returns:
            int: El número de turnos necesarios para completar la ronda.
        """
        total_turns = self.card_pairs * 2 + 2
        return total_turns

    def cls(self) -> None:
        """
        Limpia la pantalla de la consola.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def play_game(self) -> None:
        """
        Gestiona la lógica del juego de cartas de memoria, incluyendo el número de rondas, turnos y puntuación.
        """
        current_round = 1
        matched_pairs = 0
        user_score = 0

        print(art.logo)
        time.sleep(3)
        self.cls()

        game_on = True

        while game_on:
            cards = MemoryCards.shuffle_pairs(self.card_pairs)
            user_turns = self.calculate_turns()

            print(cards)
            print(
                        "\n------------------------------------\nMEMORIZA LAS PAREJAS\n------------------------------------\n"
                    )
            time.sleep(2)
            self.cls()

            for card in cards:
                card.flipped = False
            print(cards)
            print(
                        "\n------------------------------------\nConseguirás puntos segun tus turnos\n------------------------------------\n"
                    )

            while user_turns > 0:
                if user_turns == 1:
                    print(f"Ronda {current_round} ---------- ¡Te queda {user_turns} turno! ---------- Puntuación: {user_score}")
                else:
                    print(f"Ronda {current_round} ---------- Tienes {user_turns} turnos ---------- Puntuación: {user_score}")

                card_choice1 = int(input("Elige una carta: ")) - 1

                if cards[card_choice1].flipped:
                    print("Ya has descubierto la carta")
                    time.sleep(1)
                    self.cls()
                    print(cards)
                    continue

                cards[card_choice1].flip()
                print(cards[card_choice1])

                card_choice2 = int(input("Elige otra carta: ")) - 1

                if cards[card_choice2].flipped:
                    print("Ya has descubierto la carta")
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
                    user_score += user_turns
                    self.cls()
                    print(cards)
                    print(
                        "\n------------------------------------\nCorrecto\n------------------------------------\n"
                    )
                else:
                    self.cls()
                    cards[card_choice1].flip()
                    cards[card_choice2].flip()
                    print(cards)
                    print(
                        "\n------------------------------------\nIncorrecto\n------------------------------------\n"
                    )

                if matched_pairs == self.card_pairs:
                    # user_turns = self.calculate_turns() - current_round
                    current_round += 1
                    matched_pairs = 0
                    self.cls()
                    print(art.next_round)
                    time.sleep(3)
                    self.cls()
                    break
                user_turns -= 1

                if user_turns == 0:
                    self.cls()
                    print(
                        "\n------------------------------------\n¡Te has quedado sin turnos!\n------------------------------------\n"
                    )
                    print(art.game_over)
                    print(
                        f"\n------------------------------------\nHas conseguido {user_score} puntos\n------------------------------------\n"
                    )
                    time.sleep(3)
                    self.cls()
                    game_on = False
                    continue

        self.scoreboard.add_score(user_score)
        print("El juego ha finalizado.")


game = Game()
