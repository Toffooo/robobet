from dataclasses import dataclass

from decouple import config


DB_URL = config("DB_URL", cast=str)


@dataclass(frozen=True)
class Bet1X:
    base_url: str = "https://1xbet.kz/"
    get_balance: str = "https://1xbet.kz/"
