==============
jabber-the-hut
==============

An experimental bot for Jabber chat rooms.

Install
=======

``jaber-the-hut`` requires Python 3.x, and recent versions of libxml2
and libxslt.

To satisfy these dependenices on a Debian system, do::

  sudo apt-get install python3 libxml2-dev libxslt-dev

To then install ``jabber-the-hut`` itself inside a ``virtualenv``::

  wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
  mkdir jabber-the-hut
  cd jabber-the-hut
  python3 virtualenv.py .
  bin/pip install jabber-the-hut

Alternatively, you can install ``jabber-the-hut`` from the source::

  git clone https://github.com/dnouri/jabber-the-hut
  cd jabber-the-hut
  wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
  python3 virtualenv.py .
  bin/python setup.py develop

Run
===

Installation creates a ``jabber-the-hut`` console script.  This script
expects a configuration file as its first argument::

  $ bin/jabber-the-hut thehut.ini

Your configuration file should look something like this::

  [jabber-the-hut]
  jid = jabba@jabber.org
  room = sleek@conference.jabber.org
  room_password = some room password
