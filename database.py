from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base

# 使用 SQLite 数据库文件
DATABASE_URL = "sqlite:///./recipes.db"

# 创建 SQLAlchemy 引擎和 Session 工厂
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    初始化数据库：建表 + 插入初始数据（如果表是空的）
    """
    # 创建表
    Base.metadata.create_all(bind=engine)

    # 检查是否已有数据，若无则插入初始数据
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM recipes"))
        count = result.scalar()

        if count == 0:
            conn.execute(text("""
                INSERT INTO recipes (
                  id, title, making_time, serves, ingredients, cost, created_at, updated_at
                ) VALUES (
                  1, 'チキンカレー', '45分', '4人', '玉ねぎ,肉,スパイス', 1000,
                  '2016-01-10 12:10:12', '2016-01-10 12:10:12'
                );
            """))
            conn.execute(text("""
                INSERT INTO recipes (
                  id, title, making_time, serves, ingredients, cost, created_at, updated_at
                ) VALUES (
                  2, 'オムライス', '30分', '2人', '玉ねぎ,卵,スパイス,醤油', 700,
                  '2016-01-11 13:10:12', '2016-01-11 13:10:12'
                );
            """))
            conn.commit()
