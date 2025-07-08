from pydantic import BaseModel
from typing import List
from datetime import datetime

# 请求体：创建用
class RecipeCreate(BaseModel):
    title: str
    making_time: str
    serves: str
    ingredients: str
    cost: int

# 返回的单个 recipe 数据结构
class Recipe(BaseModel):
    id: int
    title: str
    making_time: str
    serves: str
    ingredients: str
    cost: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # 允许从 ORM 模型中读取字段
        

# 成功响应格式
class RecipeCreateSuccessResponse(BaseModel):
    message: str
    recipe: List[Recipe]

# 失败响应格式
class RecipeCreateErrorResponse(BaseModel):
    message: str
    required: str
