from App.Models.user import UserRegister, UserLogin
from App.Routes.db import db
from bson import ObjectId
from App.utils.password import hash

user_collection=db["ReviUsers"]

async def create_user(user:UserRegister):
    hashed_password = hash(user.password)
    user_json = user.model_dump()
    user_json["password"] = hashed_password
    result = await user_collection.insert_one(user_json)
    return str(result.inserted_id)

async def get_user_by_email(email:str):
    return await user_collection.find_one({"email":email})