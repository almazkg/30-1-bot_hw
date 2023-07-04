import sqlite3
from pathlib import Path

''' 
Подключение к базе данных 
'''
def init1():
    """
        Создание файла sqlite3
        """
    DB_NAME = 'data.sqlite3'
    DB_PATH = Path(__file__).parent.parent
    global db, cur
    db = sqlite3.connect(DB_PATH / DB_NAME)
    cur = db.cursor()

# Создание таблицы
def create_table_cars():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS dictionary (
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        price TEXT,
        description TEXT,
        link TEXT UNIQUE
    )
    """)
    db.commit()


# Вставка данных
def pop_cars(data1):
    for item in data1:
        cur.execute("""
        INSERT OR IGNORE INTO dictionary (name, price, description, link)
        VALUES (?, ?, ?, ?)
        """, (item["name"], item["price"], item["descr"], item["link"]))

    db.commit()


def get_data():
    cur.execute(
        '''
        SELECT * FROM dictionary
        '''
    )
    return cur.fetchall()


# init1()
# create_table_cars()