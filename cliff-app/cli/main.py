import sys
from cliff.app import App
from cliff.commandmanager import CommandManager


class SKCLI(App):
    def __init__(self):
        super(SKCLI, self).__init__(
            description='SKCLI Password Manager',
            version='1.0.0',
            command_manager=CommandManager('skcli.commands'),
            deferred_help=True,
        )


def main(argv=sys.argv[1:]):
    app = SKCLI()
    return app.run(argv)


if __name__ == '__main__':
    sys.exit(main())
