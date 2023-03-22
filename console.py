#!/usr/bin/python3
"""console app to test my developments"""


import cmd
import os

from datetime import date
from models.patient import Patient
from models.doctor import Doctor
from models.generalH import Hospital
from models.casefile import caseFile
from models.maternity import Maternity
from models.healthcare import H_Facilities
from models.staffLogin import Staff
from models.patientLogin import User
import json


classes = {
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
        if args[0] == "Doctor":
            staff = Staff()
            staff.staff_id = user.id
            nin = input("Please Enter your 11 digit NIN: ")
            staff.nin = nin
            user.nin = nin
            staff.email = input("Please enter your email: ")
            staff.hashed_password = input("Enter your password: ")
            auth_inst = input("Enter your work institution IDs spaced: ")
            auth_inst = auth_inst.split()
            staff.auth_inst = json.dumps(auth_inst)
        if args[0] == "Patient":
            puser = User()
            puser.user_id = user.id
            nin = input("Please Enter your 11 digit NIN: ")
            user.nin = nin
            puser.nin = nin
            puser.email = input("Please Enter your email: ")
            puser.hashed_password = input("Enter your password: ")
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
        try:
            puser.save()
        except Exception:
            staff.save()
        print(f"User saved Successfully, id: {user.id} Name: {user.surname} {user.firstname}")

    def do_License(self, args) -> None:
        """adds hospital fof database use"""
        inst = {"general": Hospital, "maternity": Maternity}
        instype = input("Insitution type: ")
        if instype not in inst:
            print("not a valid institution (general/maternity)")
        hosp = inst[instype]()
        if args == "":
            print("Usage: License [Hospiatal name]")
            return
        hosp.name = args
        hosp.address = input("Enter Hospital Location: ")
        hosp.code = input("Input Hospital code: ")
        hosp.save()
        print(f"{hosp.name} has been licensed with id {hosp.facil}")

    def do_Open(self, args) -> None:
        """Register data for patient"""
        if args != "Casefile":
            print("You can only open Casefile")
            return
        doc = input("Enter your email: ")
        if "@" in doc:
            doc = Staff.search(email=doc)
        else:
            doc = Staff.search(nin=doc)
        if doc is None:
            print("You are not a valid User")
            return
        pwd = input("Enter Password: ")
        if not Staff.get_user(doc, pwd):
            print("wrong password")
            return
        doc_id = Staff.get_user(doc, pwd).get("id")
        code = input("Enter Hospital Code: ")
        if not Staff.validate_inst_code(doc_id, code):
            print("You are not authorized in this hosp or not a valid code")
            return
        validate = Doctor.user_by_id(doc_id)
        print(f"You opened a casefile as Doctor {validate.get('surname')}")
        validate = Maternity.search_by_code(code)
        if validate is None:
            validate = Hospital.search_by_code(code)
        if validate is None:
            print("Sorry! You need to be in a hospital to open a case file")
            return
        print(f"You opened a Case File @{validate['name']} {validate['__class__']}")
        pat = input("Enter Patient ID: ")
        validate = Patient.user_by_id(pat)
        if validate is None:
            print("You cant open a casefile non patient")
            return
        print(f"You have opened a casefile for {validate['surname']} {validate['firstname']}")
        record = caseFile(staff_id=doc, healthcare_id=hosp, patient_id=pat)
        record.symptoms = input("Patient's Complaint: ")
        record.testResult = input("Test Result (If any): ")
        record.diagnosis = input("Diagnosis: ")
        record.prescription = input("Prescription: ")
        record.save()
        print(f"Casefile saved with {record.id}")

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

    def do_History(self, args) -> None:
        """Print history record of patients"""
        if args == "":
            print("Usage: History <Personnel> <Personnel: Optional>")
            return
        args = args.split()
        if args[0] == "Doctor":
            doc_id = input("Please Enter your ID: ")
            try:
                if args[1] == "Patient":
                    pat_id = input("Please Enter Patients ID: ")
                    record = caseFile.search_doctor(staff_id=doc_id,
                                                    patient_id=pat_id)
                    if record is None:
                        print("Either you are not a Doctor, or you have not treated this patient")
                        return
            except IndexError:
                record = caseFile.search_doctor(staff_id=doc_id)
                if record is None:
                    print("You must be a doctor to view history")
                    return
            for data in record:
                pat_name = Patient.user_by_id(data['patient_id']).get('surname')
                hosp_name = H_Facilities.inst_by_id(data['healthcare_id']).get('name')
                print("<<<<<<<<<<----------->>>>>>>>>>")
                print(f"At {data['created_at']}, {pat_name} complained about {data['symptoms']}")
                print(f"Test Results are as follows; {data['testResult']}")
                print(f"You diagnosed {data['diagnosis']} and precribed {data['prescription']}")
                print("<<<<<<<<<<----------->>>>>>>>>>")
                print()
        elif args[0] == "Patient":
            pat_id = input("Please Enter your ID: ")
            try:
                if args[1] == "Doctor":
                    doc_id = input("Please Enter Doctor ID: ")
                    record = caseFile.search_patient(patient_id=pat_id,
                                                     staff_id=doc_id)
                    if record is None:
                        print("Either you are not a patient or the doctor has not treated you")
                        return
            except IndexError:
                record = caseFile.search_patient(patient_id=pat_id)
                if record is None:
                    print("You have not entered your ID")
                    return
            for data in record:
                doc_name = Doctor.user_by_id(data['staff_id']).get('surname')
                hosp_name = H_Facilities.inst_by_id(data['healthcare_id']).get('name')
                print("<<<<<<<<<<----------->>>>>>>>>>")
                print(f"At {data['created_at']}, You complained about {data['symptoms']}")
                print(f"Your Test Results are as follows; {data['testResult']}")
                print(f"Doctor {doc_name} diagnosed {data['diagnosis']} and precribed {data['prescription']} for you")
                print("<<<<<<<<<<----------->>>>>>>>>>")
                print()




    do_EOF = do_quit
    help_EOF = help_quit


if __name__ == "__main__":
    print(">>>>>>>>>>>>>>>> Welcome! This is Medical Record Console App <<<<<<<<<<<<<")
    Medical_Record_Shell().cmdloop()
    print("Goodbye! Thanks for banking with us!")
