import os
from config import db
from datetime import datetime
from models import Person, Note

PEOPLE = [{
    'fname':
    'Doug',
    'lname':
    'Farrel',
    "notes": [
        ("Cool, a Hacktiv8 mini-blogging application!", "2019-01-06 22:17:54"),
        ("This could be useful", "2019-01-08 22:17:54"),
        ("Well, sort of useful", "2019-03-06 22:17:54"),
    ],
}, {
    'fname':
    'Hawk',
    'lname':
    'Amberstone',
    "notes": [
        (
            "I'm going to make really profound observations",
            "2019-01-07 22:17:54",
        ),
        (
            "Maybe they'll be more obvious than I thought",
            "2019-02-06 22:17:54",
        ),
    ],
}, {
    'fname':
    'Lucas',
    'lname':
    "Bridge",
    "notes": [
        ("Has anyone seen my eggs?", "2019-01-07 22:47:54"),
        ("I'm really late delivering these!", "2019-04-06 22:17:54"),
    ],
}]

if os.path.exists('people.db'):
    os.remove('people.db')

db.create_all()

for person in PEOPLE:
    p = Person(lname=person['lname'], fname=person['fname'])
    for note in person.get('notes'):
        content, timestamp = note
        p.notes.append(
            Note(
                content=content,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
            ))
    db.session.add(p)

db.session.commit()