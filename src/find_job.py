from abc import ABC, abstractmethod
import os
import json

import requests


class Platforms(ABC):
    "Абстрактный класс"

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(Platforms):
    """Класс для получения вакансий по API с HeadHunter"""

    def __init__(self, keyword):
        self.keyword = keyword
        self.v = []

    def get_formatted_vacancies(self):
        formatted_v = []
        for vacancy in self.v:
            formatted_v.append({
                'salary_from': vacancy['salary']['from'],
                'title': vacancy['title'],
                'url': vacancy['url'],
                'description': vacancy['description'],
                'API': 'HH'
            })
        return formatted_v

    def get_vacancies(self, keyword):
        v = []
        for page in v:
            api_hh = "http://api.hh.ru/vacancies/"
            params = {
                "per_page": 100,
                "page": page,
                "keyword": self.keyword,
                "archive": False
            }

            v.extend(requests.get(api_hh, params=params).json())


class SuperJobAPI(Platforms):
    """Класс для получения вакансий по API с SuperJob"""

    def __init__(self, keyword):
        self.keyword = keyword
        self.v = []

    def get_formatted_vacancies(self):
        formatted_v = []
        for vacancy in self.v:
            formatted_v.append({
                'salary_from': vacancy['payments_from'],
                'title': vacancy['title'],
                'url': vacancy['url'],
                'description': vacancy['description'],
                'API': 'SJ'
            })

        return formatted_v

    def get_vacancies(self, keyword):
        self.v = []
        for page in self.v:
            api_sj = "https://api.superjob.ru/2.0/vacancies/"
            params = {
                "count": 100,
                "page": page,
                "keyword": self.keyword,
                "archive": False,
            }
            headers = {
                "X-Api-App-Id": os.getenv("SECRET_KEY_SJ")
            }

            self.v.extend(requests.get(api_sj, headers=headers, params=params).json())


#
class Vacancy:
    """Класс для работы с вакансиями: сравнение по з/п"""

    def __init__(self, vacancy):
        self.title = vacancy['title']
        self.url = vacancy['url']
        self.salary_from = vacancy['salary_from']
        self.description = vacancy['description']

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __str__(self):
        return f"""
{self.title}
Зарплата от {self.salary_from}"""


class JSONSaver:
    """Класс для реализации записи, удаления, сортировки полученных данных в файл"""

    def __init__(self, filename, vacancies):
        self.filename = filename
        self.create_file(vacancies)

    def create_file(self, vacancies):
        with open("filename.txt", "r", encoding="utf-8") as f:
            json.dump(vacancies, f, indent=2, ensure_ascii=False)

    def select_all(self):
        with open("filename.txt", "r", encoding="utf-8") as f:
            data = json.load(f)
        vacancy_data = [Vacancy(x) for x in data]
        return vacancy_data

    def sorted_by(self):
        vacancy_data = self.select_all()
        s = sorted(vacancy_data)
        return s
