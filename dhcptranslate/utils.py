#!/usr/bin/env python3

import re
from socket import gethostbyname

confformat = re.compile(r'^host (\S+) \{fixed-address (\S+); hardware ethernet (\S+); \}')
ipformat = re.compile(r'[0-0]{1,3}\.[0-0]{1,3}\.[0-0]{1,3}\.[0-0]{1,3}')

def translateline(confline):
    if confline.startswith('host'):
        try:
            if confformat.match(confline):
                hostname, reservation, mac = confformat.findall(confline)[0]
            else:
                return()
        except ValueError:
            hostname, reservation, mac = 'LINEERROR', 'LINEERROR', 'LINEERROR'
        except IndexError:
            hostname, reservation, mac = 'LINEERROR', 'LINEERROR', 'LINEERROR'
        if ipformat.match(reservation):
            ipaddress = reservation
        else:
            try:
                ipaddress = gethostbyname(reservation)
            except Exception:
                ipaddress = '0.0.0.0'
        return([ipaddress, mac, hostname, reservation, confline])
        #return(','.join([ipaddress, mac, hostname, reservation, confline]))

