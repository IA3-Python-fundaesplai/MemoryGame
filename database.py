# Clase Game para controlar la lógica del juego
# Creado por: Aitor & Jon
# GitHub: https://www.github.com/aitorias | https://www.github.com/jonfdz
# Fecha creación: 2023/10/08
# Última actualización: 2023/10/16
# Versión: 1.0

import logging
import sqlite3


class Database:
    """
    Clase que proporciona métodos para ejecutar consultas, obtener resultados y cerrar la conexión a la base de datos.

    Args:
        db_name (str): El nombre del archivo de la base de datos SQLite.

    Attributes:
        conn (sqlite3.Connection): La conexión a la base de datos SQLite.
    """

    def __init__(self) -> None:
        """
        Inicializa una nueva instancia de la clase Database y establece una conexión con el archivo de base de datos SQLite especificado para crear la tabla scores.
        """
        self.DB_NAME = "scores.db"
        self.create_table()

    def create_table(self):
        connection = sqlite3.connect(self.DB_NAME)
        cursor = connection.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS scoreboard (
                        fecha TIMESTAMP PRIMARY KEY,
                        nombre TEXT,
                        puntuacion INTEGER
                        )''')
        connection.commit()
        connection.close()

    def commit_query(self, query: str, params: tuple = None) -> bool:
        """
        Ejecuta la consulta proporcionada con parámetros opcionales y confirma los cambios en la base de datos.

        Args:
            query (str): La consulta SQL a ejecutar.
            params (tuple, opcional): Los parámetros a sustituir en la consulta.

        Returns:
            bool: True si la consulta se ejecutó correctamente y se confirmaron los cambios, False en caso contrario.
        """
        try:
            connection = sqlite3.connect(self.DB_NAME)
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            cursor.close()
            return True
        except Exception as e:
            logging.error(f"Error en la base de datos: {e}")
            connection.rollback()
            return False

    def fetch_query(self, query: str, params: tuple = None) -> list:
        """
        Ejecuta la consulta proporcionada con parámetros opcionales y devuelve todas las filas obtenidas de la base de datos.

        Args:
            query (str): La consulta SQL a ejecutar.
            params (tuple, opcional): Los parámetros a sustituir en la consulta.

        Returns:
            list: Una lista de tuplas que representan las filas obtenidas de la base de datos.
        """
        try:
            connection = sqlite3.connect(self.DB_NAME)
            cursor = connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            return data
        except Exception as e:
            logging.error(f"Error en la base de datos: {e}")
            return []
