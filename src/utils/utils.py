import time
from src.classes.vacancies import Vacancy


def get_date_from_unix_time(unix_time: int):
    """
    Форматирование времени из формата unix time
    :param unix_time: время в формате unix time
    :return: дата в формате гггг-мм-дд
    """
    correct_date = time.strftime("%Y-%m-%d", time.localtime(unix_time))
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
    if raw_vacancy["salary"] is None:
        return 0
    elif raw_vacancy["salary"]["from"] is None:
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


def get_hh_vacancies_params(raw_vacancy: dict) -> list:
    """
    Возвращает параметры для вакансий HH
    :param raw_vacancy: "сырой" словарь с данными о вакансии HH
    :return: параметры для вакансий HH
    """
    salary = get_hh_salary(raw_vacancy)
    if salary > 0:
        currency = raw_vacancy["salary"]["currency"]
    else:
        currency = ""

    return [
        raw_vacancy["name"],
        salary,
        currency,
        f"Требования: {raw_vacancy['snippet']['requirement']}.\n"
        f"{raw_vacancy['snippet']['responsibility']}",
        raw_vacancy["alternate_url"],
        raw_vacancy["area"]["name"],
        to_strip_date(raw_vacancy["published_at"]),
        raw_vacancy["experience"]["name"],
        raw_vacancy["employment"]["name"]
    ]


def get_sj_vacancies_params(raw_vacancy: dict) -> list:
    """
    Возвращает параметры для вакансий SJ
    :param raw_vacancy: "сырой" словарь с данными о вакансии SJ
    :return: параметры для вакансий SJ
    """
    salary = get_sj_salary(raw_vacancy)
    if salary > 0:
        currency = raw_vacancy["currency"]
    else:
        currency = ""
    return [
        raw_vacancy["profession"],
        salary,
        currency,
        raw_vacancy["candidat"],
        raw_vacancy["link"],
        raw_vacancy["town"]["title"],
        get_date_from_unix_time(raw_vacancy["date_published"]),
        raw_vacancy["experience"]["title"],
        raw_vacancy["type_of_work"]["title"]
    ]


def get_filtered_vacancies(vacancies: list) -> list:
    filtered_vacancies = []
    for vacancy in vacancies:
        filtered_vacancies.append(Vacancy(*vacancy.values()))
    return filtered_vacancies


def print_per_page(key, job_list):
    if not key.isdigit():
        per_page = len(job_list)
    elif int(key) > len(job_list):
        per_page = len(job_list)
    else:
        per_page = int(key)

    for i in range(per_page):
        print(job_list[i])
