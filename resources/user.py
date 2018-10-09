import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field cannot be left blank.'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field cannot be left blank.'
    )

    def post(self):
        data = UserRegister.parser.parse_args()  # pobieramy dane z body po uprzednim parsowaniu

        if UserModel.find_by_user_name(data['username']):
            return {"message": "Username {} already exists.".format(data['username'])}, 400

        # user = UserModel(data['username'], data['password'])
        # user.save_to_db()

        # UserModel(data['username'], data['password']).save_to_db()

        UserModel(**data).save_to_db()

        return {"message": "User created successfully."}, 201

