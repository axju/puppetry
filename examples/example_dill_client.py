from puppetry import RemoteClient
import dill


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    client = RemoteClient((HOST, PORT), serializer=dill)
    print(client.hello())

    client.setup(name='Test')
    print(client.hello())

    client.name = 'puppetry'
    print(client.hello())
