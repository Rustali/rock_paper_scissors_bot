from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str      # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()     # Создаем экземлпяр класса Env
    env.read_env(path)      # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))     # Возвращаем экземпляр класса Config, наполнив его данными
                                                            # из переменных окружения


