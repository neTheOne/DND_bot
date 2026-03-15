"""Модуль работы с БД"""
import psycopg
import configs
import logging
import logs
import importer
import json

logs.log_init()

def postgres_init(db_name: str):
    try:
        conn = psycopg.connect(
            dbname=db_name,
            user=configs.USER,
            password=configs.PASSWORD,
            host=configs.HOST,
            port=configs.PORT
        )
        cursor = conn.cursor()
        logging.info("Успешное подключение")
        return conn, cursor
    except (Exception, BaseException) as error:
        logging.info(f"Ошибка подключения {error}")
        return None, None

'''
def clean_table(table_name):
    conn, cursor = postgres_init(configs.DB_NAME)  # подключаемся к БД
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


def add_info_table(json):
    conn, cursor = postgres_init(configs.DB_NAME)  # подключаемся к БД
    try:
        for row in json["class_table"]:
            cursor.execute(
                """
                INSERT INTO classes (
                    id,
                    recommended_stat,
                    spells,
                    class_name,
                    description,
                    hp_dice,
                    skills
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                    int(row["class_id"]),
                    row.get("recommended_stat"),
                    [int(x) for x in row.get("spells", [])],
                    row.get("class_name"),
                    row.get("description"),
                    row.get("hp_dice"),
                    json.dumps(row.get("class_skills", {}))
                )
            conn.commit()
            logging.info("Данные успешно добавлены")
    except psycopg.Error as error:
        logging.error(f"Ошибка заполнения таблицы: {error}")
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение


def get_info_table(column, table):
    conn, cursor = postgres_init(configs.DB_NAME) # подключаемся к БД
    try:
        cursor.execute(f'SELECT {column} FROM {table}')
        raw_data = cursor.fetchone() # получаем первое найденное значение (из БД мы получаем кортеж)
        data = [row[0] for row in raw_data]

        return data # возвращаем нужное значение

    except psycopg.Error as error:
        logging.info(f'Ошибка: {error}')
    finally:
        conn.close() # закрываем соединение
        cursor.close() # закрываем соединение
'''

def get_class_info():
    """
    Функция для получения class_id, class_name из таблицы class_table
    :return: class_id, class_name
    """
    conn, cursor = postgres_init(configs.DB_INFO_NAME) # подключаемся к БД
    try:
        cursor.execute('SELECT class_id, class_name FROM class_table')
        raw_data_class = cursor.fetchall()

        return raw_data_class

    except psycopg.Error as error:
        logging.info(f'Ошибка: {error}')
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение


def get_class_info(class_id):
    """
    Функция для вывода инфорамции о классе
    :param class_id: class_id - id класса
    :return: recommend_stats, spells, class_name, class_description, class_skills, hp_dice
    """
    conn, cursor = postgres_init(configs.DB_INFO_NAME)  # подключаемся к БД
    try:
        cursor.execute(
            'SELECT recommend_stats, spells, class_name, class_description, class_skills, hp_dice '
            'FROM class_table '
            'WHERE class_id = %s',
            (class_id, ))
        raw_data_class = cursor.fetchone()

        return raw_data_class

    except psycopg.Error as error:
        logging.info(f'Ошибка: {error}')
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение