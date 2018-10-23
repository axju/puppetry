from puppetry.server import RemoteServer

class HelloWorld(object):
    def joke(self):
        return "Spam spam spam"

server = RemoteServer(HelloWorld())
server.start()
