from abc import ABC, abstractmethod
import os
import json

import requests


class Platforms(ABC):
    """Абстрактный класс для работы с API платформ"""
    api_hh = "http://api.hh.ru/"
    api_sj = "http://api.superjob.ru/"

    # X-Api-App-Id = os.getenv("SECRET_KEY_SJ")
    def __init__(self):
        super().__init__()


class VakanciesJson(ABC):
    """Класс для реализации записи, удаления, сортировки полученных данных в файл"""

    def __init__(self):
        super().__init__()

    def to_json(self):  # Запись полученных данных
        with open("filename.txt", "w", encoding="utf-8") as f:
            json.dump(self.__dict__, f, indent=2, ensure_ascii=False)

    def change_json(self, item):  # Удаление
        with open("filename.txt", "a", encoding="utf-8") as f:
            for item in f:
                del "filename.txt"[item]


class HeadHunterAPI(Platforms, VakanciesJson):
    """Класс для получения вакансий по API с HeadHunter"""

    def get_vacancies(self):
        response = requests.get("http://api.hh.ru/vacancies")

        print(response.text)


class SuperJobAPI(Platforms):
    """Класс для получения вакансий по API с SuperJob"""

    def get_vacancies(self):
        response = requests.get("http://api.superjob.ru/vacancies")
        print(response.text)


class Vacancies:
    """Класс для работы с вакансиями"""

    def __init__(self, name, url, pay, description):
        self.name = name
        self.url = url
        self.pay = pay
        self.description = description

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass
