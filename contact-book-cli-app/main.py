import typer
from rich.console import Console
from rich.table import Table
from contact_book.model import Contact
from contact_book.database import create, read, update, delete

app = typer.Typer()
console = Console()


@app.command(short_help='adds a contact')
def add(name: str, contact_number: str):
    typer.echo(f"Adding {name}, {contact_number}")
    contact = Contact(name, contact_number)
    create(contact)
    show()


@app.command(short_help='shows all contacts')
def show():
    contacts = read()

    console.print("[bold magenta]Contact Book[/bold magenta]", "📕")

    if len(contacts) == 0:
        console.print("[bold red]No contacts to show[/bold red]")
    else:
        table = Table(show_header=True,
                      header_style="bold blue", show_lines=True)
        table.add_column("#", style="dim", width=3, justify="center")
        table.add_column("Name", min_width=20, justify="center")
        table.add_column("Contact Number", min_width=12, justify="center")

        for idx, contact in enumerate(contacts, start=1):
            table.add_row(str(
                idx), f'[cyan]{contact.name}[/cyan]', f'[green]{contact.contact_number}[/green]')
        console.print(table)


@app.command(short_help='edits a contact')
def edit(position: int, name: str = None, contact_number: str = None):
    typer.echo(f"Editing {position}")
    update(position, name, contact_number)
    show()


@app.command(short_help='removes a contact')
def remove(position: int):
    typer.echo(f"Removing {position}")
    delete(position)
    show()


if __name__ == "__main__":
    app()
