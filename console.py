
#!/usr/bin/python3
""" AirBnB Console """

import cmd

class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the console"""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the console"""
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
