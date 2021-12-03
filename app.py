from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'postgres://db_user:db_pw@localhost:5432/db_name'
SQLALCHEMY_BINDS = {
    'db1': SQLALCHEMY_DATABASE_URI,
    'db2': 'mysql://db_user:db_pw@localhost:3306/db_name'
}

app = Flask(__name__)
db = SQLALchemy(app)

class PostgresModel(db.Model):

    __tablename__ = 'postgres_model_table'
    __bind_key__ = 'db1'

    id = db.Column(db.Integer, primary_key=True)
    


class MySQLModel(db.Model):

    __tablename__ = 'mysql_model_table'
    __bind_key__ = 'db2'

    id = db.Column(db.Integer, primary_key=True)


manager = restless.APIManager(app, flask_sqlalchemy_db=db)
manager.init_app(app, db)

auth_func = lambda: is_authenticated(app)

manager.create_api(PostgresModel,
                   methods=['GET'],
                   collection_name='postgres_model',
                   authentication_required_for=['GET'],
                   authentication_function=auth_func)

manager.create_api(MySQLModel,
                   methods=['GET'],
                   collection_name='mysql_model',
                   authentication_required_for=['GET'],
                   authentication_function=auth_func)
