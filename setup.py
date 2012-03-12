import os

from setuptools import setup, find_packages

version = '0.0dev'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires = [
    'pyquery',
    'pytest',
    'sleekxmpp',
    'zope.dottedname',
    ]

setup(name='jabber-the-hutt',
      version=version,
      description="An experimental bot for Jabber chat rooms.",
      long_description='\n\n'.join([README, CHANGES]),
      classifiers=[
          'Programming Language :: Python :: 3.2',
          'Development Status :: 3 - Alpha',
        ],
      keywords='xmpp jabber bot chat',
      author='Daniel Nouri',
      author_email='daniel.nouri@gmail.com',
      url='https://github.com/dnouri/jabber-the-hutt',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      [console_scripts]
      jabber-the-hutt = jabberthehutt.script:main
      # -*- Entry points: -*-
      """,
      )
