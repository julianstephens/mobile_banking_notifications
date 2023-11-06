import os

from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env.local")


class Config:
    LM_ACCESS_TOKEN: str = os.environ.get("LM_ACCESS_TOKEN") or ""

    MAIL_USER: str = os.environ.get("MAIL_USER") or ""

    MAIL_PASSWORD: str = os.environ.get("MAIL_PASSWORD") or ""

    MAIL_HOST: str = os.environ.get("MAIL_HOST") or ""

    MAIL_PORT: int = int(os.environ.get("MAIL_PORT") or "-1")

    def __init__(self):
        var_arr = vars(self.__class__)
        members = [
            attr
            for attr in var_arr
            if not callable(getattr(self.__class__, attr)) and not attr.startswith("__")
        ]

        for m in members:
            if not var_arr[m] or var_arr[m] == -1:
                raise ValueError(f"Env var '{m}' is not set")
