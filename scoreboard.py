# Clase Scoreboard gestionar las puntuaciones del usuario.
# Creado por: Aitor & Jon
# GitHub: https://www.github.com/aitorias | https://www.github.com/jonfdz
# Fecha creación: 2023/09/22
# Última actualización: 2023/10/16
# Versión: 1.0

import art
import datetime
import locale

from log import Log
from database import Database


class Scoreboard:
    def __init__(self):
        """
        Constructor de la clase Scoreboard
        """
        self.user = "player_1"
        self.language = locale.getdefaultlocale()[0]
        self.score = 0

        self.log = Log(log_file=f'{self.user}-log.log')
        self.db = Database()

    def __str__(self):
        """
        Representación de una instancia de la clase Scoreboard
        """
        return f"Jugador: {self.user} | Puntuaciones: {self.scores}"

    def get_scores(self):
        """
        Función que carga las puntuaciones desde la base de datos
        """

        scores = self.db.fetch_query("SELECT * FROM scoreboard")
        return scores

    def add_score(self, score):
        """
        Función para añadir una nueva puntuación a la base de datos
        """
        date = datetime.datetime.now()
        self.user = input("Introduzca su nombre: ").upper()
        self.score = score

        self.db.commit_query("INSERT INTO scoreboard (fecha, nombre, puntuacion) VALUES (?, ?, ?)", (date, self.user, self.score))

        log_message = f'Puntuación {score} para el jugador {self.user} en {date} añadida correctamente.'
        self.log.log_info(log_message)

    def print_scoreboard(self):
        """
        Funcion para printear la clasificacion ordenada en pantalla
        """
        quit = ""

        while quit == "":
            print(art.scoreboard_art)
            print("\n\n")
            count = 1

            scores = self.db.fetch_query('SELECT nombre, max(puntuacion), STRFTIME("%d-%m-%Y", fecha) FROM scoreboard GROUP BY nombre ORDER BY puntuacion DESC')

            for index in scores:
                print(
                    f"{count}.- {index[0]}: {index[1]} puntos | Fecha: {index[2]}")
                count += 1

            quit = input("\nPulse enter para volver al menu.")
            break

    def score_label(self):
        '''
        Funcion para parsear los scores en un texto para el label del juego
        '''
        count = 1
        text_list = []
        scores = self.db.fetch_query('SELECT nombre, max(puntuacion), STRFTIME("%d-%m-%Y", fecha) FROM scoreboard GROUP BY nombre ORDER BY puntuacion DESC')
        for score in scores:
            text_list.append(f"{count}.- {score[0]}: {score[1]} puntos | Fecha: {score[2]}")
            count += 1
            if count == 11:
                break
        return "\n".join(text_list)
