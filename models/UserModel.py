from pydantic import BaseModel


class UserModel(BaseModel):
    userId = ""
    name = ""
