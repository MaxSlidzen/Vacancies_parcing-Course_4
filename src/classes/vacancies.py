class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, vacancy_name: str, salary: int, currency: str, description: str, url: str, location: str,
                 published: str, experience: str, employment: str) -> None:
        """
        Инициализация объекта Vacancy.
        :param vacancy_name: Название вакансии
        :param salary: Сумма зарплаты
        :param currency: Валюта
        :param description: Описание вакансии
        :param url: Ссылка на вакансию
        :param location: Город
        :param published: Дата публикации вакансии
        :param experience: Требуемый опыт работы
        :param employment: Тип занятости и график
        """
        self.vacancy_name = vacancy_name
        self.salary = salary
        self.currency = currency
        self.description = description
        self.url = url
        self.location = location
        self.published = published
        self.experience = experience
        self.employment = employment

    def __str__(self) -> str:
        """
        Возвращает строковое представление класса для пользователя
        :return: строковое представление класса
        """
        return f"\nДата публикации: {self.published}, город {self.location}\n" \
               f"Вакансия: {self.vacancy_name}. " \
               f"Заработная плата: {self.salary if self.salary != 0 else '0 (не указана)'} {self.currency}\n" \
               f"Опыт: {self.experience}. Тип занятости: {self.employment}\n" \
               f"Ссылка на вакансию: {self.url}.\n"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление класса для разработчика
        :return: строковое представление класса
        """
        return f"{self.__class__.__name__}.(vacancy_name={self.vacancy_name}, salary={self.salary}, " \
               f"description={self.description}, url={self.url}, location={self.location}, " \
               f"published={self.published}, experience={self.experience}, employment={self.employment}"

    def __gt__(self, other: 'Vacancy') -> bool:
        """
        Возвращает True, если зарплата вакансии больше зарплаты другой вакансии
        :param other: другая вакансия
        :return: True, если вакансия больше другой
        """
        return self.salary > other.salary

    def __lt__(self, other: 'Vacancy') -> bool:
        """
        Возвращает True, если зарплата вакансии меньше зарплаты другой вакансии
        :param other: другая вакансия
        :return: True, если вакансия меньше другой
        """
        return self.salary < other.salary
