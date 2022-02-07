import uuid

import sha3


def hasher(password: str) -> str:
    """Хеширование данных"""
    return sha3.sha3_224(password.encode("utf-8")).hexdigest()


def token_generator() -> str:
    """Генерация токена пользователя"""
    return str(uuid.uuid4()).replace("-", "")
