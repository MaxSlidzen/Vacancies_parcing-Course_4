from src.classes.savers import JSONSaver
from src.utils.user_interaction import get_query
import requests


def main():

    # Создание экземпляра класса JSONSaver для работы с временным файлом
    json_saver = JSONSaver("data/parsed_vacancies.json")
    print("В любой момент вы можете завершить работу программы, введя команду 'exit'")

    # Обработка исключения при проблемах с сервером или интернетом пользователя
    try:
        # Запуск взаимодействия с пользователем
        get_query(json_saver)
    except requests.exceptions.ConnectionError:
        print("\nПроизошла ошибка при подключении к серверу. Проверьте подключение к сети или попробуйте позже.")

    # Удаление временного файла
    json_saver.clear_data()
    print("\nПрограмма завершена.")


if __name__ == "__main__":
    main()
