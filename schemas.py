from typing import Optional

from decouple import config
from pydantic import BaseModel


CSRF_KEY = config("CSRF_KEY")


class CsrfSettings(BaseModel):
    secret_key: str = CSRF_KEY


class ToDo(BaseModel):
    id: str
    title: str
    description: str


class ToDoBody(BaseModel):
    title: str
    description: str


class SuccessMsg(BaseModel):
    message: str


class UserBody(BaseModel):
    email: str
    password: str


class UserInfo(BaseModel):
    user_id: Optional[str] = None
    email: str


class Csrf(BaseModel):
    csrf_token: str