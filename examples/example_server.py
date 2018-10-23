from puppetry import RemoteServer

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

    server = RemoteServer(HOST, PORT)
    server.obj = HelloWorld()



    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.start()
