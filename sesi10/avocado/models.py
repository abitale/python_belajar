from datetime import datetime
from config import db, ma


class Avocado(db.Model):
    __tablename__ = 'avocado'
    date = db.Column(db.DateTime)
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Float)
    avo_c = db.Column(db.Float)
    type = db.Column(db.Integer)
    regionid = db.Column(db.Integer)


class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Avocado
        # sqla_session = db.session
        load_instance = True
