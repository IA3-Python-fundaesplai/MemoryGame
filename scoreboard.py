# Clase Scoreboard para guardar el registro de puntuaciones del usuario.
# Creado por Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/22
# Última actualización: 2023/09/29
# Versión: 1.0

import datetime
import json
import locale
import logging
import os


class Scoreboard:
    def __init__(self):
        """
        Constructor de la clase Scoreboard
        """
        user = self.get_player_username()
        self.user = user
        self.language = locale.getdefaultlocale()[0]
        self.scores = {}

    def __str__(self):
        """
        Representación de una instancia de la clase Scoreboard
        """
        return f'Jugador: {self.user} | Puntuaciones: {self.scores}'

    def get_player_username(self):
        """
        Función que retorna el nombre de usuario de inicio de sesión del sistema 
        para utilizarlo como username del juego.
        """
        # Obtenemos el usuario del sistema
        try:
            username = os.getlogin()
        except OSError:
            '''
            Si se usa una máquina virtual o WSL en Windows, os.getlogin() da error.
            Para ello, usamos el módulo de Python pwd para obtener el nombre del usuario de la máquina.
            '''
            username = input("Introduzca su nombre: ")
        return f'{username}'

    def get_actual_date(self):
        """
        Función que retorna la fecha actual formatada según el idioma del sistema
        """
        try:
            # Formatear la fecha para sistemas en inglés
            if self.language in ['en_GB', 'en_US']:
                date_format = '%A %d %B %Y'
            elif self.language == 'es_ES':  # Formatear la fecha para sistemas en español
                date_format = '%A %d de %B de %Y'
            else:  # Formato de fecha para cualquier otro idioma
                date_format = '%A %d %B %Y'
            locale.setlocale(locale.LC_TIME, self.language)
        except locale.Error as error:
            logging.error(f'Locale error occurred: {error}')
        return datetime.datetime.now().strftime(date_format)

    def get_scores(self):
        """
        Función que carga las puntuaciones desde el archivo JSON
        """
        try:
            with open(f'{self.user}-scores.json', 'r') as file:
                self.scores = json.load(file)
        except FileNotFoundError as error:
            self.scores = []
            logging.error(f'File not found error: {error}')

    def save_scores(self):
        """
        Función que guarda las puntuaciones en el archivo JSON
        """
        with open(f'{self.user}-scores.json', 'w', encoding='UTF-8') as file:
            json.dump(self.scores, file, ensure_ascii=False)

    def add_score(self, score):
        """
        Función para añadir una nueva puntuación al scoreboard
        """
        try:
            date = self.get_actual_date()
            user_scores = self.scores.get(self.user, [])
            user_scores.append((score, date))
            self.scores[self.user] = user_scores
            self.save_scores()
        except Exception as error:
            logging.error(f'Error while adding score: {error}')
