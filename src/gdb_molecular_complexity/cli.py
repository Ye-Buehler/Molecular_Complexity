"""Console script for gdb_molecular_complexity."""
import gdb_molecular_complexity

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for gdb_molecular_complexity."""
    console.print("Replace this message by putting your code into "
               "gdb_molecular_complexity.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
