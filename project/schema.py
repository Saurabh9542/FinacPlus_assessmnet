from pydantic import BaseModel



class UserCreate(BaseModel):
    username: str

class AccountCreate(BaseModel):
    user_id: int

class AssetCreate(BaseModel):
    account_id: int
    symbol: str
    quantity: float
