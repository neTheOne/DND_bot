"""Модуль работы с БД"""
import psycopg
import configs
import logging


def postgres_init(db_name: str) -> tuple:
    """
    Функция инициализации БД
    :param db_name: Имя БД
    :return: БД
    """
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


def get_race_info(race_id: int) -> list|tuple:
    """
    Функция для вывода инфорамции о расе
    :param race_id: race_id - id расы
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


def get_background_id() -> list|tuple:
    """
    Функция для получения background_id, race_name из таблицы background_table
    :return: background_id, background_name
    """
    conn, cursor = postgres_init(configs.DB_INFO) # подключаемся к БД
    try:
        cursor.execute('SELECT backround_id, backround_name FROM background_table')
        raw_data_background = cursor.fetchall()

        return raw_data_background

    except psycopg.Error as error:
        logging.error(f'Ошибка: {error}')

        return []
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение


def get_background_info(background_id: int) -> list|tuple:
    """
    Функция для вывода информации о предыстории
    :param background_id: background_id - id предыстории
    :return: speed, race_description, race_skill, race_name
    """
    conn, cursor = postgres_init(configs.DB_INFO)  # подключаемся к БД
    try:
        cursor.execute(
            'SELECT backround_name, stats, skills, trait_id, prefer_class_id '
            'FROM background_table '
            'WHERE backround_id = %s',
            (background_id, ))
        raw_data_background = cursor.fetchone()
        logging.debug(f"Вывод из функции get_race_info: {raw_data_background}")

        return raw_data_background

    except psycopg.Error as error:
        logging.info(f'Ошибка: {error}')

        return []
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение


def write_data(data):
    """
    Временное решения для записы данных в таблицу персонажа
    :param data: записывсемое значние
    :return: процедура
    """
    conn, cursor = postgres_init(configs.DB_MAIN)  # подключаемся к БД
    try:
        cursor.execute(
            'INSERT INTO pers_table(class_id, pers_id) VALUES (%s, 1)',
            (data, ))
        conn.commit()
        logging.debug(f"Значение добавлено {data}")
    except psycopg.Error as error:
        logging.info(f'Ошибка: {error}')
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение


def delete_data():
    conn, cursor = postgres_init(configs.DB_MAIN)  # подключаемся к БД
    try:
        cursor.execute(
            'TRUNCATE TABLE pers_table RESTART IDENTITY')
        conn.commit()
        logging.debug(f"Таблица сброшена")
    except psycopg.Error as error:
        logging.info(f'Ошибка: {error}')
    finally:
        conn.close()  # закрываем соединение
        cursor.close()  # закрываем соединение
