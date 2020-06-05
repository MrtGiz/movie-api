## Тестовое задание MovieAPI
Django-приложение, реализующее API для получения списка фильмов со стороннего ресурса с добавлением информации из 
локальной базы данных.

Приложение доступно по адресу:
https://afternoon-brook-15863.herokuapp.com/
___

#### Админка:
https://afternoon-brook-15863.herokuapp.com/admin/

логин/пароль: admin/admin 
___

#### Получение списка фильмов с добавленными локальными данными

GET '/api/v1/list/{page}' 

где {page} - запрашиваемая страница данных из стороннего API

Success 200:

Имя | Тип | Описание
--- | --- | ---
page| int | номер запрашиваемой страници из результата запроса
total_results | int | количество фильмов удовлетворяющих запросу
total_pages | int | общее количество страниц
results | array | объекты фильмов, удовлетворяющие запросу

Состав объекта фильма:

Имя | Тип | Описание
--- | --- | ---
popularity | float | популярность
vote_count | int | количество проголосовавших
video | bool | наличие трейлера
poster_path | str | ссылка на постер
id | int | ID фильма
adult | bool | возрастной рейтинг
backdrop_path | str | ссылка на фон
original_language | str | язык оригинала
original_title | str | оригинальное название
genre_ids | array | список id жанров
title | str | название на английском
vote_average | float | средняя оценка
overview | str | описание на английском
release_date | str | дата релиза
title_rus | str | добавленное название из локальной БД
overview_rus | str | добавленное описание из локальной БД
