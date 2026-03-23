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


def get_class_id() -> list|tuple:
    """
    Функция для получения class_id, class_name из таблицы class_table
    :return: class_id, class_name
    """
    conn, cursor = postgres_init(configs.DB_INFO) # подключаемся к БД
    try:
        cursor.execute('SELECT class_id, class_name FROM class_table')
        raw_data_class = cursor.fetchall()

        return raw_data_class

    except psycopg.Error as error:
        logging.error(f'Ошибка: {error}')

        return []
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение


def get_class_info(class_id) -> list|tuple:
    """
    Функция для вывода инфорамции о классе
    :param class_id: class_id - id класса
    :return: recommend_stats, spells, class_name, class_description, class_skills, hp_dice
    """
    conn, cursor = postgres_init(configs.DB_INFO)  # подключаемся к БД
    try:
        cursor.execute(
            'SELECT recommend_stats, spells, class_name, class_description, skills, hp_dice '
            'FROM class_table '
            'WHERE class_id = %s',
            (class_id, ))
        raw_data_class = cursor.fetchone()

        return raw_data_class

    except psycopg.Error as error:
        logging.info(f'Ошибка: {error}')

        return []
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение


def get_race_id() -> list|tuple:
    """
    Функция для получения race_id, race_name из таблицы race_table
    :return: race_id, race_name
    """
    conn, cursor = postgres_init(configs.DB_INFO) # подключаемся к БД
    try:
        cursor.execute('SELECT race_id, race_name FROM race_table')
        raw_data_race = cursor.fetchall()

        return raw_data_race

    except psycopg.Error as error:
        logging.error(f'Ошибка: {error}')

        return []
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение


def get_race_info(race_id) -> list|tuple:
    """
    Функция для вывода инфорамции о расе
    :param class_id: race_id - id расы
    :return: speed, race_description, race_skill, race_name
    """
    conn, cursor = postgres_init(configs.DB_INFO)  # подключаемся к БД
    try:
        cursor.execute(
            'SELECT speed, race_description, race_skill, race_name '
            'FROM race_table '
            'WHERE race_id = %s',
            (race_id, ))
        raw_data_race = cursor.fetchone()
        logging.debug(f"Вывод из функции get_race_info: {raw_data_race}")

        return raw_data_race

    except psycopg.Error as error:
        logging.info(f'Ошибка: {error}')

        return []
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение