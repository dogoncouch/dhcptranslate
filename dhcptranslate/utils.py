#!/usr/bin/env python3

import re
from socket import gethostbyname
from mac_vendor_lookup import MacLookup

confformat = re.compile(r'^host (\S+) \{fixed-address (\S+); hardware ethernet (\S+); \}')
ipformat = re.compile(r'[0-0]{1,3}\.[0-0]{1,3}\.[0-0]{1,3}\.[0-0]{1,3}')

def translateline(confline):
    """Parse an ISC DHCP reservation, and return CSV format with:
    ip_address,MAC_address,MAC_vendor,hostname,reservation,original_line"""

    if confline.startswith('host'):
        try:
            if confformat.match(confline):
                hostname, reservation, mac = confformat.findall(confline)[0]
                mac_vendor = '"' + MacLookup().lookup(mac) + '"'
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
        return([ipaddress, mac, mac_vendor, hostname, reservation, confline])
        #return(','.join([ipaddress, mac, hostname, reservation, confline]))

