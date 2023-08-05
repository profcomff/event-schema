# Библиотека для хранения общих JSON-схем

## Использование
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