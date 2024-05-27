import click

@click.group()
@click.pass_context
def cli(ctx):
    """A simple to-do list CLI."""
    ctx.ensure_object(dict)  # Initialize an empty dictionary for tasks

@cli.command()
@click.pass_context
@click.argument('task')
def add(ctx, task):
    """Add a task to the list."""
    task_list = ctx.obj
    if task not in task_list:
        task_list[task] = 'Pending'
        click.echo(f'Added task: {task}')
    else:
        click.echo(f'Task "{task}" already exists!')

@cli.command()
@click.pass_context
def list_tasks(ctx):
    """List all tasks."""
    task_list = ctx.obj
    if task_list:
        click.echo("Your To-Do List:")
        for task, status in task_list.items():
            click.echo(f'- {task} ({status})')
    else:
        click.echo("Your to-do list is empty!")

if __name__ == '__main__':
    cli()