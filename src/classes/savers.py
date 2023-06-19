import json
from abc import ABC, abstractmethod
import os


class Saver(ABC):

    @abstractmethod
    def insert(self, params: list):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class JSONSaver(Saver):

    def __init__(self, path):
        self.path = path

        if not os.path.exists(os.path.dirname(self.path)):
            os.mkdir(os.path.dirname(self.path))
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                f.write(json.dumps([]))

    def insert(self, params: list):
        keys = ["Наименоввание вакансии",
                "Зарплата",
                # "Валюта",
                "Описание",
                "Ссылка на вакансию",
                "Город",
                "Дата публикации",
                "Требуемый опыт",
                "Тип занятости"]

        vacancy_dict = dict(zip(keys, params))

        data = self.get_vacancies()

        with open(self.path, 'w', encoding="utf-8") as f:
            data.append(vacancy_dict)
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get_vacancies(self, keyword=None):
        with open(self.path, 'r', encoding="utf-8") as f:
            data = json.load(f)
            if keyword is None:
                return data
            result = []
            for vacancy in data:
                if keyword in vacancy.values():
                    result.append(vacancy)
        return result

    def delete(self, keyword=None):
        data = self.get_vacancies()
        if keyword is None:
            return data
        result = []
        for vacancy in data:
            if keyword not in vacancy.values():
                result.append(vacancy)

    def clear_data(self):
        os.remove(self.path)
        os.rmdir(os.path.dirname(self.path))
