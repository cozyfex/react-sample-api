from pydantic import BaseModel


class BoardModel(BaseModel):
    title = ""
    readCount = 0
    name = ""
