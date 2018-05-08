import socket
from time import sleep
from os import path

class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        path_port = path.join(path.dirname(__file__),"port")
        self.server_adress = ("localhost", int(open(path_port).read()))
        self.running = True

    def run(self):
        try:
            self.sock.connect(self.server_adress)
            while self.running:
                data = self.sock.recv(1024)
                message = data.decode()
                print(message)
                sleep(0.4)
        except:
            print("connection lost")

c = Client()
c.run()
