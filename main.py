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
@click.option('--status', default="all", help='todo / done / in-progress')
def list(status="all"):
    if status not in ["all", "todo", "done", "in-progress"]:
        print("Sorry you have to type exactly todo or done or in-progress")
    else:
        ts.task_list(status)


cli.add_command(add)
cli.add_command(list)

if __name__ == "__main__":
    cli()
