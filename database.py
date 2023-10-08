# Clase Database para gestionar la base de datos
# Creado por: Aitor
# GitHub: https://www.github.com/aitorias
# Fecha creación: 2023/10/08
# Última actualización: 2023/10/08
# Versión: 1.0

import sqlite3

class Database:
    """
    Clase que proporciona métodos para ejecutar consultas, obtener resultados y cerrar la conexión a la base de datos.

    Args:
        db_name (str): El nombre del archivo de la base de datos SQLite.

    Attributes:
        conn (sqlite3.Connection): La conexión a la base de datos SQLite.
        cursor (sqlite3.Cursor): El objeto cursor utilizado para ejecutar consultas y obtener resultados.
    """

    def __init__(self, db_name: str) -> None:
        """
        Inicializa una nueva instancia de la clase Database y establece una conexión con el archivo de base de datos SQLite especificado.

        Args:
            db_name (str): El nombre del archivo de la base de datos SQLite.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute_query(self, query: str, params: tuple = None) -> bool:
        """
        Ejecuta la consulta proporcionada con parámetros opcionales y confirma los cambios en la base de datos.

        Args:
            query (str): La consulta SQL a ejecutar.
            params (tuple, opcional): Los parámetros a sustituir en la consulta.

        Returns:
            bool: True si la consulta se ejecutó correctamente y se confirmaron los cambios, False en caso contrario.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error en la base de datos: {e}")
            self.conn.rollback()
            return False

    def fetch_all(self, query: str, params: tuple = None) -> list:
        """
        Ejecuta la consulta proporcionada con parámetros opcionales y devuelve todas las filas obtenidas de la base de datos.

        Args:
            query (str): La consulta SQL a ejecutar.
            params (tuple, opcional): Los parámetros a sustituir en la consulta.

        Returns:
            list: Una lista de tuplas que representan las filas obtenidas de la base de datos.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error en la base de datos: {e}")
            return []

    def close(self):
        """
        Cierra la conexión a la base de datos.
        """
        self.conn.close()
