# Clase Scoreboard para guardar el registro de puntuaciones del usuario.
# Creado por: Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/09/22
# Última actualización: 2023/10/08
# Versión: 1.0

import datetime
import locale
import logging
import os
import pwd
import sqlite3

from database import Database 


class Scoreboard:
    """
    Clase para gestionar el registro de puntuaciones de los usuarios en un juego.

    Attributes:
        user (str): El nombre de usuario del jugador.
        language (str): El idioma del sistema.
        scores (dict): Un diccionario que almacena las puntuaciones del jugador.

    Methods:
        __init__: Constructor de la clase.
        __del__: Destructor de la clase.
        __str__: Devuelve una representación en cadena de la instancia.
        get_player_username: Obtiene el nombre de usuario del sistema.
        get_actual_date: Obtiene la fecha actual formateada según el idioma del sistema.
        get_scores: Carga las puntuaciones del jugador desde la base de datos.
        add_score: Añade una nueva puntuación al registro del jugador.
    """
    def __init__(self, db_name='scores.db') -> None:
        """
        Constructor de la clase Scoreboard
        """
        user = self.get_player_username()
        self.user = user
        self.language = locale.getdefaultlocale()[0]
        self.scores = {}

        self.db_name = db_name

    def __str__(self) -> str:
        """
        Representación de una instancia de la clase Scoreboard
        """
        return f'Jugador: {self.user} | Puntuaciones: {self.scores}'

    def get_player_username(self) -> str:
        """
        Obtiene el nombre de usuario de inicio de sesión del sistema para utilizarlo como nombre de usuario del juego.
        """
        # Obtenemos el usuario del sistema
        try:
            username = os.getlogin()
        except OSError:
            '''
            Si se usa una máquina virtual o WSL en Windows, os.getlogin() da error.
            Para ello, usamos el módulo de Python pwd para obtener el nombre del usuario de la máquina.
            '''
            username = pwd.getpwuid(os.getuid()).pw_name
        return f'{username}'

    def get_actual_date(self) -> str:
        """
        Obtiene la fecha actual formateada según el idioma del sistema.
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

    def get_scores(self) -> list:
        """
        Carga las puntuaciones del jugador desde la base de datos.
        """
        try:
            with Database(self.db_name) as db:
                db.execute_query('''
                    SELECT username, score, date
                    FROM scores
                    WHERE username = ?
                ''', (self.user,))
                self.scores = db.fetch_all('SELECT username, score, date FROM scores WHERE username = ?', (self.user,))
        except Exception as error:
            logging.error(f'Error al recibir las puntuaciones de la base de datos: {error}')

    def add_score(self, score: int) -> None:
        """
        Añade una nueva puntuación al registro del jugador.
        """
        try:
            date = self.get_actual_date()
            with Database(self.db_name) as db:
                db.execute_query('''
                    INSERT INTO scores (username, score, date)
                    VALUES (?, ?, ?)
                ''', (self.user, score, date))
        except Exception as error:
            logging.error(f'Error while adding score: {error}')
