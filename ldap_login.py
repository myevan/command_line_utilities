#!/usr/bin/env python
import sys
import argparse
import getpass

try:
    import ldap
except ImportError:
    print "sudo pip install python-ldap"
    sys.exit(-1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--hostname', type=str, help='host name')
    parser.add_argument('-P', '--password', action='store_true', help='password')
    parser.add_argument('-B', '--bind-dn', metavar='"uid=U,cn=C,dc=D"', type=str, help='bind domain name')

    args = parser.parse_args()
    if not args.hostname:
        print 'NO_HOSTNAME'
        parser.print_help()
        return -2

    conn = ldap.initialize('ldap://' + args.hostname)

    if not args.bind_dn:
        print 'NO_BIND_DN'
        parser.print_help()
        return -3

    password = getpass.getpass() if args.password else ''

    print conn.bind_s(args.bind_dn, password)
    return 0

if __name__ == '__main__':
    sys.exit(main())
