import os
import uvicorn
from fastapi import FastAPI
from endpoints import router as recipe_router
from database import init_db

app = FastAPI()

init_db()
app.include_router(recipe_router)

# 如果本地执行 main.py，自动运行 uvicorn
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
