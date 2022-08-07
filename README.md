# Учебный проект YaMDB
### Описание
REST API для проекта YaMDB - база отзывов и рейтингов пользователей на произведения (книги, фильмы, музыка и пр.)

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти, из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.

### Технологии
Python 3.7
Django 2.2.16
Django Rest Framework 3.12.4

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/robky/yamdb_final.git
cd yamdb_final
```

Переименовать файл .env.example

```
mv ./infra/.env.example ./infra/.env
```

После переименования заполнить файл .env актуальными данными согласно примера.

Запустить контейнер

```
docker-compose up -d --build
```

Выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

Загрузить данные из файлов csv в базу данных:

```
docker-compose exec web python manage.py filldb
```

Создать суперпользователя

```
docker-compose exec web python manage.py createsuperuser
```

Подключить статику

```
docker-compose exec web python manage.py collectstatic --no-input
```

Запустить в браузере

```
http://localhost/admin/
```
