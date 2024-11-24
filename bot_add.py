from telebot import types
from json import dumps
from file_classes import Person, Zone


# создание клавиатур
class Markup:
    # создание обычной клавиатуры
    def reply(self, lines_columns: list):
        keyboard = types.ReplyKeyboardMarkup(resize=True)

        for line in lines_columns:
            if line is not list:
                button = types.KeyboardButton(str(line))
                keyboard.add(button)
                break
            for column in line:
                buttons = []
                buttons.append(types.KeyboardButton(str(column)))
                keyboard.add(buttons)

        return(keyboard)

    # создание inline клавиатуры
    def inline(self, lines_columns: list, callback_data: list):
        keyboard = types.InlineKeyboardMarkup()
        line_count = len(lines_columns)

        for line_ind in range(line_count):
            line = lines_columns[line_ind]

            if lines_columns[line_ind] is not list:
                callback = callback_data[line_ind]
                callback = dumps(callback)

                button = types.InlineKeyboardButton(
                    str(lines_columns[line_ind]),
                    callback_data=callback)
                keyboard.add([button])
                break

            buttons = []
            column_count = len(line)
            for column_ind in range(column_count):
                column = line[column_ind]
                buttons.append(types.InlineKeyboardButton(str(column)))
            keyboard.add(buttons)

        return(keyboard)


class Functions:
    # запоминаем данные человека
    def reg(self, person_id, data: str, obj: bool = False):
        if obj is True:
            zone = Person.give(person_id, 'zone')
            instal = data
            Person.delete(person_id)
            Person.add(person_id, zone, instal)
            return('Вы зарегистрированы', None, None)

        instal = None
        zone = data
        return(self.reg_messasge(zone))

    # регистрация
    def reg_messasge(self, zone=None):
        # даём выбрать зону
        if not zone:
            zones = Zone.view_zones()

            message = 'выберите зону'
            lines_columns = zones
            callback_data = [[False, zone] for zone in zones]

            return(message, lines_columns, callback_data)

        # даём выбрать инсталяцию
        instals = Zone.view_instals(zone)

        message = 'выберите инсталяцию'
        lines_columns = instals
        callback_data = [['reg', [zone, instal]]
                         for instal in instals]

        return(message, lines_columns, callback_data)
