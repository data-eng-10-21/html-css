import click
from adapters.indeed_client import get_job_cards, get_card_from
import pdb

@click.group()
def scraper():
    pass

# Command Group
@click.group(name='tools')
def cli_tools():
    """Tool related commands"""
    pass

@cli_tools.command(name='scrape_jobs', help='help scrape_jobs')
def scrape_jobs(start = 0, position = 'data engineer'):
    cards = get_job_cards(position = 'data engineer', location = 'United States', start = 0)
    print(cards)


@cli_tools.command(name='get_card', help='help scrape_jobs')
@click.option('--id', default='0601c9a2ee3bd7d2', help='test option')
def get_card(id):
    card = get_card_from(id)
    print(card)

if __name__ == '__main__':
    cli_tools()