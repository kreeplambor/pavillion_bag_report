import json


class get:
    # получение всех данных
    def all_data_json(self, file_name: str):
        with open('data.json', 'r') as file:
            data = file.read()
            data = json.loads(data)
        return(data)

    # получение списка площадок
    def places(self, data):
        result = list(data.keys())
        return(result)

    # проверка существования
    def is_user(self, data, user_id):
        for place in self.places(data):
            if user_id in place['users']:
                return(True)
        return(False)
