"""
Модуль для работы с базой данных SQLite.

Содержит функции для:
- Создания структуры базы данных
- Инициализации таблиц
"""

import sqlite3


def create_db(db_name: str = 'database_hackathon.db') -> bool:
    """
    Создает базу данных и таблицы, если они не существуют.
    
    Args:
        db_name (str): Название файла базы данных
        
    Returns:
        bool: True если создание прошло успешно, False при ошибке
    """
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            
            # Создание таблицы Users
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT
                )
            """)
            
            # Создание таблицы Cards
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Cards (
                    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    card_name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    cashback REAL NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES Users (user_id)
                )
            """)
            
            # Создание индексов для ускорения запросов
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_cards_user_id 
                ON Cards (user_id)
            """)
            
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_cards_category 
                ON Cards (category)
            """)
            
            conn.commit()
            return True
            
    except sqlite3.Error as ex:
        print(f"[ОШИБКА БАЗЫ ДАННЫХ] {ex}")
        return False
    except Exception as ex:
        print(f"[НЕИЗВЕСТНАЯ ОШИБКА] {ex}")
        return False


if __name__ == "__main__":
    if create_db():
        print("База данных успешно создана")
    else:
        print("Произошла ошибка при создании базы данных")