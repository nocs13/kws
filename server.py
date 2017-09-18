import socket

class kwsServer():
    def __init__(self):
        self.server = None

    def __init__(self, ip, port):
        self.server = socket.socket(socket.AF_INET, scket.SOCK_STREAM)

        self.server.bind(ip, port)

        self.listen(10)

        
