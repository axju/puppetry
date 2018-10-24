import argparse
import subprocess
from datetime import datetime

from puppetry import __about__ as info
from puppetry import RemoteServer, RemoteClient

def log(s):
    print('[*] {} - {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), s))

class Cmd(object):
    def execute(self, cmd):
        log('execute command: {}'.format(cmd))
        result = subprocess.Popen(
            cmd, shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        ).stdout.read().decode('iso8859-1')
        print(result)
        return result

def main():
    parser = argparse.ArgumentParser(
        description=info.__summary__,
        epilog=info.__copyright__,
    )
    parser.add_argument(
            '--version',
            action='version',
            version='%(prog)s ' + info.__version__
        )

    subparsers = parser.add_subparsers(help='commands', dest='action')
    parser_server = subparsers.add_parser('server', help='Start the server')
    parser_server.add_argument('--host', type=str, default='localhost')
    parser_server.add_argument('--port', type=int, default=0)

    parser_client = subparsers.add_parser('client', help='Run a client command')
    parser_client.add_argument('cmd', type=str)
    parser_client.add_argument('--host', type=str, default='localhost')
    parser_client.add_argument('--port', type=int, default=0)

    parser_shell = subparsers.add_parser('shell', help='Run a remote shell')
    parser_shell.add_argument('--host', type=str, default='localhost')
    parser_shell.add_argument('--port', type=int, default=0)


    args = parser.parse_args()

    if args.action == 'server':

        server = RemoteServer((args.host, args.port), obj=Cmd())
        addr = server.server.server_address
        log("run server '{}' on port {}".format(*addr))
        server.start()
        return

    if args.action == 'client':
        client = RemoteClient((args.host, args.port))
        result = client.execute(cmd=args.cmd)
        print(result.decode('iso8859-1'))
        return

    if args.action == 'shell':
        client = RemoteClient((args.host, args.port))
        log("start remote shell")
        while True:
            try:
                cmd = str(input('>>> '))
                result = client.execute(cmd=cmd)
                print(result)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)

        print('Exit connection')
        return

    parser.print_help()


if __name__ == '__main__':
    main()
