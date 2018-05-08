from threading import Thread

from data import Data
from arm import Arm
from cli import Cli
from sock.server import Server


class Program:
    def __init__(self):
        self.data = Data()
        self.arm = Arm(self, emule=True)
        # table = self.data.get_table(2)
        self.cli = Cli(self)
        self.server = Server(self)

        self.t_cli = Thread(target=self.cli.run)
        self.t_cli.start()

        self.t_arm = Thread(target=self.arm.run)
        self.t_arm.start()

        self.t_server = Thread(target=self.server.run)


    def quit(self):
        self.arm.running = False

if __name__ == "__main__":
    p = Program()
