#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker


from app import app
from models import db, Pet

with app.app_context():

    # init faker generator
    fake = Faker()

    # delete rows in pet table
    Pet.query.delete()

    # create empty list
    pets = []

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # add some Pet instances
    for n in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    # insert Pet into pets table
    db.session.add_all(pets)

    # commit transaction
    db.session.commit()
