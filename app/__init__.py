from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
# from .database.contact_db import reset_table

# from .routes import global_scope, api_scope, errors_scope

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:CAMIlodev1994@localhost/pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Database
db = SQLAlchemy(app)
connection = db.session.connection()
result = connection.execute("SELECT * FROM cats")
print("Conexion Establecida")
# app.register_blueprint(global_scope, url_prefix="/")
# app.register_blueprint(errors_scope, url_prefix="/")
# app.register_blueprint(api_scope, url_prefix="/api")

# reset_table()