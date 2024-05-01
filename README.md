# Сервис по нахождению TF и IDF
Находит параметры TF и IDF из предоставленого файла
> TF (Term Frequency) - это мера того, как часто слово встречается в документе
IDF (Inverse Document Frequency) - это мера того, насколько уникальным слово является для всей колекции документов.
[wiki](https://ru.wikipedia.org/wiki/TF-IDF)

### Описание
 После загрузки текстового файла в форму отображается таблица с 50 словами из файла с колонками:
- слово
- tf, сколько раз это слово встречается в тексте
- idf, обратная частота документа
- Вывод упорядочить по уменьшению idf.

### Технологии
[![Python](https://img.shields.io/badge/Python-%5E3.11-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Swagger](https://img.shields.io/badge/Swagger-Latest-blue?style=flat&logo=swagger&logoColor=white)](https://swagger.io/)
[![Docker](https://img.shields.io/badge/Docker-Latest-blue?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Redis](https://img.shields.io/badge/Redis-Latest-blue?style=flat&logo=redis&logoColor=white)](https://redis.io/)
### Библиотеки и фреймворки
[![FastAPI](https://img.shields.io/badge/FastAPI-%5E0.110.3-blue?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-%5E0.29.0-blue?style=flat&logo=python&logoColor=white)](https://www.uvicorn.org/)
[![Python Multipart](https://img.shields.io/badge/PythonMultipart-%5E0.0.9-blue?style=flat&logo=python&logoColor=white)](https://pypi.org/project/python-multipart/)
[![Jinja2](https://img.shields.io/badge/Jinja2-%5E3.1.3-blue?style=flat&logo=python&logoColor=white)](https://palletsprojects.com/p/jinja/)
[![Pydantic Settings](https://img.shields.io/badge/PydanticSettings-%5E2.2.1-blue?style=flat&logo=python&logoColor=white)](https://pypi.org/project/pydantic-settings/)
[![Pydantic](https://img.shields.io/badge/Pydantic-%5E2.7.1-blue?style=flat&logo=python&logoColor=white)](https://pydantic-docs.helpmanual.io/)
### Разработка
[![Poetry](https://img.shields.io/badge/Poetry-use-green?style=flat)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/badge/Ruff-use-green?style=flat)](https://docs.astral.sh/)
[![Pre-commit](https://img.shields.io/badge/Pre--commit-use-green?style=flat)](https://pre-commit.com/)
## Запуск
1. Создать и заполнить файл .env по образцу .env.example
2. Из директории проекта запустить командой
``` bash
docker compose -f infra/docker-compose.local.yml up -d
```
> Приложение будет доступно по адресу http://localhost а swagger документация http://localhost/docs

[Оганин Петр](https://github.com/necroshizo) @2024
