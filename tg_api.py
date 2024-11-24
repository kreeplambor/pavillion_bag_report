import telebot
from db import get

with open('TOKEN.txt', 'r') as f:
    TOKEN = f.read()
    bot = telebot.TeleBot(TOKEN)
file_db = 'data.json'
db_data = None
in_reg = []


def get_db_data():
    global db_data
    db_data = get.all_data_json(file_db)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id

    bot.send_message(
        user_id,
        f"Приветственное сообщение {user_id}")  # привет
    if not check_reg(user_id):
        reg(user_id)


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)


# отправка сообщений
def message_sendler(user_id, text: str, markup=None):
    bot.send_message()


# проверка регистрации
def check_reg(user_id):
    if not db_data:
        get_db_data()

    result = get.is_user(db_data, user_id)
    return(result)


# регистрация
def reg(user_id):
    pass


def main():
    print('начало работы')
    bot.polling()


if __name__ == '__main__':
    main()
