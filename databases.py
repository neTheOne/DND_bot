"""Модуль работы с БД"""
import psycopg
import configs


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
        print("Успешное подключение")
        return conn, cursor
    except (Exception, BaseException) as error:
        print("Ошибка подключения к Postgresql", error)
        return None, None




