from indeed_client import *
from indeed_adapter import *

cards = get_job_cards(index, position = 'data engineer', location = 'United States', start = 0)
first_card = cards[0]