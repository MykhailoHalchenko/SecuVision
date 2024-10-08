from sqlalchemy.orm import Session
from models.user import User
from schemas.schemas_user import UserCreate, UserUpdate

# Функція для створення користувача
def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        is_active=True,
        is_superuser=user.is_superuser
    )
    db_user.set_password(user.password)  
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    db_user.username = user_update.username or db_user.username
    db_user.email = user_update.email or db_user.email
    if user_update.password:
        db_user.set_password(user_update.password)  
    db_user.is_active = user_update.is_active if user_update.is_active is not None else db_user.is_active
    db_user.is_superuser = user_update.is_superuser if user_update.is_superuser is not None else db_user.is_superuser

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False
