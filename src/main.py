from data import Data
from arm import Arm
from cli import Cli


class Program:
    def __init__(self):
        self.data = Data()
        self.arm = Arm(self, emule=True)
        # table = self.data.get_table(2)
        self.cli = Cli(self)
        self.cli.run()


if __name__ == "__main__":
    p = Program()
