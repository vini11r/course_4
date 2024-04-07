from src.HeadHunterAPI import HeadHunterAPI
from src.Connector import Connector
from src.VacanciesHH import VacanciesHH


def user_interactions():
    user_input = input('Добро пожаловать. Введите Ваш запрос:  ')

    vacanciesAPI = HeadHunterAPI().get_vacancies(user_input)
    connector = Connector(vacanciesAPI)
    connector.insert()

    user_query = input(
        'Введите ключевое слово для фильтрации вакансий по описанию или нажмите Enter чтоб пропустить:  ')
    filter_vacancies = connector.search(user_query)

    vacancies_list = []
    for i in filter_vacancies:
        vacancies_list.append(VacanciesHH(i))

    sort_vacancies = sorted(vacancies_list, reverse=True)

    n = int(input('Введите число вакансий для вывода:  '))
    for i in sort_vacancies[:n]:
        print(i)

    user_del = int(input('Желаете удалить данные о вакансиях? Да: введите 1, Нет: введите 0   '))
    if user_del == 1:
        connector.clear()
    else:
        pass


if __name__ == '__main__':
    user_interactions()
