#!/usr/bin/python3
"""
a program called console.py that contains the entry point
of the command interpreter
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    class definition of  command interpreter:
    """
    prompt = "(hbnb) "

    def do_create(self, args):
        if self.check_args("create", args):
            self.model = models.mdcls[args]()
            self.model.save()
            print(self.model.id)

    def do_show(self, args):
        if self.check_args("show", args):
            args = args.split(" ")
            key = args[0] + "." + args[1]
            # models.storage.reload()
            print(str(models.storage.all().get(key,
                                               "** no instance found **")))

    def do_destroy(self, args):
        if self.check_args("destroy", args):
            args = args.split(" ")
            key = args[0] + "." + args[1]
            # models.storage.reload()
            models.storage.all().pop(key,
                                     "** no instance found **")
            models.storage.save()

    def do_all(self, args):
        all_models = models.storage.all()
        strings = []
        if not args:
            for i in all_models.values():
                strings.append(str(i))
            print(strings)
        else:
            args = args.split(" ")
            for key, value in all_models.items():
                model_class = key.split(".")[0]
                if model_class == args[0]:
                    strings.append(str(value))
            print(strings)

    def do_update(self, args):
        if not self.check_args("update", args):
            return
        args = args.split(" ")
        key = args[0] + "." + args[1]
        if key not in models.storage.all().keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            model_update = models.storage.all()[key]
            model_update.__dict__[args[2]] = self.type_cast(args[3])
            models.storage.save()

    @staticmethod
    def type_cast(k):
        """Returns k according to its type"""
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

    @staticmethod
    def check_args(caller, args):
        if args:
            args = args.split(" ")
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in models.mdcls.keys():
            print("** class doesn't exist **")
        elif len(args) < 2 and caller in ["update", "destroy", "show"]:
            print("** instance id missing **")
        else:
            return True

    def do_EOF(self, c):
        print()
        return True

    def do_quit(self, c):
        return True

    def emptyline(self):
        return

    def help_quit(self):
        print("""Quit the command interpreter""")

    def help_create(self):
        message = """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        Usage: `create BaseModel`
        """
        print(message)

    def help_show(self):
        message = """
        Prints the string representation of an instance based
        on the class name and id.
        Usage: `show BaseModel 1234-1234-1234`
        """
        print(message)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
