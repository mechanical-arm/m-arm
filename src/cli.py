from threading import Thread
import cmd

from sock.server import Server


class Cli(cmd.Cmd):
    def __init__(self, program):
        cmd.Cmd.__init__(self)
        self.program = program
        self.prompt = '>>> '

    def do_quit(self, args):
        print("\nArresto sistema in corso...\n")
        self.program.quit()
        return 1

    def do_state(self, args):
        print(self.program.arm)

    def do_showTable(self, args):
        print(self.program.table)

    def do_goBack(self, args):
        self.program.arm.goto_back = True

    def do_goto(self, args):
        x, y = map(int,args.split())
        print("goto %d %d " %(x,y))
        arm = self.program.arm
        arm.offset_time()
        arm.pos = (x,y)
        arm.goto_pos = True
        arm.goto_x = True
        arm.goto_y = True

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
