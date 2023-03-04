import sqlite3
import ql

try:
    sqlite_connection = sqlite3.connect('RESOURCE.db')
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS RESOURCE (
                                RESOURCE_id INTEGER PRIMARY KEY,
                                RESOURCE_NAME TEXT,
                                RESOURSE_URL TEXT ,
                                TOP_TAG TEXT,
                                BOTTOM_TAG TEXT,
                                TITLE_CUT TEXT);'''

    sqlite_create_table_query2 = '''CREATE TABLE IF NOT EXISTS ITEMS (
                                    id INTEGER PRIMARY KEY,
                                    RESOURCE_ID INTEGER,
                                    LINK TEXT ,
                                    RUSSIAN_NAME TEXT,
                                    ENGLISH_NAME TEXT,
                                    YEAR TEXT,
                                    COUNTRY TEXT,
                                    THE LEAD ROLES TEXT,
                                    FOREIGN KEY(RESOURCE_ID) REFERENCES RESOURCE(RESOURCE_id));'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    cursor.execute('''INSERT INTO RESOURCE(RESOURCE_NAME,
                                RESOURSE_URL,
                                TOP_TAG ,
                                BOTTOM_TAG ,
                                TITLE_CUT ) VALUES
    ('Онлайн-кинотеатр','https://www.kinopoisk.ru','a_class_=base-movie-main-info_link__YwtP1','span_class_=styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj',
    'span_class_=desktop-list-main-info_secondaryTitle__ighTt')

    ''')

    # cursor.execute('select*from RESOURCE')

    cursor.execute(sqlite_create_table_query2)
    cursor.executemany('INSERT INTO ITEMS VALUES(?,?,?,?,?,?,?,?)', (ql.data))
    sqlite_connection.commit()

    print("Таблица SQLite создана")
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

