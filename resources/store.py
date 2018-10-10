from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help='This field cannot be blank'
    )

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message': 'Store {} not found'.format(name)}, 404

    @jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'A store with name {} already exists.'.format(name)}, 400

        # data = Store.parser.parse_args()  # data = request.get_json() - to wersja bez parsowania mamy czysty json z requestu
        store = StoreModel(name)
        # store = StoreModel(name, **data)

        try:
            store.save_to_db()
        except:
            return {"massage": "An error occured inserting store."}, 500

        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if name:
            store.delete_from_db()
        return {'message': 'Store deleted.'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}