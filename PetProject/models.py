from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()



class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)