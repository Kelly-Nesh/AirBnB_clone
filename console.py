#!/usr/bin/python3
"""
a program called console.py that contains the entry point
of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class definition of  command interpreter:
    """
    prompt = "(hbnb) "

    def do_EOF(self, c):
        print()
        return True

    def do_quit(self, c):
        return True

    def emptyline(self):
        return

    def help_quit(self):
        print("""Quit the command interpreter""")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
