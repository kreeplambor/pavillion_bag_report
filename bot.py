import telebot
from bot_add import Markup, Functions

with open('TOKEN.txt', 'r') as f:
    TOKEN = f.read()
    bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'пиривет')

    text, lines_columns, callback_data = Functions.reg_message()
    markup = Markup.inline(lines_columns, callback_data)
    bot.send_message(message.chat.id, text, reply_markup=markup)
    return


@bot.message_handler(content_types=['text'])
def proc_text(message):
    pass


# структура mode.data
@bot.callback_query_handler(lambda call: True)
def proc_call(call):
    person_id = call.user.id
    mode, data = call.data.split('.')

    modes = {'z': [Functions.reg, (person_id, data)],
             'i': [Functions.reg, (person_id, data, True)]}

    message, lines_columns, callback_data = modes[mode]

    if not lines_columns:
        bot.editMessageText(call.message.id, text=message)
        return
    markup = Markup.inline(lines_columns, callback_data)
    bot.editMessageText(call.message.id, text=message, reply_markup=markup)
    return


def reg(message, data: str, mode: bool = False):
    mode = {False: 'zone', True: 'inst'}[mode]
    if mode is 'zone':
        text, lines_columns, callback_data = Functions.reg_message()
        markup = Markup.inline(lines_columns, callback_data)
        bot.send_message(message.chat.id, text, reply_markup=markup)
        return
    # mode is 'inst'
    text, lines_columns, callback_data = Functions.reg_message(zone=data)
    markup = Markup.inline(lines_columns, callback_data)
    bot.send_message(message.chat.id, text, reply_markup=markup)
    return
