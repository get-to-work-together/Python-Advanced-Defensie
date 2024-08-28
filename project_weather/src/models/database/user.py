from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:

    username: str
    password: str
    email: str
    last_login: str = None
    active: int = 1

