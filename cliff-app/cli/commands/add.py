from cliff.command import Command
from safekey.app import SafeKey


class Add(Command):
    "Add a new password"

    def get_parser(self, prog_name):
        parser = super(Add, self).get_parser(prog_name)
        parser.add_argument('--appname', required=True)
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)
        return parser

    def take_action(self, parsed_args):
        manager = SafeKey()
        manager.add_password(parsed_args.appname, parsed_args.username, parsed_args.password)
        self.app.stdout.write(f'Password added for {parsed_args.appname}\n')
