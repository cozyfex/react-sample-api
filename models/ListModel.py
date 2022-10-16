from pydantic import BaseModel


class ListModel(BaseModel):
    result = False
    list = []
