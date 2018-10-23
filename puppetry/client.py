import socket, pickle

from puppetry.tools import _send, _recv

class JsonClient(object):
    socket = None

    def __del__(self):
        self.close()

    def connect(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(1)
        self.socket.connect((host, port))
        return self

    def send(self, data):
        if not self.socket:
            raise Exception('You have to connect first before sending data')
        _send(self.socket, data)
        return self

    def recv(self):
        if not self.socket:
            raise Exception('You have to connect first before receiving data')
        return _recv(self.socket)

    def recv_and_close(self):
        data = self.recv()
        self.close()
        return data

    def close(self):
        if self.socket:
            self.socket.close()
        self.socket = None


class RemoteClient(object):

    def __init__(self, cls, host='localhost', port=12345):
        super(RemoteClient, self).__init__()
        self.cls = cls

        self.client = JsonClient()
        self.client.connect(host, port)

    def __del__(self):
        self.close()

    def close(self):
        self.client.close()

    def send(self, name, **kwargs):
        self.client.send({'name': name, 'kwargs': kwargs})
        return self.client.recv()
        #print(result)
