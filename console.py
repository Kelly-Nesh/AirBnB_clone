#!/usr/bin/python3
import cmd

import models
from models.base_model import BaseModel
"""creating interactive console"""

class HBNBCommand(cmd.Cmd):
    """Python interactive console"""
    prompt = "(hbnb) "
    stoorage = models.storage
    
    def do_create(self, class_create):
        """Creates a new instance of BaseModel, saves it (to JSON file)
        and prints the id"""
        if not class_create:
            print("** class name missing **")
        elif class_create == 'BaseModel':
            Base_insta = BaseModel()
            Base_insta.save()
            print(Base_insta.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, class_show):
        """Prints the string representation of an instance based on
        the class name and id"""
        class_show = class_show.split(' ')
        if not class_show[0]:
            print("** class name missing **")
        elif class_show[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(class_show) < 2:
            print("** instance id missing **")
        else:
            models.engine.storage.reload()
            saved = models.storage.all()
            if class_show[1] not in saved:
                print("** no instance found **")
            else:
                old = BaseModel(saved)
                print(old)

    def do_destroy(self, class_destroy):
        """Deletes an instance based on the class name and id
        and saves the changes."""
        class_destroy = class_destroy.split(' ')
        if not class_destroy[0]:
            print("** class name missing **")
        elif class_destroy[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(class_destroy) < 2:
            print("** instance id missing **")
        else:
            models.engine.storage.reload()
            saved = models.storage.all()
            if class_destroy[1] not in saved:
                print("** no instance found **")
            else:
                del(saved[class_destroy[1]])
                models.engine.storage.save()

    def help_show(self):
        print('\n'.join(["Takes two arguments: Class and Instance Id",
        "Usage: ``show BaseModel 79734628-ebca-4188-81fe-932c7a967b84``"]))
    
    def help_destroy(self):
    	print('\n'.join(["Deletes an instance based on the class name and id and saves changes.",
	"Usage: ``destroy BaseModel 956b78db-80b5-45b2-9fa6-a98eda4f9043``"]))
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
