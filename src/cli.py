import cmd

class Cli(cmd.Cmd):
    def __init__(self, program):
        cmd.Cmd.__init__(self)
        self.program = program
        self.prompt = 'BMP > '

    def do_quit(self, args):
        print("\nArresto sistema in corso...\n")
        self.program.quit()
        return 1

    def do_state(self, args):
        print(self.program.arm)

    def do_server(self, args):
        server = self.program.server
        if server.running:
            print("\nChiusura server\n")
            server.running = False
        else:
            print("\nApertura server\n")
            self.program.t_server.start()


    def run(self):
        self.cmdloop()
