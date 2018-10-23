puppetry
========

.. image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
  :alt: Gitter
  :target: https://gitter.im/axju/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link

.. image:: https://img.shields.io/twitter/url/https/github.com/axju/axju.svg?style=social
  :alt: Twitter
  :target: https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Faxju%2Fpuppetry

Remote objects, like puppet.

Install
-------
::

  pip install puppetry

Examples
--------

Server::

  from puppetry.server import RemoteServer

  class HelloWorld(object):
      def joke(self):
          return "Spam spam spam"

  server = RemoteServer(HelloWorld())
  server.start()

Client::

  from puppetry.client import RemoteClient

  class HelloWorld(object):
      def joke(self):
          return "Spam spam spam"

  server = RemoteClient(HelloWorld)
  print(server.send('joke'))


Development
-----------
Clone repo::

  git clone https://github.com/axju/puppetry.git

Create virtual environment and update dev-tools::

  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade wheel pip setuptools twine

Install local::

  pip install -e .

Publish the packages::

  python setup.py sdist bdist_wheel
  twine upload dist/*

Run some tests::

  tox
  python setup.py test
