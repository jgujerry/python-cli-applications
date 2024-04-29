import fire

from safekey.app import SafeKey


class CLI:
    def __init__(self):
        self.manager = SafeKey()

    def add(self, appname, username, password):
        """Add a new password entry."""
        self.manager.add_password(appname, username, password)

    def get(self, appname):
        """Get the password for an app."""
        self.manager.get_password(appname)

    def update(self, appname, new_password):
        """Update the password for an app."""
        self.manager.update_password(appname, new_password)
    
    def delete(self, appname):
        """Delete the password for an app."""
        self.manager.remove_password(appname)

    def list(self):
        """List all password entries."""
        self.manager.list_passwords()


def main():
    cli = CLI()
    fire.Fire({
        "add": cli.add,
        "get": cli.get,
        "update": cli.update,
        "delete": cli.delete,
        "list": cli.list,
    })



if __name__ == "__main__":
    main()
