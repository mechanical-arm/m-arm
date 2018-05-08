import cmd

class Cli(cmd.Cmd):
    def __init__(self, program):
        cmd.Cmd.__init__(self)
        self.program = program
        self.prompt = 'BMP > '

    def do_quit(self, arg):
        print("\nArresto sistema in corso...")

    def do_state(self, args):
        print("__STATE__")
        print(self.program.arm)

    def run(self):
        self.cmdloop()
