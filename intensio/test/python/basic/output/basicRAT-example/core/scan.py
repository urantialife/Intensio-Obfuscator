# -*- coding: utf-8 -*-
import socket
YKuxwVKgqXGNPfPNuAHZICrvXJdDRSyt = [ 
            21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
            514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888
]
def rIWDlLvwQJNduZJsdPwSVIUMRBxTNank(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm = ''
    for NnqjoWetzCvXekeAiwWSCpSCIZiaANtz in YKuxwVKgqXGNPfPNuAHZICrvXJdDRSyt:
        GmwXZdrnoUbldKqssCIqWIqANfnQaEIj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tFmqaOJMsYAtFtqZghppUOPEaXLcWWPb = GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.connect_ex((ip, NnqjoWetzCvXekeAiwWSCpSCIZiaANtz))
        socket.setdefaulttimeout(0.5)
        nHfRLderMovGbMAjwfSsfyGYQhkTjVOH = 'open' if not tFmqaOJMsYAtFtqZghppUOPEaXLcWWPb else 'closed'
        gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm += '{:>5}/tcp {:>7}\n'.format(NnqjoWetzCvXekeAiwWSCpSCIZiaANtz, nHfRLderMovGbMAjwfSsfyGYQhkTjVOH)
    return gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm.rstrip()
