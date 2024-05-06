# Import the necessary modules
from cement import App, Controller, ex
from safekey.app import SafeKey


class BaseController(Controller):
    class Meta:
        label = 'base'
        description = "A simple password management CLI application."
        epilog = "Usage: skcli command --appname NAME [--username USERNAME] [--password PASSWORD]"

    @ex(help='add a new password', 
        arguments=[
            (['--appname'], {'help': 'the application name', 'required': True}),
            (['--username'], {'help': 'username for the application', 'required': True}),
            (['--password'], {'help': 'password for the application', 'required': True}),
        ])
    def add(self):
        manager = SafeKey()
        manager.add_password(self.app.pargs.appname, self.app.pargs.username, self.app.pargs.password)

    @ex(help='get a password', 
        arguments=[
            (['--appname'], {'help': 'the application name', 'required': True}),
        ])
    def get(self):
        manager = SafeKey()
        manager.get_password(self.app.pargs.appname)

    @ex(help='list all passwords', 
        arguments=[])
    def list(self):
        manager = SafeKey()
        manager.list_passwords()

    @ex(help='update an existing password',
        arguments=[
            (['--appname'], {'help': 'the application name', 'required': True}),
            (['--password'], {'help': 'new password for the application', 'required': True}),
        ])
    def update(self):
        manager = SafeKey()
        manager.update_password(self.app.pargs.appname, self.app.pargs.password)

    @ex(help='remove a stored password',
        arguments=[
            (['--appname'], {'help': 'the application name', 'required': True}),
        ])
    def remove(self):
        manager = SafeKey()
        manager.remove_password(self.app.pargs.appname)


class SKCLI(App):
    class Meta:
        label = 'skcli'
        base_controller = 'base'
        handlers = [BaseController]



def main():
    with SKCLI() as app:
        app.run()


if __name__ == '__main__':
    main()
