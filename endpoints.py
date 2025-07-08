from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import (
    RecipeCreate, 
    RecipeCreateSuccessResponse, 
    RecipeCreateErrorResponse, 
    Recipe
)
import recipe_services

router = APIRouter()

# 获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(
    "/recipes",
    response_model=RecipeCreateSuccessResponse,
    responses={400: {"model": RecipeCreateErrorResponse}}
)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    try:
        new_recipe = recipe_services.create_recipe(db, recipe)
        return {
            "message": "Recipe successfully created!",
            "recipe": [Recipe.from_orm(new_recipe)]
        }
    except Exception:
        return JSONResponse(
            status_code=400,
            content={
                "message": "Recipe creation failed!",
                "required": "title, making_time, serves, ingredients, cost"
            }
        )
