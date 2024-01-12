import click

from rich.console import Console
from rich.table import Table

from stock import ticker as tk


@click.command()
@click.option(
    "-t", "--ticker",
    required=True,
    type=click.STRING,
    help="Input a stock ticker symbol"
)
def info(ticker):
    """Show stock information for a given ticker"""    
    data = tk.get_stock_info(ticker)

    table = Table(title=f"Stock Information: {ticker}")
    for k, v in data.items():
        table.add_row(k, str(v))
    
    console = Console()
    console.print(table)
