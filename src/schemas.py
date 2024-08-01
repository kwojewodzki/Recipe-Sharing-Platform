from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    email: str
    hashed_password: str
    is_active: bool