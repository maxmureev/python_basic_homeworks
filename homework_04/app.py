from fastapi import FastAPI, Request, HTTPException, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Item(BaseModel):
    """Data Model"""

    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# Fake items Storage
fake_items_db = [
    {
        "id": 1,
        "name": "Item_1",
        "description": "Description 1",
        "numeric": 100.0,
        "sub_numeric": 10.0,
    },
    {
        "id": 2,
        "name": "Item_2",
        "description": "Description 2",
        "numeric": 200.0,
        "sub_numeric": 20.0,
    },
]

# Router for API
api_router = APIRouter(prefix="/api")

# Nested routers
@api_router.get("/items/", response_model=List[Item])
async def read_items():
    return fake_items_db


@api_router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    item = next((item for item in fake_items_db if item["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return item


@api_router.post("/items/", response_model=Item)
async def create_item(item: Item):
    fake_items_db.append(item.dict())
    return item


# Connecting the API router to the main app
app.include_router(api_router)


# HTML viewes
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Сайт ДЗ | Homework 04",
        },
    )


@app.get("/about/", response_class=HTMLResponse, include_in_schema=False)
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {
            "request": request,
            "title": "Сайт ДЗ | About",
        },
    )


@app.get("/list/", response_class=HTMLResponse, include_in_schema=False)
async def read_items_html(request: Request):
    return templates.TemplateResponse(
        "list.html",
        {
            "request": request,
            "title": "Список товаров",
            "items": fake_items_db,
        },
    )
