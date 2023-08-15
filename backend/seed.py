from database import SessionLocal
from domainmodels.daos.users import UsersModel

db = SessionLocal()


def seed():
    user = UsersModel(name='アンパンマン')

    db.add(user)
    db.commit()


if __name__ == '__main__':
    seed()
