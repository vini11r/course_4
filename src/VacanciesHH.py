class VacanciesHH:

    def __init__(self, data):
        self.name = data['name']
        self._salary = data['salary']
        self.url = data['url']
        self.snippet = data['snippet']

    @property
    def salary_from(self):
        """Возвращает нижнюю границу зарплаты"""
        if self._salary and self._salary.get('from'):
            return self._salary.get('from')
        else:
            return 0

    @property
    def salary_to(self):
        """Возвращает верхнюю границу зарплаты"""
        if self._salary and self._salary.get('to'):
            return self._salary.get('to')
        else:
            return 0

    @property
    def salary_currency(self):
        """Возвращает нижнюю границу зарплаты"""
        if self._salary and self._salary.get('currency'):
            return self._salary.get('currency')
        else:
            return 'Не указана'

    def __lt__(self, other):
        """Метод для операции сравнения «меньше»"""
        return self.salary_to < other.salary_to

    def __gt__(self, other):
        """Метод для операции сравнения «больше»"""
        return self.salary_to > other.salary_to

    def __str__(self):
        """Вывод для пользователя"""
        return (f"{self.name}; Зарплата от {self.salary_from} до {self.salary_to} {self.salary_currency};"
                f"{self.snippet['requirement']}; {self.snippet['responsibility']}; {self.url}")

    def __repr__(self):
        """Вывод информации для отладки"""
        return f"{self.__class__.__name__} ({self.name}, {self._salary}, {self.snippet}, {self.url})\n"
