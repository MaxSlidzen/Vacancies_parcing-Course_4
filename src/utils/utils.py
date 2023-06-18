import time


def get_date_from_unix_time(unix_time: str):
    """
    Форматирование времени из формата unix time
    :param unix_time: время в формате unix time
    :return: дата в формате гггг-мм-дд
    """
    correct_date = time.strftime("%Y-%m-%d", time.localtime(int(unix_time)))
    return correct_date


def to_strip_date(date_str: str):
    """
    Возвращает дату публикации без указания времени
    :param date_str:
    :return: дата в формате гггг-мм-дд
    """
    stripped_date = date_str.split("T")[0]
    return stripped_date


def get_hh_salary(raw_vacancy: dict) -> int:
    """
    Возвращает величину зарплаты для вакансий HH
    :param raw_vacancy: "сырой" словарь с данными о вакансии HH
    :return: величина зарплаты
    """
    if raw_vacancy["salary"]["from"] is None:
        if raw_vacancy["salary"]["to"] is None:
            return 0
        return raw_vacancy["salary"]["to"]
    return raw_vacancy["salary"]["from"]


def get_sj_salary(raw_vacancy: dict) -> int:
    """
    Возвращает величину зарплаты для вакансий SJ
    :param raw_vacancy: "сырой" словарь с данными о вакансии SJ
    :return: величина зарплаты
    """
    if raw_vacancy["payment_from"] == 0:
        if raw_vacancy["payment_to"] == 0:
            return 0
        return raw_vacancy["payment_to"]
    return raw_vacancy["payment_from"]

