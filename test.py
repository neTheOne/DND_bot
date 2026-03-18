from databases import postgres_init
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

''' # - Сань, скажи как правильно
    elif "back" in callback_info:
        step -= 1
        if step == 0:
            bot.send_message(chat_id=call.chat.id,
                            text='Выберите класс', reply_markup=keyboards.class_review_keyboard())
        elif step == 1:
            bot.send_message(chat_id=call.message.chat.id,
                            text=f"Вы выбрали класс {class_data[2]}. Вывести информацию о нем?",
                            reply_markup=keyboards.class_info_keyboard())
    elif "full_info" in callback_info:
        step += 1
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Название класса: {class_data[2]}\n"
                              f"Рекомендованная характеристика: {class_data[0]}\n"
                              f"Умения класса: {class_data[4]}\n"
                              f"Кость хитов класса: {class_data[5]}"
                              f"Описание класса: {class_data[3]}",
                         reply_markup=keyboards.back_keyboard())
    elif "forward" in callback_info:
        bot.send_message(chat_id=call.chat.id,
                         text='Иди-ка пока нахуй', reply_markup=keyboards.back_keyboard())
    '''