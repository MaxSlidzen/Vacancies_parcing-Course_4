class Vacancy:
    """
    Класс для работы с вакансиями
    """
    __slots__ = ['__vacancy_name', '__salary', '__currency', '__description', '__url', '__location',
                 '__published', '__experience', '__employment']

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
        return f"{self.__class__.__name__}.({self.__slots__})"

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

    # Валидация данных инициализации
    @property
    def vacancy_name(self) -> str:
        return self.__vacancy_name

    @vacancy_name.setter
    def vacancy_name(self, value) -> None:
        if isinstance(value, str):
            self.__vacancy_name = value

    ###

    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, value) -> None:
        if isinstance(value, int):
            self.__salary = value

    ###

    @property
    def currency(self) -> str:
        return self.__currency

    @currency.setter
    def currency(self, value) -> None:
        if isinstance(value, str) and (len(value) == 3 or len(value) == 0):
            self.__currency = value

    ###

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value) -> None:
        if isinstance(value, str):
            self.__description = value

    ###

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, value) -> None:
        if isinstance(value, str) and 'http' in value:
            self.__url = value

    ###

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value) -> None:
        if isinstance(value, str):
            self.__location = value

    ###

    @property
    def published(self) -> str:
        return self.__published

    @published.setter
    def published(self, value) -> None:
        if isinstance(value, str) and len(value) == 10:
            self.__published = value

    ###

    @property
    def experience(self) -> str:
        return self.__experience

    @experience.setter
    def experience(self, value) -> None:
        if isinstance(value, str):
            self.__experience = value

    ###

    @property
    def employment(self) -> str:
        return self.__employment

    @employment.setter
    def employment(self, value) -> None:
        if isinstance(value, str):
            self.__employment = value
