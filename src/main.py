from threading import Thread

from data import Data
from arm import Arm
from cli import Cli
from sock.server import Server

class Program:
    def __init__(self):
        self.data = Data()
        self.arm = Arm(self, emule=True)
        table = self.data.get_table(10)
        print(table)
        self.cli = Cli(self)
        self.server = Server(self)

        # Thread
        self.t_cli = Thread(target=self.cli.run)
        self.t_arm = Thread(target=self.arm.run)
        self.t_server = Thread(target=self.server.run)

    def start(self):
        self.t_cli.start()
        self.t_arm.start()

    def quit(self):
        self.arm.running = False
        self.server.running = True

if __name__ == "__main__":
    p = Program()
    p.start()
