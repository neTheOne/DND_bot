import telebot
import configs
import keyboards

bot = telebot.TeleBot(configs.TOKEN)

# TODO: Тут я вызываю функцию настройки лога


@bot.message_handler(commands=['start'])
def text(message):
    user_first_name = message.from_user.first_name
    bot.send_message(chat_id=message.chat.id,
                     text=f'Hello {user_first_name}!!!!', reply_markup=keyboards.main_menu())


@bot.message_handler(content_types=['text'])
def new_pers_func(message):
    user_id = message.from_user.id
    if message.text == "Создать персонажа":
        bot.send_message(chat_id=message.chat.id,
                         text='Создаю', reply_markup=keyboards.back_button())
    elif message.text == "Мои персонажи":
        bot.send_message(chat_id=message.chat.id,
                         text='Иди-ка пока нахуй', reply_markup=keyboards.back_button())


@bot.callback_query_handler()
def back_btn(call):
    user_id = call.from_user.id
    bot.send_message(chat_id=call.message.chat.id,
                     text='Бро, хорошо. Давай вернмся на шаг назад', reply_markup=keyboards.main_menu())


@bot.message_handler(content_types=['sticker'])
def text(message):
    print(message)
    bot.send_message(chat_id=message.chat.id,
                     text='О, Это стикер, Скебоб')

bot.polling()
# TODO: Разобраться, как работает стандратная библеотека Logging, прописать логи разных уровней.
'''
- Создать файл logs.py
- В нем создать функцию инициализатора лога
- В ней настроить лог
- В main.py вызвать функцию настройки
- Я великолепен 
'''
# TODO: Все чувствительные данные перенести в конфиг
# TODO: Название DB вынести в конфиг, в функциях вызывать переменную из конфига
# TODO: Переименовать модули согласно, PEP8
# TODO: Прочитать любые десять статей в PEP8 и рассказать Саше
# TODO: Создать файлик test.py  перенести туда все дерьмо
# TODO: Дозаполнить базу данных
# TODO: В разделе создать персонажа выполнить следующий скрипт
"""
- Подключиться к БД
- Из таблицы достать все классы
- Сделать массив со всеми классами
- Передать массив в клавиатуру и сдедать по кнопке с каждым классом
- Вывести nline клаввиатуру, где каждая кнопка имя класса, а collback формате class_42
- В декоратаре обработки callbackов
"""
# TODO: прочитатиь по ссылке ниже
"""
https://ru.wikipedia.org/wiki/%D0%9D%D1%83%D0%BC%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B9_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F
"""