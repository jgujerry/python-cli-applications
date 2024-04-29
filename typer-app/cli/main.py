import typer

from safekey.app import SafeKey

app = typer.Typer()
safekey = SafeKey()


@app.command()
def add(
    appname: str = typer.Option(None, "-a", "--appname", help="The name of the app."),
    username: str = typer.Option(None, "-u", "--username", help="The username for the app."),
    password: str = typer.Option(None, "-p", "--password", help="The password for the app."),
):
    """Add a new password entry."""
    safekey.add_password(appname, username, password)
    

@app.command()
def get(appname: str = typer.Option(None, "-a", "--appname", help="The name of the app.")):
    """Get a password for an app."""
    safekey.get_password(appname)


@app.command()
def list():
    """List all passwords."""
    safekey.list_passwords()


@app.command()
def update(
    appname: str = typer.Option(None, "-a", "--appname", help="The name of the app."),
    new_password: str = typer.Option(None, "-p", "--password", help="The new password for the app."),
):
    """Update a password for an app."""
    safekey.update_password(appname, new_password)


@app.command()
def remove(appname: str = typer.Option(None, "-a", "--appname", help="The name of the app.")):
    """Remove a password for an app."""
    safekey.remove_password(appname)



if __name__ == "__main__":
    app()
