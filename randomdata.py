#!/usr/bin/env python3

from faker import Faker
import random
import string
import datetime
import uuid

fake = Faker()

# Generate 10 random doctors
for i in range(1, 11):
    id = uuid.uuid4()
    address = fake.address()
    nxt_of_kin = fake.name()
    phone = fake.phone_number()
    created_at = datetime.datetime.now()
    updated_at = created_at
    nin = ''.join(random.choices(string.digits, k=11))
    firstname = fake.first_name()
    surname = fake.last_name()
    middlename = fake.mid
    sex = random.choice(['Male', 'Female'])
    dob = fake.date_of_birth(minimum_age=25, maximum_age=70)

    print(f"INSERT INTO `Doctor` (`address`, `nxt_of_kin`, `phone`, `id`, `created_at`, `updated_at`, `nin`, `firstname`, `surname`, `middlename`, `sex`, `dob`) VALUES ('{address}', '{nxt_of_kin}', '{phone}', '{id}', '{created_at}', '{updated_at}', '{nin}', '{firstname}', '{surname}', '{middlename}', '{sex}', '{dob}');")
