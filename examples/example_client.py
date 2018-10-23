from puppetry.client import RemoteClient

class HelloWorld(object):
    def joke(self):
        return "Spam spam spam"

server = RemoteClient(HelloWorld)
print(server.send('joke'))
