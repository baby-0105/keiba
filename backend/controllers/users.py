from fastapi import HTTPException

from domainmodels.daos.users import UsersModel


class UsersController:
    @classmethod
    def get_name(cls, db):
        try:
            user = db.query(UsersModel).filter(UsersModel.id == 1).first()
            return user.name
        except:
            raise HTTPException(status_code=500, detail="user not found")
