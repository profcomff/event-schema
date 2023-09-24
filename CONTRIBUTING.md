## Что нужно для запуска 

1. python3.11. Установка описана [тут](https://www.python.org/downloads/)

2. Завсимости, описанные в setup.py, requirements.dev.txt

## Как создать новую схему

1. Создать новый .py файл в папке /event_schema/<...>, где ... - то, к чему относится данная схема
2. Создать, если еще не создан, новый __init__.py файл в /event_schema/<...> - там же где создан .py файл
3. Описать схему в созданном файле. Документация по pydantic [тут](https://docs.pydantic.dev/latest/usage/models/)
4. Импортировать схему в ~/event_schema/<...>/__init__.py, указав её в __all__. Пример [тут](https://github.com/profcomff/event-schema/blob/de6ef5b07ff5ba74bafdf7bf9143415e97d6dcd2/event_schema/auth/__init__.py#L3)

## Codestyle

- Black. Как пользоваться описано [тут](https://black.readthedocs.io/en/stable/)

- Также применяем [isort](https://pycqa.github.io/isort/)

