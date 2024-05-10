from cliff.command import Command
from safekey.app import SafeKey


class Update(Command):
    "Update an existing password"

    def get_parser(self, prog_name):
        parser = super(Update, self).get_parser(prog_name)
        parser.add_argument('--appname')
        parser.add_argument('--new-password')
        return parser

    def take_action(self, parsed_args):
        manager = SafeKey()
        manager.update_password(parsed_args.appname, parsed_args.new_password)
        self.app.stdout.write(f'Password updated for {parsed_args.appname}\n')
