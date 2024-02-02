import click

from app.task import Task


@click.command()
@click.option(
    "-n", "--name",
    required=True,
    type=click.STRING,
    help="Input a name"
)
def info(name):
    """Show task info with given name"""    
    t = Task(name)
    print(t.info())
