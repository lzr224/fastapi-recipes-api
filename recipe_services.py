from sqlalchemy.orm import Session
from models import Recipe as RecipeModel
from schemas import RecipeCreate

def create_recipe(db: Session, recipe_data: RecipeCreate):
    recipe = RecipeModel(
        title=recipe_data.title,
        making_time=recipe_data.making_time,
        serves=recipe_data.serves,
        ingredients=recipe_data.ingredients,
        cost=recipe_data.cost,
    )
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe
