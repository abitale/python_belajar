import os
from config import db
from models import Person

PEOPLE =  [
    {'fname': 'Doug','lname': 'Farrel'},
    {'fname': 'Hawk','lname': 'Amberstone'},
    {'fname': 'Lucas','lname': "Bridge"}
]


if os.path.exists('people.db'):
    os.remove('people.db')

db.create_all()

for person in PEOPLE:
    p = Person(lname=person['lname'], fname=person['fname'])
    db.session.add(p)

db.session.commit()