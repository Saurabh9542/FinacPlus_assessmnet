from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from connection import get_db, Base, engine
from models import Base, User, Account, Asset
from schema import UserCreate, AccountCreate, AssetCreate


Base.metadata.create_all(bind = engine)


app = FastAPI()


@app.get("/")
def root():
    return "Hello" "World"


@app.post("/users")
def createUser(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username = user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    print(db_user)
    

@app.post("/accounts/")
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    db_account = Account(user_id=account.user_id)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


@app.post("/assets/")
def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
    db_asset = Asset(**asset.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset


@app.get("/portfolio/{user_id}")
def get_portfolio(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    portfolio = {}
    accounts = db.query(Account).filter(Account.user_id == user_id).all()
    for account in accounts:
        assets = db.query(Asset).filter(Asset.account_id == account.id).all()
        portfolio[account.id] = {
            "assets": [{asset.symbol: asset.quantity} for asset in assets]
        }
    
    return portfolio

