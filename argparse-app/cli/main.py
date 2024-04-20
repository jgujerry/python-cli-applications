import argparse

from safekey import SafeKey


def main():
    safekey = SafeKey()
    
    parser = argparse.ArgumentParser(description="SafeKey CLI Tool")
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')

    # Add sub-command
    add_parser = subparsers.add_parser('add', help='Add a new credential')
    add_parser.add_argument('--appname', type=str, help='Application name')
    add_parser.add_argument('--username', type=str, help='Username registered')
    add_parser.add_argument('--password', type=str, help='Password registered')
    add_parser.set_defaults(func=safekey.add_password)

    # Get sub-command
    get_parser = subparsers.add_parser('get', help='Retrieve a password')
    get_parser.add_argument('--appname', type=str, help='App name or Username')
    get_parser.set_defaults(func=safekey.get_password)

    # Update sub-command
    update_parser = subparsers.add_parser('update', help='Update a password')
    update_parser.add_argument('--appname', type=str, help='App name or Username')
    update_parser.add_argument('--new-password', type=str, help='New Password')
    update_parser.set_defaults(func=safekey.update_password)

    # Remove sub-command
    remove_parser = subparsers.add_parser('remove', help='Remove a password')
    remove_parser.add_argument('--appname', type=str, help='App name or Username')
    remove_parser.set_defaults(func=safekey.remove_password)

    # List sub-command
    list_parser = subparsers.add_parser('list', help='List all passwords')
    list_parser.set_defaults(func=safekey.list_passwords)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
