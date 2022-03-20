from hyper.db import db
from models.entities import People
from typing import List


class PeopleRepo:
    
    def create(self,people):
        db.session.add(people)
        db.session.commit()
        
    def fetchById(self,_pid)-> 'People':
        return db.session.query(People).filter_by(pid=_pid).first()
    
    def fetchAll(self) -> List['People']:
        return db.session.query(People).all()
    
    def deleteAll(self) -> List['People']:
        db.session.query(People).delete()
        db.session.commit()
    
    def delete(self,_pid) -> None:
        people= db.session.query(People).filter_by(pid=_pid).first()
        db.session.delete(people)
        db.session.commit()
        
    def update(self,People_data):
        db.session.merge(People_data)
        db.session.commit()