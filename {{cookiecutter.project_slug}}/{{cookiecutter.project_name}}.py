import click

@click.group()
def {{cookiecutter.command_name}}():
    pass

@{{cookiecutter.command_name}}.command()
def cmd1():
    '''Command on {{cookiecutter.command_name}}'''
    click.echo('{{cookiecutter.command_name}} cmd1')

@{{cookiecutter.command_name}}.command()
def cmd2():
    '''Command on {{cookiecutter.command_name}}'''
    click.echo('{{cookiecutter.command_name}} cmd2')

if __name__ == '__main__':
    {{cookiecutter.command_name}}()
