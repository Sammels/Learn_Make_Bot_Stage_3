# Поиск файлов по шаблону
from glob import glob

# Импорт из рандома: рандинт и чойс
from random import choice

# Импортим из ютился что перенесли.
from utills import get_smile, play_random_numbers, main_keyboard


# Функция приветствия + Эмодзи.
def greet_user(update, context):
    print("Вызван /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    # Добавляем клавиатуру сюда
    update.message.reply_text(
        f"Доброго денечка {context.user_data['emoji']}",
        reply_markup=main_keyboard()
    )


# Функция отзеркаливания сообщения
def talk_to_me(update, context):
    print("Простое сообщение ")
    text = update.message.text
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"ты потерял {text}{context.user_data['emoji']}",
                              reply_markup=main_keyboard()
                              )


# Функция Игры в числа
def guess_number(update, context):
    print(context.args)
    if context.args:
        # Проверка: Целои ли число ?
        try:
            user_number = int(context.args[0])
            # Тут дальше будет игровая логика по генерированию механики игры.
            message = play_random_numbers(user_number)

        except (TypeError, ValueError):
            message = "Таки введите целое число, любезный"

    else:
        message = "Таки введите число, любезнейший"
    update.message.reply_text(message, reply_markup=main_keyboard())


# Функция Отправки котиков
def send_cat_picture(update, context):
    print("вызываю котиков /cat")

    # Получаем список всех картинок
    cat_photos_list = glob('picture/cat*.jp*g')

    # Выбираем случайную картинку
    cat_pic_filename = choice(cat_photos_list)

    # Отправка картинки пользователю
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'),
                           reply_markup=main_keyboard()
                           )


# Функция пользовательских координат
def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
        )
