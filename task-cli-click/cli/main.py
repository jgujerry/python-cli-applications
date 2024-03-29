import sys
import click

from app.task import Task


@click.group()
def main():
    """Task CLI built with Click"""
    pass

#----------------------------------------------------------------
# Command with argument
#----------------------------------------------------------------
@click.command()
@click.argument("name", type=click.STRING,)
def show(name):
    """Show task info with given name"""    
    t = Task(name)
    print(t.show())


#----------------------------------------------------------------
# Command with argument, options
#----------------------------------------------------------------
def parse_parameters(ctx, param, value):
    """Parase parameters from click options"""
    params = {}
    for item in value:
        if "=" not in item:
            print("Parameter should be in format: key=value")
            sys.exit(1)
        key, value = item.split("=")[0], "=".join(item.split("=")[1:])
        if not key or not value:
            print("Parameter should be in format: key=value")
            sys.exit(1)
        params[key] = value
    return params


@click.command()
@click.argument("name", type=click.STRING)
@click.option(
    "-p", "--param",
    required=False,
    multiple=True,
    type=click.STRING,
    callback=parse_parameters,
    help="Input the parameters",
)
def run(name, param):
    """Run task with given name"""
    t = Task(name)
    t.run(params=param)


#----------------------------------------------------------------
# Sub-command
#----------------------------------------------------------------
@click.group()
def scheduler():
    """Task sub-command"""
    pass


@scheduler.command()
def start():
    """Start task scheduler"""
    print("Starting task scheduler...")
    print("Started!")


@scheduler.command()
def stop():
    """Stop task scheduler"""
    print("Stopping task scheduler...")
    print("Stopped!")


main.add_command(show)
main.add_command(run)
main.add_command(scheduler)


if __name__ == "__main__":
    main()
