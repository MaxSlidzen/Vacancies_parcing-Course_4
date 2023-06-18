from abc import ABC, abstractmethod
import requests
import os


class API(ABC):
    """
    Абстрактный класс для работы с API
    """
    @abstractmethod
    def get_vacancies(self, keyword: str) -> dict:
        """
        Возвращает список вакансий по заданному ключу
        :param keyword: ключ для поиска
        :return: список вакансий
        """
        pass


class HeadHunterAPI(API):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self) -> None:
        """
        Инициализация класса
        """
        self._url = "https://api.hh.ru/vacancies/"


    def __repr__(self) -> str:
        """
        Возвращает строковое представление класса для разработчика
        :return: строковое представление класса
        """
        return f"{self.__class__.__name__}()"


    def __str__(self) -> str:
        """
        Возвращает строковое представление класса для пользователя
        :return: строковое представление класса
        """
        return "HeadHunter API"


    def get_vacancies(self, keyword: str) -> dict:
        """
        Возвращает список вакансий по заданному ключу
        :param keyword: ключ для поиска
        :return: список вакансий
        """
        response = requests.get(f"{self._url}",
                                params={"text": keyword,
                                        "per_page": 100})
        return response.json()


class SuperJobAPI(API):
    """
    Класс для работы с API SuperJob
    """

    API_KEY = os.getenv('SJ_SECRET_KEY')

    def __init__(self) -> None:
        """
        Инициализация класса
        """
        self._url = "https://api.superjob.ru/2.0/vacancies/"
        self._headers = {"X-Api-App-Id": self.API_KEY}


    def __repr__(self) -> str:
        """
        Возвращает строковое представление класса для разработчика
        :return: строковое представление класса
        """
        return f"{self.__class__.__name__}()"


    def __str__(self) -> str:
        """
        Возвращает строковое представление класса для пользователя
        :return: строковое представление класса
        """
        return "SuperJob API"


    def get_vacancies(self, keyword: str) -> dict:
        """
        Возвращает список вакансий по заданному ключу
        :param keyword: ключ для поиска
        :return: список вакансий
        """
        response = requests.get(f"{self._url}",
                                headers=self._headers,
                                params={"keyword": keyword,
                                        "count": 100})
        return response.json()
