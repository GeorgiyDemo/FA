import re
from datetime import datetime

from pydantic import BaseModel, validator

from utils import token_generator


class AuthUser(BaseModel):
    email: str
    password: str

    class Config:
        validate_assignment = True

    @validator("email")
    def email_validation(cls, value: str) -> str:
        regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if re.search(regex, value):
            return value
        raise ValueError("Некорректный e-mail")


class User(AuthUser):
    id: int
    name: str
    api_key: str = token_generator()
    create_at: datetime = datetime.now()

    @validator("name")
    def name_validation(cls, value: str) -> str:
        numbers_list = list(map(str, range(10)))
        if any(map(lambda x: x in value, numbers_list)):
            raise ValueError("ФИО не может содержать цифр")
        return value
