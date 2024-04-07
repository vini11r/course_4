import json
from AbstractProcessingVacancies import AbstractProcessingVacancies


class Connector(AbstractProcessingVacancies):

    def __init__(self, data):
        self.data = data
        self.file = 'data/vacancies.json'

    def insert(self):
        """Добавляет данные в JSON файл"""
        with open(self.file, 'w', encoding='utf8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def search(self, query=None):
        """Фильтрует данные по ключевому слову в описании"""
        with open(self.file, 'r', encoding='utf8') as file:
            result = json.load(file)
            result_list = []
            if not query:
                return result
            else:
                for i in result:
                    if not i['snippet']['requirement']:
                        pass
                    elif query in i['snippet']['requirement']:
                        result_list.append(i)
            return result_list

    def clear(self):
        """Очищает JSON файл"""
        with open(self.file, 'w', encoding='utf8'):
            pass
