from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    username = Column(String(120))
    merged = Column(Integer)
    closed = Column(Integer)

    def __repr__(self):
        return f'<Member: {self.username}>'
