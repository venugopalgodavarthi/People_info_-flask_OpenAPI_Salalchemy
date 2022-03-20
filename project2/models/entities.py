from hyper.db import db
import datetime

class People(db.Model):
    __tablename__ = "peoples"

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ptype = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    check = db.Column(db.Boolean, nullable=False)


    def __repr__(self):
        return 'PeopleModel(pid=%d, name=%s,)' % (self.pid,self.name)

    def json(self):
        return {'pid':self.pid,'name': self.name, 'ptype': self.ptype,
        'age':self.age,'desc': self.desc, 'date': self.date,'check':self.check}