# from flask import Flask
# from flask_restful import Api



# app = Flask(__name__)
# api = Api(app)


from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy










app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://test1:123@localhost/test'
db = SQLAlchemy(app)


from resources import student_resource
from resources import book_resource






