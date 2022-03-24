from datetime import datetime, timedelta

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Enum,
    Boolean,
    ForeignKey,
)
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship

from app.database.conn import db, Base

class BaseMixin:
    id         = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    def __init__(self):
        self._q = None
        self._session = None
        self.served = None
    
    def all_columns(self):
        return [c for c in self.__table__.columns if c.primary_key is False and c.name !="created_at"]
    
    def __hash(self):
        return hash(self.id)

    @classmethod
    def create(cls, session:Session, auto_commit=False, **kwargs):
        """
        테이블 데이터 적재 전용 함수
        :param session:
        :param auto_commit: 자동 커밋 여부
        :param kwargs: 적재 할 데이터
        :return:
        """
        obj = cls()
        for col in obj.all_columns():
            col_name = col.name
            if col_name in kwargs:
                setattr(obj, col_name, kwargs.get(col_name))
        
        session.add(obj)
        session.flush()
        if auto_commit:
            session.commit()
        return obj

    @classmethod
    def get(cls, **kwargs):
        """
        Simply get a Row
        :param kwargs:
        :return:
        """
        session = next(db.session())
        query = session.query(cls)
        for key, val in kwargs.items():
            col = getattr(cls, key)
            query = query.filter(col == val)

        if query.count() > 1:
            raise Exception("Only one row is supposed to be returned, but got more than one.")
        return query.first()

class Users(Base, BaseMixin):
    __tablename__="users"
    status          = Column(Enum("active", "deleted", "blocked"), default="active")
    email           = Column(String(length= 255), nullable=True)
    pw              = Column(String(length=2000), nullable=True)
    name            = Column(String(length= 255), nullable=True)
    phone_number    = Column(String(length=  20), nullable=True)
    profile_img     = Column(String(length=1000), nullable=True)
    sns_type        = Column(Enum("FB","G","K"), nullable=True)
    marketing_agree = Column(Boolean, nullable=True, default=True)
    # keys = relationship("ApiKeys", back_populates="users")
 
