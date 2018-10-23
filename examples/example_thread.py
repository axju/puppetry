from puppetry import RemoteServerThread,  RemoteClient

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

    server = RemoteServerThread(HOST, PORT, obj=HelloWorld())
    server.start()

    client = RemoteClient(HOST, PORT)
    print(client.hello())

    #client.setup(name='Test')
    #print(client.hello())

    #client.name = 'AxJu'
    #print(client.hello())
