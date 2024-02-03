import click

from app.task import Task


@click.group()
def main():
    """App CLI built with Click"""
    pass


@click.command()
@click.option(
    "-n", "--name",
    required=True,
    type=click.STRING,
    help="Input the task name"
)
def info(name):
    """Show task info with given name"""    
    t = Task(name)
    print(t.info())


@click.command()
@click.option(
    "-n", "--name",
    required=True,
    type=click.STRING,
    help="Input the task name"
)
def run(name):
    """Run task with given name"""
    t = Task(name)
    t.run()


main.add_command(info)
main.add_command(run)


if __name__ == "__main__":
    main()
