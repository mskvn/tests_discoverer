import os

import click


@click.command()
def cli():
    click.echo(f'Current directory is: {os.getcwd()}')
    files = "\n".join(os.listdir(os.getcwd()))
    click.echo(f'Files list:\n {files}')
