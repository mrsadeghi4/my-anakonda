from datetime import datetime

from pytz import timezone

from ..config import Config


def now():
    return datetime.now(tz=timezone(Config.TimeZONE))
