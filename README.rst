puppetry
========

.. image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
  :alt: Gitter
  :target: https://gitter.im/axju/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link

.. image:: https://img.shields.io/twitter/url/https/github.com/axju/axju.svg?style=social
  :alt: Twitter
  :target: https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Faxju%2Fpuppetry

Remote objects, like puppet.

For a small project I need to communicate between two process. In one process I
have a class which create an object. The other process should access the
functions and variables of this object. The process play with the object like an
puppetry.

Install
-------
::

  pip install puppetry

Basic usage
-----------
Example class::

  class HelloWorld(object):

      def __init__(self, name=''):
          self.name = name

      def hello(self, name=None):
          if name: return 'Hello ' + name
          return 'Hello ' + self.name

Server::

  from puppetry import RemoteServer

  server = RemoteServer((HOST, PORT), obj=HelloWorld('world'))
  server.start()

Client::

  from puppetry import RemoteClient

  client = RemoteClient((HOST, PORT))
  print(client.hello())

  client.name = 'puppetry'
  print(client.hello())

See more examples in the example folder.

Development
-----------
Clone repo::

  git clone https://github.com/axju/puppetry.git

Create virtual environment and update dev-tools::

  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade wheel pip setuptools twine tox

Install local::

  pip install -e .

Publish the packages::

  python setup.py sdist bdist_wheel
  twine upload dist/*

Run some tests::

  tox
  python setup.py test
