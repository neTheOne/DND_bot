"""Модуль работы с БД"""
import psycopg


def postgres_init(db_name: str):
    try:
        conn = psycopg.connect(
            dbname=db_name,
            user="postgres",
            password="Sirden2003",
            host="127.0.0.1",
            port="5432"
        )
        cursor = conn.cursor()
        print("Успешное подключение")
        return conn, cursor
    except (Exception, BaseException) as error:
        print("Ошибка подключения к Postgresql", error)
        return None, None

def test_func_1():
    conn, cursor = postgres_init(db_name='dnd_tgbot_info') # подключаемся к БД
    try:
        cursor.execute(
            'INSERT INTO test_table (test, test1) ' # записываем в таблицу с именем таким то (в столбцы такие-то)
            'VALUES (%s, %s);', # по сути "заглушки" чтобы не было sql инъекция (должны соответствовать количеству передаваемых значений)
            (200, "test1",)
        )
        conn.commit() # сохраняем изменения, запись и т.д
        print('Данные пользователя успешно сохранены в таблицу имя_таблицы')
    except psycopg.Error as error:
        print(f'Ошибка записи в таблицу имя_таблицы: {error}')
    finally:
        conn.close() # закрываем соединение
        cursor.close() # закрываем соединение


def test_func_2():
    conn, cursor = postgres_init(db_name='dnd_tgbot_info') # подключаемся к БД
    try:
        cursor.execute('SELECT name FROM test_table WHERE test = %s', (100,))
        data = cursor.fetchone() # получаем первое найденное значение (из БД мы получаем кортеж)
        conn.commit() # сохраняем изменения, запись и т.д
        return data[0] # возвращаем нужное значение
    except psycopg.Error as error:
        print(f'Ошибка: {error}')
    finally:
        conn.close() # закрываем соединение
        cursor.close() # закрываем соединение

print(test_func_2())
