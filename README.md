# Библиотека для хранения общих JSON-схем

## Функционал
Представление данных, передаваемых через Kafka, в виде pydantic моделей для валидации принимаемых и отправляемых сообщений

## Сценарий использования
1. Передача соообщения о пользовательских данных
```python
from event_schema.auth import UserLogin, UserLoginKey
from confluent_kafka import Producer

some_data = {} ## insert your data here
kafka_config = {}

producer = Producer(**kafka_config)

new = UserLogin(**some_data)
new_key = UserLoginKey(user_id=42)

producer.produce(topic="topic_name", key=new_key.model_dump_json(), value=new.model_dump_json())
producer.flush()
```

## Contributing 
- Основная [информация](https://github.com/profcomff/.github/wiki/%255Bdev%255D-Backend-%25D1%2580%25D0%25B0%25D0%25B7%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25BA%25D0%25B0) по разработке наших приложений

- [Ссылка](https://github.com/profcomff/event-schema/blob/main/CONTRIBUTING.md) на страницу с информацией по разработке event-schema
