from models.repositories import PeopleRepo
from schemas.schemas import PeopleSchema
from flask import request
from flask import Flask
from hyper import db
from datetime import datetime
from models.entities import People
peopleRepo = PeopleRepo()
peopleSchema = PeopleSchema()
peopleListSchema = PeopleSchema(many=True)
PEOPLE_NOT_FOUND = "People not found for id: {}"

app = Flask(__name__)

def get(pid):
    people_data = peopleRepo.fetchById(pid)
    if people_data:
        return peopleSchema.dump(people_data)
    return {'message': PEOPLE_NOT_FOUND.format(pid)}, 404

def update(pid):
    people_data = peopleRepo.fetchById(pid)
    people_req_json = request.get_json()
    if people_data:
        people_data.name = people_req_json['name']
        people_data.ptype = people_req_json['ptype']
        people_data.age = people_req_json['age']
        people_data.desc = people_req_json['desc']
        people_data.date = datetime.now()
        people_data.check = people_req_json['check']
        peopleRepo.update(people_data)
        return peopleSchema.dump(people_data)
    return {'message': PEOPLE_NOT_FOUND.format(pid)}, 404

def create():
    people_data = request.get_json(force=True)
    if people_data:
        pid=int(people_data['pid'])
        name=people_data['name']
        ptype=people_data['ptype']
        age=int(people_data['age'])
        desc=people_data['desc']
        date=datetime.now()
        check=bool(people_data['check'])
        peop=People(pid=pid,name=name,ptype=ptype,age=age,desc=desc,date=date,check=check)
        peopleRepo.create(peop)
        return peopleSchema.dump(peop),201
    return {'message': 'Data is incorrect format'}, 404
    

def getAll():
    return peopleListSchema.dump(peopleRepo.fetchAll()), 200

def deleteAll():
    return peopleListSchema.dump(peopleRepo.deleteAll()), 200

def delete(pid):
    people_data = peopleRepo.fetchById(pid)
    if people_data:
        peopleRepo.delete(pid)
        return {'message': 'People deleted successfully'}, 200
    return {'message': PEOPLE_NOT_FOUND.format(pid)}, 404
