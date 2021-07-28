# Бот версия/стадия 3 (refactor)

# Импортируем логгирование и преднастройки
import logging
import settings

# Персональное импортирование
from handlers import (greet_user, talk_to_me, guess_number,
                      send_cat_picture, user_coordinates)

# Импоортим из либы тг : апдейтер, СommandHandler MessageHandler, Filters
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Логгирование сообщений в файл bot3.log, level INFO
logging.basicConfig(filename='bot3.log', level=logging.INFO)

# Создаем словарь с проксей-сервером
PROXY = {'proxy_url': settings.PROXY_URL,
         'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME,
                                  'password': settings.PROXY_PASSWORD}}


# Функция для запуска ТГ бота
def main():
    # Создаем ТГ бота, и передаем Апишку для работы
    mybot3 = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    # Используем Диспетчер mybot2.dispatcher,
    # чтобы при наступлени события вызывалась наша функция.
    dp = mybot3.dispatcher

    # Добавляем обработчик, реагирующий на /start и вызывать функцию
    dp.add_handler(CommandHandler("start", greet_user))

    # Обработчик команды guess. Игра больше меньше.
    dp.add_handler(CommandHandler("guess", guess_number))

    # Обработчик команды cat. Картинки с котиками.
    dp.add_handler(CommandHandler("cat", send_cat_picture))

    # Добавляем обработчик реагируший на строку "Показать котиков"
    dp.add_handler(MessageHandler(Filters.regex('^(Показать котика)$'),
                                  send_cat_picture))

    # Добавляем обработчик координат
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))

    # Добавляем обработчик реагирующий на текстовые сообшения
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # Запись "Бот стартовал", логгирование
    logging.info('Стартуем!!!!')

    # Отправляем ботв в ТГ за сообщениями
    mybot3.start_polling()

    # Запуск бота. Работает до принудительной осановки.
    mybot3.idle()


# Если этот файл вызвали python3 bot2.py
# то будет вызван main
# если нет, то main вызван не будет.
if __name__ == '__main__':
    main()
