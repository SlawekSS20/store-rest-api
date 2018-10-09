from flask_restful import Resource, reqparse  # reqparse - to do selektywnego parsowania i updatowania potem
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank."
    )
    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="Every item needs the store_id."
    )

    @jwt_required()  # ten dekorator powoduje, że request wymaga autentykacji (importowany powyżej)
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {'message': 'Item {} not found'.format(name)}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'An item with name {} already exists.'.format(name)}, 400

        data = Item.parser.parse_args()  # data = request.get_json() - to wersja bez parsowania mamy czysty json z requestu
        item = ItemModel(name, data['price'], data['store_id'])
        # item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"massage": "An error occured inserting item."}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if name:
            item.delete_from_db()
        return {'message': 'Item deleted.'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}  # to dla pythonowców
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}  # to dla JSów

