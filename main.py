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


@click.command()
@click.argument('Task_ID')
def mark_done(task_id):
    try:
        task_is_int = int(task_id)
    except:
        print("Id have to be an integer, you fool...")
        return
    ts.ts_mark_done(task_id)
    print(f"The Task number {task_id} has changed is status for done")

@click.command()
@click.argument('Task_ID')
def mark_in_progress(task_id):
    try:
        task_is_int = int(task_id)
    except:
        print("Id have to be an integer, you fool...")
        return
    ts.ts_mark_in_progress(task_id)
    print(f"The Task number {task_id} has changed is status for in-progress")

@click.command()
@click.argument('Task_ID')
def mark_to_do(task_id):
    try:
        task_is_int = int(task_id)
    except:
        print("Id have to be an integer, you fool...")
        return
    ts.ts_mark_to_do(task_id)
    print(f"The Task number {task_id} has changed is status for to do")


@click.command()
@click.argument('Task_ID')
def delete(task_id):
    try:
        task_is_int = int(task_id)
    except:
        print("Id have to be an integer")
        return
    ts.delete_from_ts(task_id)
    print(f"Task Number {task_id} has been removed")


@click.command()
@click.argument('Task_ID')
@click.argument('description')
def description(task_id, description):
    try:
        task_is_int = int(task_id)
    except:
        print("Id have to be an integer")
        return
    ts.ts_description_change(task_id,description)
    print(f"Description has been successfully modified !")


cli.add_command(delete)
cli.add_command(add)
cli.add_command(list)
cli.add_command(mark_done)
cli.add_command(mark_in_progress)
cli.add_command(mark_to_do)
cli.add_command(description)

if __name__ == "__main__":
    cli()
