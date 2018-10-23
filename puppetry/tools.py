import socket
import hashlib
import hmac

#import pickle as serializer
import dill as serializer

def decode(data, key):
    pickled_data = serializer.dumps(data)
    digest =  hmac.new(key, pickled_data, hashlib.sha1).hexdigest()
    header = '%s' % (digest)
    return '{} {}'.format(header, pickled_data).encode()

def encode(data, key):
    recvd_digest, pickled_data = data.split(' ')
    new_digest = hmac.new(key, pickled_data.encode(), hashlib.sha1).hexdigest()
    if recvd_digest != new_digest:
        return False
        #print 'Integrity check failed'
    else:
        return serializer.loads(pickled_data)


def send(addr, data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(addr)
        #sock.sendall(serializer.dumps(data))
        #return serializer.loads(sock.recv(1024))
        sock.sendall(decode(data, '123'))
        return encode(sock.recv(1024), '123')
    finally:
        sock.close()
