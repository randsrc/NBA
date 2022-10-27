from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Player(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first = db.Column(db.Text(), nullable=False)
    last = db.Column(db.Text(), nullable=False)
    height = db.Column(db.Float(), nullable=False)
    weight = db.Column(db.Float(), nullable=False)
    #freethrow = db.Column(db.Float(5), nullable=False)
    avgscore = db.Column(db.Float(5), nullable=False)
    field = db.Column(db.Float(5), nullable=False)
    threepoint = db.Column(db.Float(5), nullable=False)

    def to_dict(self):
        return{
            'first': self.first,
            'last': self.last,
            'height': self.height,
            'weight': self.weight,
            'avgscore': self.avgscore,
            'field': self.field,
            'threepoint': self.threepoint,
           #'freethrow': self.freethrow,
        }
