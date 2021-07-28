# Мои настройки
import settings

# Рандом импортим
from random import choice, randint

# Импортим эмодзи
from emoji import emojize

# Импортируем класс для создания клавиатуры
from telegram import ReplyKeyboardMarkup, KeyboardButton


# Функция для работы со смайлами
def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


# Фунция делающая вычисления в игре
def play_random_numbers(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if user_number > bot_number:
        message = f"Ваше число {user_number}, моё {bot_number}, Шекели ваши!"
    elif user_number == bot_number:
        message = f"Ваше число {user_number}, моё {bot_number}, Ничья!"
    else:
        message = f"Ваше число {user_number}, моё {bot_number}, \
давайте Ваши Шекели любезный!"
    return message


# Функция отрисовки клавиатуры
def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Показать котика', KeyboardButton('Мои коорды', request_location=True)]
        ])
