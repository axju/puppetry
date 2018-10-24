from puppetry import RemoteServer
import dill

class HelloWorld(object):

    def __init__(self, name=''):
        self.name = name

    def setup(self, name):
        self.name = name

    def hello(self, name=None):
        if name:
            return 'Hello ' + name
        return 'Hello ' + self.name


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = RemoteServer((HOST, PORT), obj=HelloWorld(), serializer=dill)
    server.start()
