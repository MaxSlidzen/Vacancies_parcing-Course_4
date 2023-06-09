
import datetime

class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, vacancy_name: str, salary: tuple, description: str, url: str, location: str,
                 published: datetime, experience: str, requirements: str, education:str,
                 employment: str) -> None:
        """
        Инициализация объекта Vacancy.
        :param vacancy_name: Название вакансии
        :param salary: Сумма зарплаты (от, до)
        :param description: Описание вакансии
        :param url: Ссылка на вакансию
        :param location: Город
        :param published: Дата публикации вакансии
        :param experience: Требуемый опыт работы
        :param requirements: Требования к вакансии
        :param education: Требуемое образование
        :param employment: Тип занятости и график
        """
        self.vacancy_name = vacancy_name
        self.salary = salary
        self.description = description
        self.url = url
        self.location = location
        self.published = published
        self.experience = experience
        self.requirements = requirements
        self.education = education
        self.employment = employment


    def __repr__(self) -> str:
        """
        Возвращает строковое представление класса для разработчика
        :return: строковое представление класса
        """
        return f"{self.__class__.__name__}.(vacancy_name={self.vacancy_name}, salary={self.salary}, description={self.description}, " \
               f"url={self.url}, location={self.location}, published={self.published}, experience={self.experience}, " \
               f"requirements={self.requirements}, education={self.education}, employment={self.employment}"


    def __str__(self) -> str:
        """
        Возвращает строковое представление класса для пользователя
        :return: строковое представление класса
        """
        return f"Вакансия: {self.vacancy_name}"


    def __gt__(self, other: 'Vacancy') -> bool:
        """
        Возвращает True, если зарплата вакансии больше зарплаты другой вакансии
        :param other: другая вакансия
        :return: True, если вакансия больше другой
        """
        return self.salary > other.salary
