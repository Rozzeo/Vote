
import sqlite3

# Создаем или подключаемся к базе данных SQLite
conn = sqlite3.connect('my_database.db')

# Создаем курсор (объект, который используется для выполнения SQL-запросов)
cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Вставляем данные в таблицу
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Yair Lapid', 59))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Benjamin Netanyahu', 73))

# Сохраняем изменения
conn.commit()

# Выполняем SQL-запрос для выборки данных
cursor.execute('SELECT * FROM users')

# Получаем все строки результата
rows = cursor.fetchall()

# Выводим результат
for row in rows:
    print(row)

# Закрываем соединение с базой данных
conn.close()


'''
import sqlite3

# Создаем или подключаемся к базе данных SQLite
conn = sqlite3.connect('my_d.db')

# Создаем курсор (объект, который используется для выполнения SQL-запросов)
cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''

''')

# Вставляем данные в таблицу
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Yair lapid', ))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Benjamin Netanyahu', 73))

# Сохраняем изменения
conn.commit()

# Выполняем SQL-запрос для выборки данных
cursor.execute('SELECT * FROM users')

# Получаем все строки результата
rows = cursor.fetchall()

# Выводим результат
for row in rows:
    print(row)

# Закрываем соединение с базой данных
conn.close()
'''








'''import sqlite3


class MyLib:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)

    def close(self):
        if self.connection:
            self.connection.close()

    # def show_table(self, table):
       """ self.cursor.execute(f"SELECT * FROM {table}")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def count_rows(self, table):
        self.cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = self.cursor.fetchone()[0]
        return count

    def query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print("Error executing query:", e)
            return False

    def query_update(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.rowcount
        except sqlite3.Error as e:
            print("Error executing query:", e)
            return 0

    def query_column_int(self, query, column):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            if result:
                return result[0]
            return -1
        except sqlite3.Error as e:
            print("Error executing query:", e)
            return -1

    def query_column_double(self, query, column):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            if result:
                return result[0]
            return -1.0
        except sqlite3.Error as e:


def password_to_hash(pass):
    return
    pass  # Replace with actual password hashing code'''
