from . import db_session
from .users import User
from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify
from .reqparser import parser


def abort_if_jobs_not_found(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_jobs_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({'users': users.to_dict(
            only=('surname', 'name', 'position', 'address','email','age'))})

    def delete(self, user_id):
        abort_if_jobs_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('surname', 'name', 'position', 'address','email','age')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            surname=args['surname'],
            name=args['name'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['address'],
            age=args['age']

        )
        session.add(users)
        session.commit()
        return jsonify({'id': users.id})