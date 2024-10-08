from multiprocessing import get_context
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from passlib.context import CryptContext

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)
    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password)
    def __repr__(self):
        return f"<User(username={self.username}, email={self.email}, is_active={self.is_active})>"
    