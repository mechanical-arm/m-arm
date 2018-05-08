import socket
from time import sleep

class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_adress = ("localhost", 7612)
        self.running = True

    def run(self):
        self.sock.connect(self.server_adress)
        while self.running:
            data = self.sock.recv(1024)
            message = data.decode()
            print(message)
            sleep(0.4)

c = Client()

c.run()
