from datetime import datetime
from time import mktime
from wsgiref.handlers import format_date_time


def get_date() -> str:
    """
    Возвращает текущую дату и время в формате Http хедера Date

    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Date
    """
    now = datetime.now()
    stamp = mktime(now.timetuple())
    return format_date_time(stamp)
