from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ The pet Model """

    __tablename__ = 'adoption'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default='https://bit.ly/3tQncTZ') #how to make optional still?
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)

    def __repr__ (self):
        return f'<Pet id:{self.id}, name:{self.name}, species:{self.species}, photo_url:{self.photo_url}, age:{self.age}, notes:{self.notes}, available:{self.available}>'
