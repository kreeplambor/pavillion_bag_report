import json
import os


# работа с файлом people.json
class File:
    # чтение
    def read(self):
        self.check_exists()
        with open('people.json', 'r') as f:
            content = f.read()
        content = json.loads(content)
        return(content)

    # запись
    def write(self, data):
        with open('people.json', 'w') as f:
            data = json.dumps(data)
            f.write(data)

    # проверка существования
    def check_exists(self):
        if not os.path.exists('people.json'):
            self.write(json.dumps({}))


# работа с людьми
class Person:
    # Добавление человека
    def add(self, person_id, zone, inst):
        if self.check_exists(person_id):
            return("person in zone")
        data = File.read()
        data[person_id] = [zone, inst]
        File.write(data)
        return

    #
    def give(self, person_id, obj):
        data = File.read()
        zone, instal = data[person_id]

        g = {'zone': zone, "instal": instal, 'all': [zone, instal]}
        return(g[obj])

    # Удаление человека
    def delete(self, person_id):
        if not self.check_exists(person_id):
            return("person not exists")
        data = File.read()
        data.pop(person_id)
        File.write(data)

    # Проверка существования
    def check_exists(self, person_id):
        data = File.read()
        return(person_id in data)


# работа с зоной
class Zone:
    # чтение файла
    def read_file(self):
        with open('zones.json', 'r') as f:
            content = f.read()
            content = json.loads(content)
            return(content)

    # Показать зоны
    def view_zones(self):
        data = self.read_file()
        data = data.keys()
        data = list(data)
        return(data)

    # Показать инсталяции
    def view_instals(self, zone):
        data = self.read_file()
        data = data[zone]
        data = list(data)
        return(data)

    # Статус инсталяции
    def status(self, zone, inst):
        people_file = File.read()
        value = [zone, inst]
        values = people_file.values()
        keys = people_file.keys()

        if value not in values:
            return(False)

        index = list(values).index(value)
        person = keys[index]

        return("Zone assigned to a ", person)
