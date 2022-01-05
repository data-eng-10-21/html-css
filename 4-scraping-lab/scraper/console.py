from src.adapters.indeed_client import get_job_cards

cards = get_job_cards(position = 'data engineer', location = 'United States', start = 0)
first_card = cards[0]