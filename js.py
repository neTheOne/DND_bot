import json
import logging

from databases import postgres_init
import psycopg
import configs

def read_js(filepath):
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return data

def clean_table(table_name):
    conn, cursor = postgres_init(configs.DB_NAME) # подключаемся к БД
    try:
        cursor.execute(
            f'TRUNCATE TABLE {table_name} RESTART IDENTITY'  # отчищаем таблицу
        )
        conn.commit()  # сохраняем изменения, запись и т.д
        logging.info(f"{table_name} успешно отчищена")
    except psycopg.Error as error:
        logging.error(f"Ошибка удаления таблицы: {error}")
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение


def add_info_table(table_name, json):
    conn, cursor = postgres_init(configs.DB_NAME)  # подключаемся к БД

    try:
        cursor.execute(
            f'INSERT INTO {table_name} ({}) ' # записываем в таблицу с именем таким то (в столбцы такие-то)
            'VALUES (%s, %s);', # по сути "заглушки" чтобы не было sql инъекция (должны соответствовать количеству передаваемых значений)
            (200, "test1",)
        )
    except psycopg.Error as error:
        logging.error(f"Ошибка удаления таблицы: {error}")
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение
