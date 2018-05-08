import socket
from time import sleep

class Server:
    def __init__(self, program):
        self.program = program
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ("localhost", int(open("sock/port").read()))
        self.sock.bind(self.address)
        self.sock.listen(1)
        self.running = False

    def run(self):
        self.running = True
        self.client, self.client_address = self.sock.accept()
        print("connect to %s" % str(self.client_address))
        while self.running:
            message = str(self.program.arm)
            data = message.encode()
            try: self.client.send(data)
            except: self.running = False
            sleep(0.4)
        print("connection lost")
