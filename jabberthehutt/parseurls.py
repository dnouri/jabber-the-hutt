# http://mail.python.org/pipermail/tutor/2002-September/017228.html

import re

def grab_urls(text):
    r"""
      >>> grab_urls('''hello world, this is an url:
      ...           http://python.org.  Can you find it?''')
      ['http://python.org']
    """
    return url_re.findall(text)

urls = '(?: %s)' % '|'.join("""http https telnet gopher file wais
ftp""".split())
ltrs = r'\w'
gunk = r'/#~:.?+=&%@!\-'
punc = r'.:?\-'
any = "%(ltrs)s%(gunk)s%(punc)s" % { 'ltrs' : ltrs,
                                     'gunk' : gunk,
                                     'punc' : punc }

url = r"""
    \b                            # start at word boundary
        %(urls)s    :             # need resource and a colon
        [%(any)s]  +?             # followed by one or more
                                  #  of any valid character, but
                                  #  be conservative and take only
                                  #  what you need to....
    (?=                           # look-ahead non-consumptive assertion
            [%(punc)s]*           # either 0 or more punctuation
            (?:   [^%(any)s]      #  followed by a non-url char
                |                 #   or end of the string
                  $
            )
    )
    """ % {'urls' : urls,
           'any' : any,
           'punc' : punc }

url_re = re.compile(url, re.VERBOSE | re.MULTILINE)

def test():
    assert 0
    sample = """hello world, this is an url:
                http://python.org.  Can you find it?"""
    match = url_re.search(sample)
    assert match.group(0) == 'http://python.org'
