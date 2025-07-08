from fastapi import FastAPI
from endpoints import router as recipe_router
from database import init_db

app = FastAPI()

# 初始化数据库并插入初始数据
init_db()

# 加载所有 API 路由
app.include_router(recipe_router)
