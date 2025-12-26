import os

class config():
    BASE_DIR =os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://flaskuser:password@localhost/flaskdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


