import typer

from safekey.app import SafeKey

app = typer.Typer()
safekey = SafeKey()


@app.command()
def add(appname: str, username: str, password: str):
    """Add a new password entry."""
    safekey.add_password(appname, username, password)
    

@app.command()
def get(appname: str):
    """Get a password for an app."""
    safekey.get_password(appname)


@app.command()
def list():
    """List all passwords."""
    safekey.list_passwords()


@app.command()
def update(appname: str, new_password: str):
    """Update a password for an app."""
    safekey.update_password(appname, new_password)


@app.command()
def remove(appname: str):
    """Remove a password for an app."""
    safekey.remove_password(appname)



if __name__ == "__main__":
    app()
