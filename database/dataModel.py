from pydantic import BaseModel

# 사용자 데이터 모델
class User(BaseModel):
    id: int
    name: str
    email: str