
from pyquery import PyQuery as pq
from urllib.error import URLError

from .parseurls import grab_urls

def extract_html_title(bot, msg):
    """
      >>> extract_html_title(
      ...     None,
      ...     {'body': 'Check this http://danielnouri.org out'},
      ...     )
      ["Daniel Nouri's Homepage · http://danielnouri.org"]
      >>> extract_html_title(None, {'body': 'Nothing to see here'})
      []
    """
    messages = []
    for url in grab_urls(msg['body']):
        try:
            document = pq(url=url)
        except URLError:
            continue
        messages.append("{} · {}".format(document('title').text(), url))
    return messages
