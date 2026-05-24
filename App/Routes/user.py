from fastapi import APIRouter, HTTPException,status
from App.CRUD.user import create_user, get_user_by_email
from App.Models.user import UserRegister,UserLogin
from App.utils.password import verify
from App.utils.authentication import generate_jwt_token

router = APIRouter(prefix="")
@router.post("/register")
async def register_user(user:UserRegister):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User email already exists")
    await create_user(user)
    return{"message":"User Registered"}

@router.post("/login")
async def login_user(user:UserLogin):
    db_user = await get_user_by_email(user.email)
    if not db_user or not verify(user.password, db_user["password"]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid email or password")
    token = generate_jwt_token({
        "id": str(db_user["_id"]),
        "name": db_user["name"],
        "email": db_user["email"]
    })
    return {"message":"Login successful","token": token}