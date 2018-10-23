from puppetry import RemoteClient


HOST, PORT = "localhost", 9999

client = RemoteClient(HOST, PORT)
print(client.hello())

client.setup(name='Test')
print(client.hello())

client.name = 'Axel'
print(client.hello())
