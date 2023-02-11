#!/usr/bin/python3
import cmd
import json
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
                saved = saved[class_show[1]]
                s_id = saved['id']
                updated_at = saved['updated_at']
                created_at = saved['created_at']
                to_show = BaseModel(id=s_id, created_at=created_at, 
                updated_at=updated_at)
                print(to_show)

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

    def do_all(self, class_all):
        """Prints all string representations of instances based or not
	on the class name. """
        rt = []
        if not class_all or class_all == 'BaseModel':
            all_saved = models.engine.storage.all()
            cp_saved = all_saved.values()
            for itm in cp_saved:
                id = itm['id']
                updated_at = itm['updated_at']
                created_at = itm['created_at']
                old_instance = BaseModel(id=id, created_at=created_at, 
                updated_at=updated_at)
                rt.append(str(old_instance))
            print(rt)
            del(rt)
        elif class_all != 'BaseModel':
                print("** class doesn't exist **")
    
    def do_update(self, class_update):
        """Updates an instance based on class name and id by adding or updating
        attributes and saves the changes to json file"""
        class_update = class_update.split(' ')
        saved = models.engine.storage.all()
        if not class_update[0]:
            print("** class name missing **")
        elif class_update[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(class_update) < 2:
            print("** instance id missing **")
        elif class_update[1] not in saved:
            print("** no instance found **")
        elif len(class_update) < 3:
            print("** attribute name missing **")
        elif len(class_update) < 4:
            print("** value missing **")
        else:
            old_inst = saved[class_update[1]]
            id = old_inst['id']
            created_at = old_inst['created_at']
            updated_at = old_inst['updated_at']
            to_update = BaseModel(id=id, created_at=created_at,
            updated_at=updated_at)
            setattr(to_update, class_update[2], 
                HBNBCommand.type_cast(class_update[3]))
            to_update.save()
            models.engine.storage.reload()
    
    @staticmethod
    def type_cast(k):
        try:
            k=int(k)
        except ValueError:
            try:
                k=float(k)
            except ValueError:
                try:
                    k=str(k)
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
        print('\n'.join(["Takes two arguments: Class and Instance Id",
        "Usage: ``show BaseModel 79734628-ebca-4188-81fe-932c7a967b84``"]))
    
    def help_destroy(self):
    	print('\n'.join(["Deletes an instance based on the class name and id and saves changes.",
	"Usage: ``destroy BaseModel 956b78db-80b5-45b2-9fa6-a98eda4f9043``"]))

    def help_all(self):
        print('\n'.join(["prints all string representation of all instances",
	"whether specified class or not", 
	"Usage: ``all BaseModel`` or ``all``"]))

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

