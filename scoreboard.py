# Clase Scoreboard gestionar las puntuaciones del usuario.
# Creado por: Aitor & Jon
# GitHub: https://www.github.com/aitorias | https://www.github.com/jonfdz
# Fecha creación: 2023/09/22
# Última actualización: 2023/10/09
# Versión: 1.0

import art
import datetime
import json
import locale
from functools import reduce

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

    def get_actual_date(self):
        """
        Función que retorna la fecha actual formatada según el idioma del sistema
        """
        try:
            # Formatear la fecha para sistemas en inglés
            if self.language in ["en_GB", "en_US"]:
                date_format = "%A %d %B %Y"
            elif (
                self.language == "es_ES"
            ):  # Formatear la fecha para sistemas en español
                date_format = "%A %d de %B de %Y"
            else:  # Formato de fecha para cualquier otro idioma
                date_format = "%A %d %B %Y"
            locale.setlocale(locale.LC_TIME, self.language)
        except locale.Error as error:
            self.log.log_error(f"Locale error occurred: {error}")
        return datetime.datetime.now().strftime(date_format)

    def get_scores(self):
        """
        Función que carga las puntuaciones desde el archivo JSON y si no existe lo crea
        """

        scores = self.db.fetch_query("SELECT * FROM scoreboard")
        return scores

    def add_score(self, score):
        """
        Función para añadir una nueva puntuación a la database scores.db
        """
        date = self.get_actual_date()
        self.user = input("Introduzca su nombre: ").upper()
        self.score = score

        self.db.commit_query("INSERT INTO scoreboard (fecha, nombre, puntuacion) VALUES (?, ?, ?)", (datetime.datetime.now(), self.user, self.score))

        log_message = f'Puntuación {score} para el jugador {self.user} en {date} añadida correctamente.'
        self.log.log_info(log_message)

    def parse_list(self, item):
        username = item[0]
        score, date = reduce(lambda a, b: a if a[0] > b[0] else b, item[1])
        return [username, score, date]

    def print_scoreboard(self):
        """
        Funcion para printear la clasificacion ordenada en pantalla
        """
        quit = ""

        while quit == "":
            print(art.scoreboard_art)
            print("\n\n")

            scores = self.get_scores()
            parsed_scores = []
            count = 1

            parsed_scores = list(map(self.parse_list, scores.items()))

            parsed_scores.sort(key=lambda x: x[1], reverse=True)

            for user in parsed_scores:
                print(
                    f"{count}.- {user[0]}: {user[1]} puntos | Fecha: {user[2]}")
                count += 1

            quit = input("\nPulse enter para volver al menu.")
            break

scoreboard = Scoreboard()

scoreboard.print_scoreboard()