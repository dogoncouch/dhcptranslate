#!/usr/bin/env python3

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

from argparse import ArgumentParser
from ipaddress import IPv4Address

import dhcptranslate.utils
from dhcptranslate import __version__


class DHCPTranslateCore:

    def __init__(self):
        """Initialize the DHCP translate CLI program"""

        self.args = None
        self.arg_parser = ArgumentParser()


    def get_args(self):
        """Set argument options"""

        self.arg_parser.add_argument('--version', action = 'version',
                version = '%(prog)s ' + str(__version__))
        self.arg_parser.add_argument('files',
                action = 'store', metavar = 'FILE', nargs = '+',
                help = 'set a dhcp conf file to parse')
        self.arg_parser.add_argument('-c', '--config',
                action = 'store_true',
                help = 'Output in config format with IP address')

        self.args = self.arg_parser.parse_args()


    def main_event(self):
        """Read input files and output CSV"""
        conflines = []
        for inputfile in self.args.files:
            try:
                with open(inputfile, 'r') as f:
                    lines = [r.rstrip() for r in f.readlines()]
            except FileNotFoundError:
                print('Error: file', inputfile, 'not found.')
                exit(1)
            for line in lines:
                conflines.append(line)

        if self.args.config:
            newconflines = []
            for line in conflines:
                newconfline = dhcptranslate.utils.translatetoconfig(line)
                if newconfline:
                    newconflines.append(newconfline)
            for line in newconflines:
                print(line)

        else:
            csvlines = []
            for line in conflines:
                csvline = dhcptranslate.utils.translateline(line)
                if csvline:
                    csvlines.append(csvline)

            csvlinessorted = sorted(csvlines, key=lambda x: IPv4Address(x[0]))

            print('ip_address,MAC_address,MAC_vendor,hostname,' + \
                    'reservation,original_config_line')
            for line in csvlinessorted:
                print(','.join(line))


    def run_script(self):
        """Run the dhcptranslate program"""
        try:
            self.get_args()
            self.main_event()

        except KeyboardInterrupt:
            print('\nExiting on KeyboardInterrupt')


def main():
    translator = DHCPTranslateCore()
    translator.run_script()


if __name__ == "__main__":
    main()
