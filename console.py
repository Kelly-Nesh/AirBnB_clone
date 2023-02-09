#!/usr/bin/python3
import cmd
"""creating interactive console"""


class HBNBCommand(cmd.Cmd):
    """Python interactive console"""
    prompt = "(hbnb) "

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
