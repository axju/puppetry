import pickle

def _send(socket, data):
    try:
        serialized = pickle.dumps(data)
    except (TypeError, ValueError) as e:
        raise Exception('You can only send JSON-serializable data')

    # send the length of the serialized data first
    socket.send('{}\n'.format(len(serialized)).encode())

    # send the serialized data
    socket.send(serialized)


def _recv(socket):
    # read the length of the data, letter by letter until we reach EOL
    length_str = ''
    while True:
        char = socket.recv(1).decode()
        if char == '\n': break
        length_str += char
    total = int(length_str)

    serialized = socket.recv(total)
    try:
        deserialized = pickle.loads(serialized)
    except (TypeError, ValueError) as e:
        raise Exception('Data received was not in JSON format')

    return deserialized
