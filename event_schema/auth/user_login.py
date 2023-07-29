from pydantic import constr

from event_schema.base import Base


class UserInfo(Base):
    category: str
    param: str
    value: str | None = None


class UserLogin(Base):
    items: list[UserInfo]
    source: constr(min_length=1)
