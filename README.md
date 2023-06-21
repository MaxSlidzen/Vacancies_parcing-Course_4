# Проект для парсинга вакансий с HeadHunter и SuperJob

Данная программа позволяет загрузить вакансии по ключевому слову, а затем отфильтровать по ключам и отсортировать

### Особенности проекта
- Поиск вакансий по сайтам-работодателям по ключу производится во всех полях вакансий.
  - Примечание: 
  
    поиск по ключу проводится согласно API сайтов-работадателей. Например, если забыли поменять раскладку клавиатуры 
    и ввели "vfcnth" вместо "мастер", поиск завершится успешно
- Максимальное количество составляет по 100 вакансий с каждого сайта-работодателя
- Все полученные вакансии обрабатываются и приводятся к одному формату
- Обработанные вакансии сохраняются во временном JSON-файле
- <b>В любой момент пользователь может выйти из программы, введя в консоль "exit"</b>
- Ключи для фильтрации чувствительны к регистру. Фильтр производится в точности по ключу
- Фильтрация по ключу производится по всем полям данных вакансий.
- Также при вводе ключа-выборки поддерживается отбор по заработной плате 
(отбираются только те вакансии, заработная плата которых больше или равна введенному числу)
- Создаются экземпляры и формируется список для дальнейшего отображения
- Сортировка по зарплате не учитывает валюту. Берется только числовое значение