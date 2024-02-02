import click

from .info import info


@click.group()
def main():
    """App CLI built with Click"""
    pass


main.add_command(info)


if __name__ == "__main__":
    main()
