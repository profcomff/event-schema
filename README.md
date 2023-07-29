# Библиотека для хранения общих JSON-схем

## Использование
```python
from event_schema import UserInfoUpdate
from confluent_kafka import Producer

some_data = {} ## insert your data here
kafka_config = {}

producer = Producer(**kafka_config)

new = UserInfoUpdate(**some_data)

producer.produce(topic="topic_name", value=new.model_dump_json())
```