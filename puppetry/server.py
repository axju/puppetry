import socketserver
import threading
#import pickle as serializer
import dill as serializer

from puppetry.tools import decode, encode

class PuppetryHandler(socketserver.BaseRequestHandler):

    def method(self, data):
        method_to_call = getattr(self.server.obj, data['method'])
        if 'kwargs' in data:
            return method_to_call(**data['kwargs'])
        else:
            return method_to_call()

    def variabl(self, data):
        if 'value' in data:
            return setattr(self.server.obj, data['variabl'], data['value'])
        return getattr(self.server.obj, data['variabl'])

    def func(self, data):
        if data['func'] == 'cls':
            return self.server.obj.__class__

        if data['func'] == 'obj':
            return self.server.obj

    def handle(self):
        serialized = self.request.recv(1024)
        print(serialized)
        #data = serializer.loads(serialized)
        data = encode(serialized, '123')
        print(data)
        #print('recv() ->', data)

        if 'method' in data:
            result = self.method(data)

        if 'variabl' in data:
            result = self.variabl(data)

        if 'func' in data:
            result = self.func(data)

        #self.request.send(serializer.dumps(result))
        self.request.send(decode(result, '123'))


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class RemoteServer(object):

    def __init__(self, host, port, obj=None):
        self.server = socketserver.TCPServer((host, port), PuppetryHandler)
        self.server.obj = obj

    @property
    def obj(self):
        return self.server.obj

    @obj.setter
    def obj(self, value):
        self.server.obj = value

    def start(self):
        self.server.serve_forever()


class RemoteServerThread(RemoteServer):

    def __init__(self, host, port, obj=None):
        self.server = ThreadedTCPServer((host, port), PuppetryHandler)
        self.thread = threading.Thread(target=self.server.serve_forever)

        self.server.obj = obj

    def __del__(self):
        self.server.shutdown()
        self.server.server_close()

    def start(self):
        self.thread.daemon = True
        self.thread.start()
