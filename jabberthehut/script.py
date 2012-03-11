import configparser
import getpass
from logging.config import fileConfig
import os
import sys

from zope.dottedname.resolve import resolve

from jabberthehut.bot import Bot

DEFAULTS = {
    'handlers': ' '.join([
        'jabberthehut.handlers.html_title',
        'jabberthehut.handlers.echo',
        'jabberthehut.handlers.source',
        ]),
    }

def main(argv=sys.argv):
    if len(argv) == 1:
        config_filename = os.path.join([os.getcwd(), 'jabber-the-hut.ini'])
    else:
        config_filename = argv[1]

    parser = configparser.ConfigParser()    
    parser.read(config_filename)

    if parser.has_section('loggers'):
        fileConfig(
            config_filename,
            dict(__file__=config_filename,
                 here=os.path.dirname(config_filename)),
            )

    config = DEFAULTS.copy()
    config.update(dict(parser.items(parser.sections()[0])))

    config.setdefault('nick', 'jabba')
    if 'password' not in config:
        config['password'] = getpass.getpass(
            "Password for {}: ".format(config['jid']))

    config['handlers'] = [resolve(name) for name in config['handlers'].split()]

    xmpp = Bot(**config)
    xmpp.connect()
    xmpp.process(block=True)
