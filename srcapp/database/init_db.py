from sqlalchemy.orm import Session

from models.user import User
from schemas.schemas_user import UserCreate
from crud.cruduser import create_user
from security import get_password_hash


def init_db(db: Session) -> None:
    user = db.query(User).first()
    if not user:
        superuser_data = UserCreate(
            email="admin@example.com",
            password="supersecretpassword",
            is_superuser=True
        )
        superuser = create_user(db=db, user=superuser_data)