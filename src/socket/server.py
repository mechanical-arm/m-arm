import socket
from time import sleep
class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ("localhost", 7612)
        self.sock.bind(self.address)
        self.sock.listen(1)
        self.running = True

    def run(self):
        self.client, self.client_address = self.sock.accept()
        print("connect to %s" % str(self.client_address))
        while self.running:
            message = "ciao"
            data = message.encode()
            try: self.client.send(data)
            except: self.running = False
            sleep(0.4)
        print("connection lost")



s = Server()
s.run()
