from cliff.command import Command
from safekey.app import SafeKey


class List(Command):
    "List all saved passwords"

    def take_action(self, parsed_args):
        manager = SafeKey()
        entries = manager.list_passwords()
        for entry in entries:
            self.app.stdout.write(f"Appname: {entry['appname']}, Username: {entry['username']}\n")
