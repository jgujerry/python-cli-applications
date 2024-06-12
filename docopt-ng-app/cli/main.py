"""
skcli - A simple CLI password manager.

Usage:
  skcli add <appname> <username> <password>
  skcli get <appname>
  skcli list
  skcli update <appname> <new_password>
  skcli remove <appname>
  skcli (-h | --help)
  skcli (-v | --version)

Options:
  -h --help     Show this screen.
  -v --version  Show the version.
Commands:
  add       Add a new password entry.
  get       Retrieve a password entry.
  list      List all password entries.
  update    Update an existing password entry.
  remove    Remove a password entry.
"""

import sys
from docopt import docopt
from safekey.app import SafeKey

def main():
    args = docopt(__doc__, version="v0.0.1")
    sk = SafeKey()

    if args['add']:
        sk.add_password(args['<appname>'], args['<username>'], args['<password>'])
    elif args['get']:
        sk.get_password(args['<appname>'])
    elif args['list']:
        sk.list_passwords()
    elif args['update']:
        sk.update_password(args['<appname>'], args['<new_password>'])
    elif args['remove']:
        sk.remove_password(args['<appname>'])


if __name__ == '__main__':
    main()
