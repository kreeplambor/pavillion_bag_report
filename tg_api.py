import telebot

with open('TOKEN.txt', 'r') as f:
    TOKEN = f.read()
    bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Приветственное сообщение")


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)


def message_sendler():
	pass


def main():
    print('начало работы')
    bot.polling()


if __name__ == '__main__':
    main()
