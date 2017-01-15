from flask_restful import reqparse, Resource
from flask import request
from models import *
from app import api

parser = reqparse.RequestParser()
parser.add_argument('user_id', type=str)


class SinglePerson(Resource):
    def get(self):
        user_id = request.args.get('user_id')

        person = ndb.Key('Person', user_id).get()
        return person.serialize, 200

    def post(self):
        person_json = request.get_json()

        person = Person()
        person.user_id = person_json.get('user_id')
        person.name = person_json.get('name')
        person.age = person_json.get('age')
        person.email = person_json.get('email')

        person.key = ndb.Key('Person', person_json.get('user_id'))
        person.put()

        return person.key.id(), 204

    def put(self):
        pass

    def delete(self):
        pass


class AllPersons(Resource):
    def get(self):
        persons = Person.query().fetch()
        return [p.serialize for p in persons], 200


api.add_resource(SinglePerson, '/person')
api.add_resource(AllPersons, '/allpersons')
