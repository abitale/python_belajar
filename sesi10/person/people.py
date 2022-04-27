from flask import make_response, abort
from config import db
from models import Person, PersonSchema


def read_all():
    people = Person.query.order_by(Person.lname).all()

    person_schema = PersonSchema(many=True)
    return person_schema.dump(people)


def read_one(id):
    person = Person.query.filter(Person.person_id == id).one_or_none()

    if person is not None:
        person_schema = PersonSchema()
        return person_schema.dump(person)

    else:
        abort(404, "Person not found for id: {id}".format(id=id))


def create_person(person):
    fname = person.get('fname')
    lname = person.get('lname')

    existing_person = (Person.query.filter(Person.fname == fname).filter(
        Person.lname == lname).one_or_none())

    if existing_person is None:
        person_schema = PersonSchema()
        new_person = person_schema.load(person, session=db.session)

        db.session.add(new_person)
        db.session.commit()

        return person_schema.dump(new_person), 201

    else:
        abort(
            409, "Person {fname} {lname} already exist".format(fname=fname,
                                                               lname=lname))


def update(id, person):
    update_person = Person.query.filter(Person.person_id == id).one_or_none()

    fname = person.get('fname')
    lname = person.get('lname')

    existing_person = Person.query.filter(Person.fname == fname).filter(
        Person.lname == lname).one_or_none()

    if update_person is None:
        abort(404, "Person not found with id: {id}".format(id=id))
    elif existing_person is not None and existing_person.person_id != id:
        abort(
            409, "Person {fname} {lname} already exist".format(fname=fname,
                                                               lname=lname))
    else:
        person_schema = PersonSchema()
        update = person_schema.load(person, session=db.session)

        update.person_id = update_person.person_id

        db.session.merge(update)
        db.session.commit()

        return person_schema.dump(update_person), 200


def delete_person(id):
    person = Person.query.filter(Person.person_id == id).one_or_none()

    if person is not None:
        db.session.delete(person)
        db.session.commit()

        return make_response("Person {id} successfuly deleted".format(id=id),
                             200)
    else:
        abort(404, "Person not found by {id}".format(id=id))
