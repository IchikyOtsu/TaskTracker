import click
from utils import task as ts


@click.group()
def cli():
    pass


@click.command()
@click.argument('task_name')
def add(task_name):
    click.echo(task_name + " has been successfully created !")
    new_Task = ts.Task(task_name)
    new_Task.add_new_task()


@click.command()
def list():
    ts.task_list()


cli.add_command(add)
cli.add_command(list)

if __name__ == "__main__":
    cli()
