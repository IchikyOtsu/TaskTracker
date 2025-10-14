import click
from utils import task as ts


@click.group()
def cli():
    pass


@click.command()
@click.argument('task_name')
def add(task_name):
    click.echo(task_name + " has been successfully created !")
    new_Task = ts.Task()
    print(new_Task)


cli.add_command(add)


if __name__ == "__main__":
    cli()
