from flask import make_response, abort
from config import db
from models import Avocado, AvocadoSchema


def read_all():
    avocado = Avocado.query.all()

    avocado_schema = AvocadoSchema(many=True)
    return avocado_schema.dump(avocado)