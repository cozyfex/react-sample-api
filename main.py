from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from faker import Faker

from models.BoardModel import BoardModel
from models.ListModel import ListModel
from models.UserModel import UserModel

fake = Faker("ko_KR")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/user/list")
def get_user_list():
    result = ListModel()

    for _ in range(22):
        user = UserModel()
        simple_profile = fake.simple_profile()
        user.userId = simple_profile["username"]
        user.name = simple_profile["name"]
        result.list.append(user)

    json_compatible_item_data = jsonable_encoder(result)

    return JSONResponse(content=json_compatible_item_data)


@app.get("/user/view/{user_id}")
def get_user_view(user_id):
    result = UserModel()

    profile = fake.profile()
    result.userId = profile["username"]
    result.name = profile["name"]

    json_compatible_item_data = jsonable_encoder(result)

    return JSONResponse(content=json_compatible_item_data)


@app.get("/board/list")
def get_board_list():
    result = ListModel()

    for _ in range(22):
        board = BoardModel()
        profile = fake.profile()
        board.readCount = fake.unique.random_int()
        board.title = profile["company"]
        board.name = profile["name"]
        result.list.append(board)

    json_compatible_item_data = jsonable_encoder(result)

    return JSONResponse(content=json_compatible_item_data)


@app.get("/board/view/{title}")
def get_board_view(title):
    board = BoardModel()
    profile = fake.profile()
    board.readCount = fake.unique.random_int()
    board.title = profile["company"]
    board.name = profile["name"]

    json_compatible_item_data = jsonable_encoder(board)

    return JSONResponse(content=json_compatible_item_data)


@app.post("/board/write")
def post_board_write(item: BoardModel):
    json_compatible_item_data = jsonable_encoder(item)

    return JSONResponse(content=json_compatible_item_data)


@app.put("/board/write")
def put_board_write(item: BoardModel):
    json_compatible_item_data = jsonable_encoder(item)

    return JSONResponse(content=json_compatible_item_data)


@app.delete("/board/delete/{board_name}")
def delete_board(board_name):
    result = {"board_name": board_name}
    json_compatible_item_data = jsonable_encoder(result)

    return JSONResponse(content=json_compatible_item_data)
