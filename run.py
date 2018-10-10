from app import app
from db import db


db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()  # mamy już zdefiniowane modele - to tylko tworzy bazę i tabele o ile potrzeba