import click
from .quoter import get_quote

@click.command()
@click.argument("n", default=1)
def quote(n):
    quotes = get_quote(n)
    for q in quotes:
        click.secho(f"{q['quote']}")
        click.secho(f"> {q['author']}")
        click.echo("---"*5)

if __name__ == '__main__':
    quote(1)