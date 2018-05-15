from threading import Thread

from data import Data
from arm import Arm
from cli import Cli

class Program:
    def __init__(self, arg):
        # argparse
        if arg[1] == "emule": emule = True
        else: emule = False

        self.data = Data()
        self.arm = Arm(self, emule)
        self.table = self.data.get_table(48)

        self.cli = Cli(self)

        # Thread
        self.t_cli = Thread(target=self.cli.run)
        self.t_arm = Thread(target=self.arm.run)

    def start(self):
        self.t_cli.start()
        self.t_arm.start()

    def quit(self):
        self.arm.running = False

if __name__ == "__main__":
    import sys
    p = Program(sys.argv)
    p.start()
