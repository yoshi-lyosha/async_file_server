from aiohttp import web
from urllib.parse import urlparse
import argparse
import errno
import os
import sys


def parse_args():
    """Настройка argsparse"""
    parser = argparse.ArgumentParser()
    parser.add_argument('server', help='localhost_ip:port')
    return parser.parse_args()


def parse_ip_port(server):
    """Парсинг ip:port"""
    parsed = urlparse('//{}'.format(server))
    ip = parsed.hostname
    port = parsed.port
    return ip, port


if __name__ == '__main__':
    parser_args = parse_args()
    server_ip, server_port = parse_ip_port(parser_args.server)
    if server_port is None:
        print('You need to write port')
        sys.exit(errno.EINVAL)

    project_root = os.path.abspath(os.path.curdir)
    app = web.Application()
    app.router.add_static('/get/', path=project_root)
    web.run_app(app, host=server_ip, port=server_port)
