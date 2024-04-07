import requests
from AbstractAPI import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword):
        """Метод для получения списка вакансий с hh.ru по запросу пользователя"""
        self.params['text'] = keyword
        while self.params.get('page') != 10:
            response = requests.get(self.url, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
            return self.vacancies


a = HeadHunterAPI()
b = a.get_vacancies('python')
