#!/usr/bin/env python3

import random
import string
import datetime
import uuid
from faker import Faker
from models.doctor import Doctor
from models.patient import Patient
from models.loginauth import PersonAuth

fake = Faker()

# Generate 10 random doctors
for i in range(0, 20):
    diction = {}
    diction['id'] = str(uuid.uuid4())
    diction['address'] = fake.address()
    diction['nxt_of_kin'] = fake.name()
    diction['phone'] = "2348122420302"
    diction['created_at'] = datetime.datetime.now()
    diction['updated_at'] = diction['created_at']
    diction['nin'] = ''.join(random.choices(string.digits, k=11))
    diction['firstname'] = fake.first_name()
    diction['surname'] = fake.last_name()
    diction['middlename'] = fake.first_name()
    diction['sex'] = random.choice(['Male', 'Female'])
    diction['dob'] = fake.date_of_birth(minimum_age=25, maximum_age=70)

    '''print(f"INSERT INTO `Patient` (`address`, `nxt_of_kin`, `phone`, `id`, `created_at`, `updated_at`, `nin`, `firstname`, `surname`, `middlename`, `sex`, `dob`) VALUES ('{address}', '{nxt_of_kin}', '{phone}', '{id}', '{created_at}', '{updated_at}', '{nin}', '{firstname}', '{surname}', '{middlename}', '{sex}', '{dob}');")
    '''
    print(diction)
    Doc = Patient(**diction)
    Doc.nin = diction['nin']
    # Doc.authinst = "GENOYSK293"
    login = PersonAuth()
    login.email = f"{diction['surname']}@gmail.com"
    login.set_password("iloverose")
    login.person_id = diction['id']
    Doc.save()
    login.save()
