import click

from safekey.app import SafeKey


@click.group()
def main():
    """Safekey CLI app built with Click"""
    pass


@click.command()
@click.option(
    "-a", "--appname",
    type=click.STRING,
    required=True,
    help="Application name",
)
@click.option(
    "-u", "--username",
    type=click.STRING,
    required=True,
    help="Username registered",
)
@click.option(
    "-p", "--password",
    type=click.STRING,
    required=True,
    help="Password registered",
)
def add(appname, username, password):
    """Add a new password"""    
    safekey = SafeKey()
    safekey.add_password(
        appname=appname,
        username=username,
        password=password
    )


@click.command()
@click.option(
    "-a", "--appname",
    type=click.STRING,
    required=True,
    help="Application name",
)
def get(appname):
    """Retrieve a password"""
    safekey = SafeKey()
    safekey.get_password(appname=appname)


@click.command()
def list():
    """List all passwords"""
    safekey = SafeKey()
    safekey.list_passwords()


@click.command()
@click.option(
    "-a", "--appname",
    type=click.STRING,
    required=True,
    help="Application name",
)
@click.option(
    "-p", "--new-password",
    type=click.STRING,
    required=True,
    help="New Password",
)
def update(appname, new_password):
    """Update a password"""
    safekey = SafeKey()
    safekey.update_password(
        appname=appname,
        new_password=new_password
    )


@click.command()
@click.option(
    "-a", "--appname",
    type=click.STRING,
    required=True,
    help="Application name",
)
def remove(appname):
    """Remove a password"""
    safekey = SafeKey()
    safekey.remove_password(appname=appname)


main.add_command(add)
main.add_command(get)
main.add_command(list)
main.add_command(update)
main.add_command(remove)


if __name__ == "__main__":
    main()
