from puppetry.tools import send as _send

def _load_method(addr):
    cls = _send(addr, {'func': 'cls'})
    return [name for name in cls.__dict__]


def _load_variabl(addr):
    obj = _send(addr, {'func': 'obj'})
    return [name for name in obj.__dict__]


class Wrapper(object):

    def __init__(self, addr, method):
        self.addr = addr
        self.method = method

    def __call__(self, **kwargs):
        return _send(self.addr, {'method': self.method, 'kwargs': kwargs})


class RemoteClient(object):

    def __init__(self, host, port, load=True):
        self._meta = {'addr': (host, port), 'method': [], 'variabl': []}

        if load:
            self._meta['method'] = _load_method((host, port))
            self._meta['variabl'] = _load_variabl((host, port))


    def __getattr__(self, name):
        if name in self._meta['method']:
            return Wrapper(self._meta['addr'], name)

        if name in self._meta['variabl']:
            return _send(self._meta['addr'], {'variabl': name})


    def __setattr__(self, name, value):
        if name == '_meta':
            super(RemoteClient, self).__setattr__(name, value)
        elif name in self._meta['variabl']:
            _send(self._meta['addr'], {'variabl': name, 'value': value})
        else:
            raise Exception('No attribut named {}'.format(name))
