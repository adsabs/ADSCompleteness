import click

try:
    import lvtn_utils as utils

    config = utils.load_config()
    logger = utils.setup_logging("ADSCompleteness.cli")
except ImportError:
    import logging

    config = {}
    logger = logging.getLogger("ADSCompleteness.cli")


@click.group()
def cli():
    pass


@cli.command()
def hello():
    """Will greet"""
    print("Hello World!")


if __name__ == "__main__":
    cli()
