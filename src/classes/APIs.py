from abc import ABC, abstractmethod
import requests
import os


class API(ABC):
    """
    Абстрактный класс для работы с API
    """

    @abstractmethod
    def get_vacancies(self) -> list:
        """
        Возвращает список вакансий
        :return: список вакансий
        """
        pass


class HeadHunterAPI(API):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, keyword) -> None:
        """
        Инициализация класса по заданному ключу
        :param keyword: ключ для поиска вакансий HeadHunter
        """
        self.__url = "https://api.hh.ru/vacancies/"
        self.__params = {"text": keyword, "per_page": 100}

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

    def get_vacancies(self) -> dict:
        """
        Возвращает список вакансий по заданному ключу
        :return: список вакансий
        """
        response = requests.get(f"{self.__url}",
                                params=self.__params)
        return response.json()


class SuperJobAPI(API):
    """
    Класс для работы с API SuperJob
    """

    API_KEY = os.getenv('SJ_SECRET_KEY')

    def __init__(self, keyword: str) -> None:
        """
        Инициализация класса по заданному ключу
        :param keyword: Ключ для поиска вакансий SuperJob
        """
        self.__url = "https://api.superjob.ru/2.0/vacancies/"
        self.__headers = {"X-Api-App-Id": self.API_KEY}
        self.__params = {"keyword": keyword, "count": 100}

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

    def get_vacancies(self) -> dict:
        """
        Возвращает список вакансий по заданному ключу
        :return: список вакансий
        """
        response = requests.get(f"{self.__url}",
                                headers=self.__headers,
                                params=self.__params)
        return response.json()
