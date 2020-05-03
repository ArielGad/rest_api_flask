from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True  # So flask will see flask_jwt errors
app.secret_key = 'ariel'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


# JWT creates a new endpoint -> /auth
jwt = JWT(app, authenticate, identity)


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
