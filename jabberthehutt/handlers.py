import functools
import os
from subprocess import Popen
from subprocess import PIPE
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import urlparse

from pyquery import PyQuery as pq

from .parseurls import grab_urls

def cmd(name):
    """
      >>> class Bot:
      ...     nick = 'jabba'
      >>> bot = Bot()
      >>> @cmd('mycommand')
      ... def mycommand(bot, msg, arg):
      ...     print('Called with "{}"'.format(arg))
      >>> mycommand(bot, {'body': 'jabba: hey'})
      >>> mycommand(bot, {'body': 'jabba: mycommand do'})
      Called with "do"
      >>> mycommand(bot, {'body': 'jabba: mycommand'})
      Called with ""
      >>> mycommand(bot, {'body': 'mycommand do'})
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(bot, msg):
            result = _extract_command(bot, msg)
            if result and result[0].lower() == name:
                arg = None
                if len(result) > 1:
                    arg = result[1]
                return func(bot, msg, arg)
        return wrapper
    return decorator

def _extract_command(bot, msg):
    """
      >>> class Bot:
      ...     nick = 'jabba'
      >>> bot = Bot()
      >>> def extr(text):
      ...     return _extract_command(bot, {'body': text})
      >>> extr("jabba, what's up")
      ["what's", 'up']
      >>> extr('JABBA can u hear me')
      ['can', 'u hear me']
      >>> extr('jabba:')
      >>> extr('jabba')
      >>> extr('Nothing to see here')
    """
    if msg['body'].lower().startswith(bot.nick):
        args = msg['body'].split()[1:]
        if args:
            return [args[0], ' '.join(args[1:])]

def html_title(bot, msg):
    """
      >>> class Bot:
      ...     cache = {}
      >>> bot = Bot()
      >>> html_title(
      ...     bot,
      ...     {'body': 'Check this http://danielnouri.org out'},
      ...     )
      ["Daniel Nouri's Homepage · danielnouri.org"]
      >>> html_title(
      ...     bot,
      ...     {'body': 'http://docs.python.org/py3k/tutorial/'},
      ...     )
      ['The Python Tutorial — Python v3.2.2 documentation · docs.python.org']
      >>> html_title(
      ...     bot,
      ...     {'body': 'http://danielnouri.org'},
      ...     )
      []
      >>> html_title(
      ...     bot,
      ...     {'body': 'http://danielnouri.org/favicon.ico'},
      ...     )
      []
    """
    seen = bot.cache.setdefault('html_title.seen', [])
    messages = []
    for url in grab_urls(msg['body']):
        if url in seen:
            continue
        else:
            seen.append(url)
        try:
            document = pq(url=url)
        except URLError:
            continue
        try:
            document_title = document('title').text()
        except AttributeError:
            continue
        if document_title:
            netloc = urlparse(url).netloc
            messages.append("{} · {}".format(document_title, netloc))
    seen[:-10] = []
    return messages

@cmd('echo')
def echo(bot, msg, arg):
    return '{}: {}'.format(msg['from'], arg)

@cmd('source')
def source(bot, msg, arg):
    return 'https://github.com/dnouri/jabber-the-hut'

@cmd('fortune')
def fortune(bot, msg, arg):
    """
      >>> class Bot:
      ...     nick = 'jabba'
      >>> bot = Bot()
      >>> isinstance(fortune(bot, {'body': 'jabba: fortune'}), str)
      True
    """
    process = Popen("fortune", stdout=PIPE, shell=True)
    os.waitpid(process.pid, 0)
    return '\n' + process.communicate()[0].decode('utf-8').strip()

@cmd('urban')
def urban(bot, msg, arg):
    """
      >>> class Bot:
      ...     nick = 'jabba'
      >>> bot = Bot()
      >>> print(urban(bot, {'body': 'jabba: urban foo'}))
      An term used for unimportant variables in programming when the programmer is too lazy to think of an actual name.  The origin of such word is described in detail in RFC 3092.
      int foo; foo = 2 + 2; cout << foo;
    """
    url = 'http://www.urbandictionary.com/define.php?' + urlencode({'term': arg})
    document = pq(url=url)
    text = pq(document('.definition:first')).text()
    text_example = pq(document('.example:first')).text()
    if text:
        if text_example:
            text = '{}\n{}'.format(text, text_example)
        return text
