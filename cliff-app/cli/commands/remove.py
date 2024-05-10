from cliff.command import Command
from safekey.app import SafeKey


class Remove(Command):
    "Remove a password entry"

    def get_parser(self, prog_name):
        parser = super(Remove, self).get_parser(prog_name)
        parser.add_argument('--appname')
        return parser

    def take_action(self, parsed_args):
        manager = SafeKey()
        manager.remove_password(parsed_args.appname)
        self.app.stdout.write(f'Password removed for {parsed_args.appname}\n')
