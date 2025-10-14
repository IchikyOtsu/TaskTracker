import click

# Fonction de test


def printfonct():
    print("Hello World")


@click.group()
def cli():
    pass


@click.command()
@click.argument('task_name')
def add(task_name):
    click.echo(task_name)
    printfonct()


cli.add_command(add)


if __name__ == "__main__":
    cli()
