# MIT License
# 
# Copyright (c) 2020 Dan Persons (dogoncouch@dogoncouch.net)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
dhcptranslate
----------

dhcptranslate parses DHCP reservations from an ISC DHCP config file, and translates any reservations made by DNS name to an IP address. Outputs CSV format to the command line in the following format, sorted by ip_address:

ip_address,MAC_address,"MAC_vendor",hostname,reservation,original_config_line

The reservation field contains what was originally defined by the reservation, whether it is by IP address or DNS name. The ip_address field will show 0.0.0.0 if DNS resolution failed. MAC_vendor is in quotes, since it sometimes contains commas. The last field is the original config line in its entirety.


Options
```````

::

    usage: dhcptranslate [-h] [--version] FILE [FILE ...]
    
    positional arguments:
      FILE        set a dhcp conf file to parse
    
    optional arguments:
      -h, --help  show this help message and exit
      --version   show program's version number and exit
      -c, --config  Output in config format with IP address


"""

from setuptools import setup
from os.path import join
from sys import prefix
from dhcptranslate import __version__

ourdata = [(join(prefix, 'share/doc/dhcptranslate'), ['README.md',
            'LICENSE', 'CHANGELOG.md'])]

setup(name = 'dhcptranslate', version = str(__version__),
        description = 'Basic CLI network automation tool',
        long_description = __doc__,
        author = 'Dan Persons', author_email = 'dogoncouch@dogoncouch.net',
        url = 'https://github.com/dogoncouch/dhcptranslate',
        download_url = 'https://github.com/dogoncouch/dhcptranslate/archive/v' + str(__version__) + '.tar.gz',
        keywords = ['networking'],
        packages = ['dhcptranslate'],
        entry_points = \
                { 'console_scripts': [ 'dhcptranslate = ' + \
                'dhcptranslate.core:main' ]},
        data_files = ourdata,
        classifiers = ["Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: POSIX",
            "Programming Language :: Python",
            "Topic :: System :: Systems Administration"])
