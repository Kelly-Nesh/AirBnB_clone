#!/usr/bin/python3
import cmd
import json
import models
from models.base_model import BaseModel
from models import classes
"""creating interactive console"""


class HBNBCommand(cmd.Cmd):
    """Python interactive console"""
    prompt = "(hbnb) "
    storage = models.storage

    def do_create(self, class_create):
        """Creates a new instance of BaseModel, saves it (to JSON file)
        and prints the id"""
        if not class_create:
            print("** class name missing **")
        elif class_create not in classes:
            print("** class doesn't exist **")
        else:
            class_create = classes[class_create]
            insta = class_create()
            print(insta.id)
            insta.save()

    def do_show(self, class_show):
        """Prints the string representation of an instance based on
        the class name and id"""
        class_show = class_show.split(' ')
        if not class_show[0]:
            print("** class name missing **")
        elif class_show[0] not in classes:
            print("** class doesn't exist **")
        elif len(class_show) < 2:
            print("** instance id missing **")
        else:
            models.storage.reload()
            saved = models.storage.all()
            old = class_show[0] + '.' + class_show[1]
            if old not in saved:
                print("** no instance found **")
            else:
                print(saved[old])

    def do_destroy(self, class_destroy):
        """Deletes an instance based on the class name and id
        and saves the changes."""
        class_destroy = class_destroy.split(' ')
        if not class_destroy[0]:
            print("** class name missing **")
        elif class_destroy[0] not in classes:
            print("** class doesn't exist **")
        elif len(class_destroy) < 2:
            print("** instance id missing **")
        else:
            models.storage.reload()
            saved = models.storage.all()
            key = class_destroy[0] + '.' + class_destroy[1]
            if key not in saved:
                print("** no instance found **")
            else:
                del(saved[key])
                models.storage.save()

    def do_all(self, class_all):
        """Prints all string representations of instances based or
        not on the class name."""
        stored = models.storage.all().values()
        rt = []
        if not class_all:
            for m in stored:
                rt.append(str(m))
            print(rt)
        elif class_all not in classes:
            print("** class doesn't exist **")
        else:
            for saved_instance in stored:
                # for later when we need to show for the exact class
                # if class_all == saved_instance.__class__.__name__:
                rt.append(str(saved_instance))
            print(rt)

    def do_update(self, class_update):
        """Updates an instance based on class name and id by adding or updating
        attributes and saves the changes to json file"""
        class_update = class_update.split(' ')
        saved = models.storage.all()
        if not class_update[0]:
            print("** class name missing **")
        elif class_update[0] not in classes:
            print("** class doesn't exist **")
        elif len(class_update) < 2:
            print("** instance id missing **")
        elif len(class_update) < 3:
            print("** attribute name missing **")
        elif len(class_update) < 4:
            print("** value missing **")
        else:
            key = class_update[0] + '.' + class_update[1]
            if key not in saved:
                print("** no instance found **")
                return
            stored = saved[key]
            setattr(stored, class_update[2], class_update[3])
            models.storage.save()

    @staticmethod
    def type_cast(k):
        """returns the casted value of k according to its type"""
        try:
            k = int(k)
        except ValueError:
            try:
                k = float(k)
            except ValueError:
                try:
                    k = str(k)
                except ValueError:
                    pass
                else:
                    return k
            else:
                return k
        else:
            return k

    # HELP METHODS
    def help_show(self):
        """Prints a help doc of the command show"""
        print('\n'.join(["Takes two arguments: Class and Instance Id",
                         "Usage: ``\
                         show BaseModel <id>``"]))

    def help_destroy(self):
        """Prints a help doc of the command destroy"""
        print('\n'.join(["Deletes an instance based on the \
                        class name and id and saves changes.",
                        "Usage: \
                        ``destroy BaseModel <id>``"]))

    def help_all(self):
        """Prints a help doc of the command all"""
        print('\n'.join(["\tprints all string representation of all instances",
                        "\twhether class is specified or not",
                         "\t\tUsage: ``all BaseModel`` or ``all``"]))

    # OVERRIDEN METHODS
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
