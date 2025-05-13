import sys
sys.path.append('../')

from fastapi import APIRouter
from pydantic import BaseModel

auth_endpoint = APIRouter()

class PostAuthAdminRequest(BaseModel):
    email: str
    password: str
    administorator_code: int

class PostAuthStudentRequest(BaseModel):
    email: str
    password: str

@auth_endpoint.post("/auth/admin/login", tags=["auth"])
def handle_login(user: PostAuthAdminRequest):
    """
    ログインに使用するエンドポイント
    """
    return {"user": f"メールアドレス {user.email} パスワード {user.password} ユーザを作成するエンドポイント"}

@auth_endpoint.post("/auth/student/login", tags=["auth"])
def handle_student_login(user: PostAuthStudentRequest):
    """
    学生ログインに使用するエンドポイント
    """
    return {"user": f"メールアドレス {user.email} パスワード {user.password} ユーザを作成するエンドポイント"}
