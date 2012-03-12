===============
jabber-the-hutt
===============

An experimental bot for Jabber chat rooms.

  *Jabba Desilijic Tiure, or simply Jabba the Hutt. Jabba is of the
  Hutt race and like most of his species, a gangster. Hutts are a
  large slug-like race with thick leathery skin, human-like arms,
  large black cat-like eyes, and a wide mouth. A Hutt may weigh in
  excess of several tons. The species are hermaphrodites and reproduce
  by fission. They speak Huttese, a language reminiscent of Quechua.*
  -- Urban Dictionary

Install
=======

``jaber-the-hutt`` requires Python 3.x, and recent versions of libxml2
and libxslt, along with development headers.

To satisfy these dependenices on a Debian system, do::

  sudo apt-get install python3 python3-dev libxml2-dev libxslt-dev

To then install ``jabber-the-hutt`` itself inside a ``virtualenv``::

  wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
  mkdir jabber-the-hutt
  cd jabber-the-hutt
  python3 virtualenv.py .
  bin/pip install jabber-the-hutt

Alternatively, you can install ``jabber-the-hutt`` from the source::

  git clone https://github.com/dnouri/jabber-the-hutt
  cd jabber-the-hutt
  wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
  python3 virtualenv.py .
  bin/python setup.py develop

Run
===

Installation creates a ``jabber-the-hutt`` console script.  This script
expects a configuration file as its first argument::

  $ bin/jabber-the-hutt hutt.ini

Your configuration file should look something like this::

  [jabber-the-hutt]
  jid = jabba@jabber.org
  room = sleek@conference.jabber.org
  room_password = some room password
