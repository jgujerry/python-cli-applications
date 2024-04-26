import typer

from safekey.app import SafeKey

app = typer.Typer()
safekey = SafeKey()


@app.command()
def add(appname: str, username: str, password: str):
    safekey.add_password(appname, username, password)
    



if __name__ == "__main__":
    app()
