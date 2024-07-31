from fastapi import APIRouter, Request, Form, status
from models.todos import Todo
from schema.schemas import individual_serial, list_todos
from config.database import collection_name
from bson import ObjectId
from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/")
async def home(request: Request):
    todos = collection_name.find()
    return templates.TemplateResponse("index.html", {"request": request, "todo_list": todos})

@router.post("/add")
async def insert_todo(request: Request, Title: str = Form(...), Description: str = Form(...)):
    todo = Todo(title = Title, description = Description)
    collection_name.insert_one(dict(todo))

    url = router.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@router.get("/update/{todo_id}")
async def update_todo(request: Request, todo_id: str):
    _id = ObjectId(todo_id)
    todo = collection_name.find_one({"_id": _id})
    collection_name.update_one({"_id": _id}, {"$set": {"complete": not(todo["complete"])}})

    url = router.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)



@router.get("/delete/{todo_id}")
async def update_todo(request: Request, todo_id: str):
    _id = ObjectId(todo_id)
    collection_name.delete_one({"_id": _id})

    url = router.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)



# @router.get("/")
# async def get_todos():
#     todos = collection_name.find()
#     return list_todos(todos)


# @router.post("/")
# async def insert_todo(todo: Todo):
#     collection_name.insert_one(dict(todo))


# @router.put("/{id}")
# async def delete_todo(_id: str, todo: Todo):
#     collection_name.find_one_and_update({"_id": ObjectId(_id)}, {"$set": dict(todo)})


# @router.delete("/{id}")
# async def delete_todo(_id: str):
#     collection_name.find_one_and_delete({"_id": ObjectId(_id)})