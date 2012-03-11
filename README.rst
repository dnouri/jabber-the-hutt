==============
jabber-the-hut
==============

An experimental bot for Jabber chat rooms.

Install
=======

``jaber-the-hut`` requires Python 3.x, and recent versions of libxml2
and libxslt.

To install ``jabber-the-hut`` inside a ``virtualenv``::

  virtualenv -p python3 jabber-the-hut
  cd jabber-the-hut
  bin/pip install jabber-the-hut

Or from the source::

  git clone https://github.com/dnouri/jabber-the-hut
  cd jabber-the-hut
  virtualenv -p python3 .
  bin/python setup.py develop

Run
===

Installation creates a ``jabber-the-hut`` console script.  This script
expects a configuration file as its first argument::

  $ jabber-the-hut thehut.ini

Your configuration file should look something like this::

  [jabber-the-hut]
  jid = jabba@jabber.org
  room = sleek@conference.jabber.org
  room_password = some room password
