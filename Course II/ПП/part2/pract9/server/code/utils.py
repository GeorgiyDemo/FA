import uuid


def token_generator() -> str:
    """Генерация токена пользователя"""
    return str(uuid.uuid4()).replace("-", "")
