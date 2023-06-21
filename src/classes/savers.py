import json
from abc import ABC, abstractmethod
import os


class Saver(ABC):
    """
    Абстрактный класс для работы с данными вакансий
    """

    @abstractmethod
    def insert(self, params: list):
        pass

    @abstractmethod
    def get_vacancies(self, keyword=None):
        pass

    @abstractmethod
    def delete(self, chosen_vacancies: list):
        pass


class JSONSaver(Saver):
    """
    Класс для работы с данными вакансий в формате JSON
    """

    def __init__(self, path):
        """
        Конструктор класса
        :param path: путь к файлу
        """
        self.__path = path

        # Создание пути к файлу в случае его отсутствия
        if not os.path.exists(os.path.dirname(self.__path)):
            os.mkdir(os.path.dirname(self.__path))
        if not os.path.exists(self.__path):
            with open(self.__path, 'w') as f:
                f.write(json.dumps([]))

    def insert(self, params: list):
        """
        Добавление вакансий в файл
        :param params: отформатированные данные в вакансии
        """

        keys = ["Наименование вакансии",
                "Зарплата",
                "Валюта",
                "Описание",
                "Ссылка на вакансию",
                "Город",
                "Дата публикации",
                "Требуемый опыт",
                "Тип занятости"]

        # Создание словаря вакансий
        vacancy_dict = dict(zip(keys, params))

        data = self.get_vacancies()

        # Добавление вакансии в файл
        with open(self.__path, 'w', encoding="utf-8") as f:
            data.append(vacancy_dict)
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get_vacancies(self, keyword=""):
        """
        Получение вакансий из файла
        :param keyword: ключевое слово для поиска вакансий
        :return: список данных вакансий
        """
        # В случае отсутствия ключа возвращается исходный список
        with open(self.__path, 'r', encoding="utf-8") as f:
            data = json.load(f)
            if keyword == "":
                return data

            result = []
            for vacancy in data:
                if keyword.isdigit() and int(keyword) <= vacancy["Зарплата"]:
                    result.append(vacancy)
                    continue
                if keyword in vacancy.values():
                    result.append(vacancy)

        return result

    @staticmethod
    def delete(chosen_vacancies, keyword=""):
        """
        Удаление вакансий, содержащих в значениях ключ, из файла
        :param chosen_vacancies: список выбранных вакансий
        :param keyword: ключевое слово для удаления вакансий
        :return: список данных вакансий
        """
        # В случае отсутствия ключа возвращается исходный список
        if keyword == "":
            return chosen_vacancies

        data = chosen_vacancies.copy()
        for vacancy in chosen_vacancies:
            for value in vacancy.values():
                if isinstance(value, str):
                    if keyword in value:
                        data.remove(vacancy)
                        break
                    else:
                        continue
                else:
                    continue

        return data

    def clear_file(self):
        """
        Очистка файла
        """
        with open(self.__path, 'w') as f:
            f.write(json.dumps([]))

    def clear_data(self):
        """
        Удаление временных данных
        """
        if os.path.exists(self.__path):
            os.remove(self.__path)
            os.rmdir(os.path.dirname(self.__path))
