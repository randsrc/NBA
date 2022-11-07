from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Player(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    height = db.Column(db.Float(), nullable=False)
    weight = db.Column(db.Float(), nullable=False)
    #freethrow = db.Column(db.Float(5), nullable=False)
    avgscore = db.Column(db.Float(5), nullable=False)
    tsp = db.Column(db.Float(5), nullable=False)
    assists = db.Column(db.Float(5), nullable=False)
    def to_dict(self):
        return{
            'name': self.name,
            'height': self.height,
            'weight': self.weight,
            'avgscore': self.avgscore,
            'tsp': self.tsp,
            'assists': self.assists,
           #'freethrow': self.freethrow,
        }
