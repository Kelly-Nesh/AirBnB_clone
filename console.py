#!/usr/bin/python3
import cmd

import models
from models.base_model import BaseModel
"""creating interactive console"""

class HBNBCommand(cmd.Cmd):
    """Python interactive console"""
    prompt = "(hbnb) "
    stoorage = models.storage
    
    def do_create(self, argv):
        """Creates a new instance of BaseModel, saves it (to JSON file)
        and prints the id"""
        args = check_args(argv)
        if args:
    
    def do_quit(self, qt):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing in case of empty line"""
        pass

    """quit in case of EOF from ctr d"""
    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
