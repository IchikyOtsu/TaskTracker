import click
from utils import task as ts


@click.group()
def cli():
    """
    Command Line Interface for the Task Tracker application.
    This CLI allows users to manage tasks, including adding, listing, marking, and deleting tasks.
    """
    pass


@click.command()
@click.argument('task_name')
def add(task_name):
    """
    Add a new task to the task list.

    :param task_name: The name of the task to be added.
    """
    click.echo(task_name + " has been successfully created !")
    new_Task = ts.Task(task_name)
    new_Task.add_new_task()


@click.command()
@click.option('--status', default="all", help='todo / done / in-progress')
def list(status="all"):
    """
    List tasks based on their status.

    :param status: The status of tasks to list (todo, done, in-progress, or all).
    """
    if status not in ["all", "todo", "done", "in-progress"]:
        print("Sorry you have to type exactly todo or done or in-progress")
    else:
        ts.task_list(status)


@click.command()
@click.argument('Task_ID')
def mark_done(task_id):
    """
    Mark a task as done.

    :param task_id: The ID of the task to mark as done.
    """
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
    """
    Mark a task as in progress.

    :param task_id: The ID of the task to mark as in progress.
    """
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
    """
    Mark a task as to do.

    :param task_id: The ID of the task to mark as to do.
    """
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
    """
    Delete a task from the task list.

    :param task_id: The ID of the task to delete.
    """
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
    """
    Change the description of a task.

    :param task_id: The ID of the task to modify.
    :param description: The new description for the task.
    """
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
