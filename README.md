# Библиотека для хранения общих JSON-схем

## Использование
```python
from event_schema.auth import UserLogin
from confluent_kafka import Producer

some_data = {} ## insert your data here
kafka_config = {}

producer = Producer(**kafka_config)

new = UserLogin(**some_data)

producer.produce(topic="topic_name", value=new.model_dump_json())
```