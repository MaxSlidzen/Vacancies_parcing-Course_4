from abc import ABC, abstractmethod
import requests


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
        self._headers = {"User-Agent": "HH-User-Agent"}


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
                                headers=self._headers,
                                params={"text": keyword,
                                        "per_page": 100})
        return response.json()


class SuperJobAPI(API):
    """
    Класс для работы с API SuperJob
    """
    def __init__(self) -> None:
        """
        Инициализация класса
        """
        self._url = "https://api.superjob.ru/2.0/vacancies/"
        self._headers = {"X-Api-App-Id": "v3.r.137598076.b9969aa163487aecc9928f7cf2c0d2f4d769da7e"
                                         ".568b25124c152bd563719ca9e46a3c422787c869"}


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

