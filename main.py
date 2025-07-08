import os
import uvicorn
from fastapi import FastAPI

from endpoints import router as recipe_router
from database import init_db

app = FastAPI()

# 初始化数据库
init_db()

# 注册路由
app.include_router(recipe_router)

# Railway 会自动设置 PORT 环境变量
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
