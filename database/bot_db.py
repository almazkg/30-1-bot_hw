import sqlite3

db = sqlite3.connect('bot.sqlite3')
cursor = db.cursor()


def sql_create():
    if db:
        print("База данных подключена")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fsm_anketa(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name1 TEXT,
            age INTEGER NOT NULL,
            phonetic TEXT,
            group_name TEXT
        )
        """)
    db.commit()


async def anketa_insert(data):
    data = data.as_dict()
    cursor.execute(
        "INSERT INTO fsm_anketa "
        "(name1, age, phonetic, group_name)"
        "VALUES (:name, :age, :phonetic, :group_name)",
        {'name1': data['name1'], 'age': data['age'],
         'phonetic': data['phonetic'], 'group_name': data['group_name']}
    )
    db.commit()
