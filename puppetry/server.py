import socket

from puppetry.tools import _send, _recv

class JsonServer(object):

    socket = None

    def __init__(self, host='localhost', port=12345):
        super(JsonServer, self).__init__()
        self.host = host
        self.port = port
        self.bind()

    def __del__(self):
        self.close()

    def bind(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket .setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.settimeout(1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)

    def accept(self):
        if self.client: self.client.close()
        if not self.socket: self.bind()

        while True:
            try:
                self.client, addr = self.socket.accept()
                break
            except socket.timeout:
                pass
            except Exception as e:
                break

        return self

    def send(self, data):
        if not self.client:
            raise Exception('Cannot send data, no client is connected')
        _send(self.client, data)
        return self

    def recv(self):
        if not self.client:
            raise Exception('Cannot receive data, no client is connected')
        return _recv(self.client)

    def close(self):
        if self.client:
            self.client.close()
            self.client = None
        if self.socket:
            self.socket.close()
            self.socket = None


class RemoteServer(JsonServer):
    client = None

    def __init__(self, obj, host='localhost', port=12345):
        super(RemoteServer, self).__init__(host, port)
        self.obj = obj

    def start(self):
        while True:
            try:
                if not self.client: self.accept()

                data = self.recv()
                method_to_call = getattr(self.obj, data['name'])
                result = method_to_call(**data['kwargs'])
                self.send(result)

            except KeyboardInterrupt:
                break

            finally:
                self.close()
