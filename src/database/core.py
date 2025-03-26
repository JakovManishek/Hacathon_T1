"""
Модуль для работы с базой данных SQLite.

Содержит функции для:
- Проверки наличия пользователя
- Получения данных из таблиц
- Обновления данных
- Создания новых записей
"""

import sqlite3
from typing import Union, List, Tuple, Optional
from pathlib import Path

# Путь к БД
DB_DIR = Path(__file__).parent.parent / "database"
DB_PATH = DB_DIR / "database_hackathon.db"



def is_user_in_table(user_id: int) -> bool:
    """
    Проверяет наличие пользователя в таблице Users.
    
    Args:
        user_id (int): ID пользователя для проверки
        
    Returns:
        bool: True если пользователь существует, иначе False
    """
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute('SELECT 1 FROM Users WHERE user_id = ?', (user_id,))
        return cur.fetchone() is not None


def get_value_db(table: str, id: int) -> List[Tuple]:
    """
    Получает данные из указанной таблицы по ID.
    
    Args:
        table (str): Название таблицы ('Users' или 'Cards')
        id (int): ID для поиска
        
    Returns:
        List[Tuple]: Список кортежей с результатами запроса
        
    Raises:
        ValueError: Если передана несуществующая таблица
    """
    if table not in ("Users", "Cards"):
        raise ValueError(f"Unknown table: {table}")

    query = {
        "Users": "SELECT * FROM Users WHERE chat_id = ?",
        "Cards": "SELECT * FROM Cards WHERE user_id = ?"
    }

    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute(query[table], (id,))
        return cur.fetchall()


# def set_value_db(
#     table: str,
#     id: int,
#     new_value: Union[str, int],
#     column: Optional[str] = None
# ) -> None:
#     """
#     Обновляет значение в указанной таблице.
    
#     Args:
#         table (str): Название таблицы ('Users' или 'Cards')
#         id (int): ID записи для обновления
#         new_value (Union[str, int]): Новое значение
#         column (Optional[str]): Название столбца (None для Cards)
        
#     Raises:
#         ValueError: Если передана несуществующая таблица
#         ValueError: Для таблицы Users не указан column
#     """
#     if table not in ("Users", "Cards"):
#         raise ValueError(f"Unknown table: {table}")

#     if table == "Users" and not column:
#         raise ValueError("Column must be specified for Users table")

#     query = {
#         "Users": f"UPDATE Users SET {column} = ? WHERE chat_id = ?",
#         "Cards": "UPDATE Cards SET ? WHERE card_id = ?"
#     }

#     with sqlite3.connect(DB_PATH) as con:
#         cur = con.cursor()
#         params = (new_value, id) if table == "Users" else (id, new_value)
#         cur.execute(query[table], params)
#         con.commit()


def create_user(user_id: int, name: str) -> int:
    """
    Создает нового пользователя в таблице Users.
    
    Args:
        user_id (int): ID пользователя
        name (str): Имя пользователя
        
    Returns:
        int: ID созданной записи
    """
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Users (user_id, username) VALUES (?, ?)",
            (user_id, name)
        )
        con.commit()
        return cur.lastrowid


def create_card(
    user_id: int,
    card_name: str,
    category: str,
    cashback: float
) -> int:
    """
    Создает новую карту в таблице Cards.
    
    Args:
        user_id (int): ID пользователя-владельца
        card_name (str): Название карты
        category (str): Категория карты
        cashback (float): Размер кешбека
        
    Returns:
        int: ID созданной записи
    """
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute(
            """INSERT INTO Cards 
               (user_id, card_name, category, cashback) 
               VALUES (?, ?, ?, ?)""",
            (user_id, card_name, category, cashback)
        )
        con.commit()
        return cur.lastrowid