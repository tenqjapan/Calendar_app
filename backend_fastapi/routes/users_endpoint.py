import sys
sys.path.append('../')

from fastapi import APIRouter
from pydantic import BaseModel

users_endpoint = APIRouter()

class PostUserRequest(BaseModel):
    email: str
    password: str
    is_administrator: bool

@users_endpoint.get("/users", tags=["users"])
def handle_get_users():
    """
    ユーザ情報を取得するエンドポイント
    """
    return {"users": "ユーザ一覧を返すエンドポイント"}

@users_endpoint.get("/users/{user_id}", tags=["users"])
def handle_get_user(user_id: int):
    """
    ユーザ情報を取得するエンドポイント
    """
    return {"user": f"ユーザID {user_id} の情報を返すエンドポイント"}

@users_endpoint.get("/users/email/{email}", tags=["users"])
def handle_get_user_by_email(email: str):
    """
    ユーザ情報を取得するエンドポイント
    """
    return {"user": f"メールアドレス {email} のユーザ情報を返すエンドポイント"}

@users_endpoint.post("/users", tags=["users"])
def handle_create_user(user: PostUserRequest):
    """
    ユーザ情報を作成するエンドポイント
    """
    return {"user": f"メールアドレス {user.email} パスワード {user.password} 権限 {user.is_administrator} ユーザを作成するエンドポイント"}

@users_endpoint.delete("/users/{user_id}", tags=["users"])
def handle_delete_user(user_id: int):
    """
    ユーザ情報を削除するエンドポイント
    """
    return {"user": f"ユーザID {user_id} を削除するエンドポイント"}