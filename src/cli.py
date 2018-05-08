from threading import Thread
import cmd


from sock.server import Server


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

    def do_showTable(self, args):
        print(self.program.table)

    def do_newNumber(self, args):
        print(self.program.table.new_num(int(args)))

    def do_server(self, args):
        print("\nApertura server\n")
        server = Server(self.program)
        t_server = Thread(target=server.run)
        t_server.start()
        print("\nServer aperto\n")



    def run(self):
        self.cmdloop()
