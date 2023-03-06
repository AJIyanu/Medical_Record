#!/usr/bin/python3
"""console app to test my developments"""


import cmd
import os

from models.patient import Patient
from models.doctor import Doctor
from models.card import Card
from models.casefile import Casefile
from models.generalH import Hospital

classes = {
            "Patient": Patient,
            "Doctor": Doctor,
            "Casefile": Casefile,
            "Hospital": Hospital,
            "Card": Card
          }
