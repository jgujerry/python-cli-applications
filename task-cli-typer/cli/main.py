import typer


def main(a: str, b: int):
    typer.echo("Welcome to Typer")
    

if __name__ == "__main__":
    typer.run(main)
