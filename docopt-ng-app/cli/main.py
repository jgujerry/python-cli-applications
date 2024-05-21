import sys
from docopt import docopt
from safekey.app import SafeKey


def main():
    arguments = docopt(__doc__, version='SafeKey 1.0')

    sk = SafeKey()

    if arguments['add']:
        sk.add_password(arguments['<appname>'], arguments['<username>'], arguments['<password>'])
    elif arguments['get']:
        sk.get_password(arguments['<appname>'])
    elif arguments['list']:
        sk.list_passwords()
    elif arguments['update']:
        sk.update_password(arguments['<appname>'], arguments['<new_password>'])
    elif arguments['remove']:
        sk.remove_password(arguments['<appname>'])


if __name__ == '__main__':
    main()
