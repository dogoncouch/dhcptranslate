# dhcptranslate

## Usage
Parses DHCP reservations from an ISC DHCP config file, and translates any reservations made by DNS name to an IP address. Outputs CSV format to the command line in the following format, sorted by `ip_address`:
```
ip_address,MAC_address,"MAC_vendor",hostname,reservation,original_config_line
```
The `reservation` field contains what was originally defined by the reservation, whether it is by IP address or DNS name. The `ip_address` field will show `0.0.0.0` if DNS resolution failed. `MAC_vendor` is in quotes, since it sometimes contains commas. The last field is the original config line in its entirety.

### Options
```
usage: dhcptranslate [-h] [--version] FILE [FILE ...]

positional arguments:
  FILE        set a dhcp conf file to parse

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  -c, --config  Output in config format with IP address
```

## Examples
    
    dhcptranslate dhcpd.conf includes.conf > csvoutputfile

## Support
Bugs, questions, and other issues can be directed to the project's [issues page](https://github.com/dogoncouch/dhcptranslate/issues) on GitHub, or emailed to [dogoncouch@dogoncouch.net](mailto:dogoncouch@dogoncouch.net).


# Copyright
MIT License

Copyright (c) 2020 Dan Persons (dogoncouch@dogoncouch.net)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
