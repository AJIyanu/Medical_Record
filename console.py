#!/usr/bin/python3
"""console app to test my developments"""


import cmd
import os

from models.base_person import Person
from models.base_institution import Institution
from models.base_record import Record
from datetime import date
from models.patient import Patient
from models.doctor import Doctor


classes = {
            "Person": Person,
            "Record": Record,
            "Institution": Institution,
            "Patient": Patient,
            "Doctor": Doctor
          }

class Medical_Record_Shell(cmd.Cmd):
    """shell for medical project testing"""

    prompt: str = "AJ Iyanu $: "

    def emptyline(self) -> None:
        """does nothing"""
        pass

    def do_quit(self, s) -> bool:
        """
        Quits the program
        """
        return True

    def help_quit(self) -> None:
        """
        documantation for quit
        """
        print("Quit command to exit the program")

    def do_Register(self, args) -> None:
        """Register a Person"""
        args = args.split()
        try:
            user = classes[args[0]]()
        except IndexError:
            print("Please Enter Personnel")
            return
        except KeyError:
            print(f"{args[0]} is not a personnel. Try Doctor/Patient")
            return
        try:
            user.firstname = args[2]
            user.surname = args[1]
            try:
                user.middlename = args[3]
            except IndexError:
                pass
        except IndexError:
            print("create [personel] [surname] [firstname] [middlename:optional]")
            return
        user.sex = input("Enter Sex: ")
        dd = input("Enter Date of Birth [Usage:YYYY/MM/DD]: ")
        dd = dd.split("/")
        try:
            user.dob = date(int(dd[0]), int(dd[1]), int(dd[2]))
        except Exception as e:
            print(e)
            print("Date not in the right format")
            print("User is not saved because dob cannot be empty, try again")
            return
        user.save()
        print(f"User saved Successfully, id: {user.id}, Name: {user.surname} {user.firstname}")

    def do_Show(self, args) -> None:
        """show all data"""
        try:
            args = args.split()
            users = classes[args[0]]().show_all()
            for user in users:
                print(f"{user} : {users[user]}")
        except IndexError:
            print("usage: Show [personnel]")
            return


    do_EOF = do_quit
    help_EOF = help_quit


if __name__ == "__main__":
    Medical_Record_Shell().cmdloop()
