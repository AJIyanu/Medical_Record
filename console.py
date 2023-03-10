#!/usr/bin/python3
"""console app to test my developments"""


import cmd
import os

from models.base_person import Person
from models.base_institution import Institution
from models.base_record import Record


classes = {
            "Person": Person,
            "Record": Record,
            "Institution": Institution
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
        

    do_EOF = do_quit
    help_EOF = help_quit


if __name__ == "__main__":
    Medical_Record_Shell().cmdloop()
