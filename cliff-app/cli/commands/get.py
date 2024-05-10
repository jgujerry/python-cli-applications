from cliff.command import Command
from safekey.app import SafeKey


class Get(Command):
    "Get a password"

    def get_parser(self, prog_name):
        parser = super(Get, self).get_parser(prog_name)
        parser.add_argument('--appname')
        return parser

    def take_action(self, parsed_args):
        manager = SafeKey()
        password = manager.get_password(parsed_args.appname)
        self.app.stdout.write(f'Password for {parsed_args.appname}: {password}\n')
