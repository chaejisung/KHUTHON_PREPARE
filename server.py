from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from pydantic import BaseModel
from database.dbConfig import conn, cursor
from database.dataModel import User
from database.queries import q1


app = FastAPI()

# middleware - cors설정
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# 라우터
# 사용자 생성
@app.post("/users/", response_model=User)
def create_user(user: User):
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (user.name, user.email))
    conn.commit()
    return user

# 모든 사용자 가져오기
@app.get("/users/")
def read_users():
    query = "SELECT id, name, email FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    return users

# 특정 사용자 가져오기
@app.get("/users/{user_id}")
def read_user(user_id: int):
    query = "SELECT id, name, email FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

myIP = '172.21.4.248'
myPort = 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=myIP, port=myPort)
