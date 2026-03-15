from databases import postgres_init, clean_table, add_info_table
import psycopg
import configs
import importer


def test_func_1():
    conn, cursor = postgres_init(configs.DB_NAME) # подключаемся к БД
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


def test_func_2(column, table):
    conn, cursor = postgres_init(db_name='dnd_tgbot_info') # подключаемся к БД
    try:
        cursor.execute(f'SELECT {column} FROM {table}')
        data = cursor.fetchone() # получаем первое найденное значение (из БД мы получаем кортеж)
        conn.commit() # сохраняем изменения, запись и т.д
        class_names = [row[0] for row in data]

        return class_names # возвращаем нужное значение

    except psycopg.Error as error:
        print(f'Ошибка: {error}')
    finally:
        conn.close() # закрываем соединение
        cursor.close() # закрываем соединение


#clean_table("class_table")
json_data = json_loader.read_js("json\data.json")
add_info_table(json_data)
