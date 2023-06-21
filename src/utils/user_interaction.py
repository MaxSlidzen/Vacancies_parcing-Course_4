from src.classes.APIs import HeadHunterAPI, SuperJobAPI
from src.utils.utils import get_sj_vacancies_params, get_hh_vacancies_params, get_filtered_vacancies, print_per_page


def get_query(saver) -> None:
    """
    Основная функция для взаимодействия с пользователем
    :param saver: Класс для работы с данными вакансий в файле
    :return: При выходе из программы функция завершается без вывода. Иначе - вызывает следующую функцию
    """
    # Бесконечный цикл для корректного взаимодействия с пользователем
    while True:

        query = input("Введите запрос: \n")
        if query == "exit":
            return

        # Получаем экземпляры для работы с API
        hh_api = HeadHunterAPI(query)
        sj_api = SuperJobAPI(query)

        # Получаем параметры вакансий с сайтов
        raw_hh_vacancies = hh_api.get_vacancies()["items"]

        # Обработка исключения при некорректном API_KEY SuperJob
        try:
            raw_sj_vacancies = sj_api.get_vacancies()["objects"]

        except KeyError:
            print("\nНеправильно определен API_KEY для работы с SuperJob")

            # Условие продолжения работы только с HeadHunter
            user_input = input("Продолжить работу только с HeadHunter? (y): ")

            if user_input != "y" or user_input == "exit":
                return
            else:
                # Проверяем наличие вакансий согласно запросу. В случае их отсутствия переходим в начало цикла
                if len(raw_hh_vacancies) == 0:
                    print("Ничего не найдено.\n")
                    continue

                # Форматируем данные вакансий и сохраняем в файл
                for raw_vacancy in raw_hh_vacancies:
                    vacancy = get_hh_vacancies_params(raw_vacancy)
                    saver.insert(vacancy)
        # Выполнение кода, если исключение не вызвалось
        else:
            # Проверяем наличие вакансий согласно запросу. В случае их отсутствия переходим в начало цикла
            if len(raw_hh_vacancies) == 0 and len(raw_sj_vacancies) == 0:
                print("Ничего не найдено.\n")
                continue

            # Форматируем данные вакансий и сохраняем в файл
            for raw_vacancy in raw_hh_vacancies:
                vacancy = get_hh_vacancies_params(raw_vacancy)
                saver.insert(vacancy)

            for raw_vacancy in raw_sj_vacancies:
                vacancy = get_sj_vacancies_params(raw_vacancy)
                saver.insert(vacancy)

        # Выходим из цикла и запускаем следующую функцию
        break
    return to_seek_n_hide(saver)


def to_seek_n_hide(saver) -> None:
    """
    Функция для выборки вакансий из файла по ключевым словам
    :param saver: Класс для работы с данными вакансий в файле
    :return: При выходе из программы функция завершается без вывода. Иначе - вызывает следующую функцию
    """
    # Бесконечный цикл для корректного взаимодействия с пользователем
    while True:

        select_key = input("\nВведите ключевое слово для выборки вакансий:\n"
                           "Чтобы пропустить нажмите 'Enter'.\n")
        if select_key == "exit":
            return

        # Отбор данных вакансий из файла в список по ключевому слову
        selected_vacancies = saver.get_vacancies(select_key)

        hide_key = input("Введите ключевое слово, чтобы скрыть вакансии:\n"
                         "Чтобы пропустить нажмите 'Enter'.\n")

        if hide_key == "exit":
            return

        # Удаление из списка с данными вакансий тех вакансий, в которых упоминается ключевое слово
        final_vacancies = saver.delete(selected_vacancies, hide_key)

        # Формирование списка с экземплярами вакансий согласно отфильтрованному списку с данными
        vacancies = get_filtered_vacancies(final_vacancies)
        # Проверяем наличие вакансий согласно фильтрам. В случае их отсутствия переходим в начало цикла
        if len(vacancies) == 0:
            print("\nНичего не найдено")
            continue
        # Выходим из цикла и запускаем следующую функцию
        break
    return to_print_vacancies(vacancies, saver)


def to_print_vacancies(vacancies: list, saver) -> None:
    """
    Функция для вывода вакансий пользователю
    :param vacancies: Список экземпляров вакансий
    :param saver: Класс для работы с данными вакансий в файле
    :return: При выходе из программы функция завершается без вывода. Иначе - вызывает следующую функцию
    """
    print(f"Найдено вакансий: {len(vacancies)}")
    sort_key = input("\nВакансии будут отсортированы в порядке публикации.\n"
                     "Отсортировать вакансии по заработной плате? (y) \n")

    if sort_key == "exit":
        return
    # Сортировка вакансий
    elif sort_key == "y":
        vacancies.sort(reverse=True)
    else:
        vacancies.sort(key=lambda vacancy: vacancy.published, reverse=True)

    per_page_key = input("\nВведите количество вакансий, отображаемых на странице.\n"
                         "Чтобы вывести все вакансии, нажмите 'Enter'.\n")
    if per_page_key == "exit":
        return
    # Вывод информации о вакансиях и запуск следующей функции
    print_per_page(per_page_key, vacancies)
    return is_continue(saver)


def is_continue(saver) -> None:
    """
    Функция для продолжения работы программы
    :param saver: Класс для работы с данными вакансий в файле
    :return: Завершение цепочки функций, либо возврат к началу запроса/фильтру вакансий
    (в зависимости от команды пользователя)
    """
    continue_key = input("Ввеедите 'n', чтобы завершить программу. \n"
                         "Любой другой ввод продолжит работу программы.\n")

    if continue_key == "n" or continue_key == "exit":
        return

    else:
        new_filter_key = input("Выбрать другие фильтры для отбора вакансий начального запроса? (y): \n"
                               "Любой другой ввод вернет в начало программы.\n")

        if new_filter_key == "exit":
            return
        # Переход к фильтру
        elif new_filter_key == "y":
            return to_seek_n_hide(saver)
        # Очистка файла и переход к новому запросу
        saver.clear_file()
        return get_query(saver)
