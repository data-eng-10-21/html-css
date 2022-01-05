from bs4 import BeautifulSoup as bs
from src.adapters.indeed_client import *
import pdb

def test_get_indeed_html():
    results = get_indeed_html(position = 'data engineer', location = 'United States', start = 1)
    html_str = '<!DOCTYPE html>\n<html lang="en" dir="ltr">\n<head>\n<meta http-equiv="content-type" content="text/html'
    assert results.startswith(html_str)

def test_get_job_cards_returns_all_fifteen_jobs_from_page():
    cards = get_job_cards(position = 'data engineer', location = 'United States', start = 0)
    assert len(cards) == 15

def test_job_card_has_job_id():
    cards = get_job_cards(position = 'data engineer', location = 'United States', start = 0)
    do_card_ids_start_with_job = [card['id'].startswith('job') for card in cards]
    assert all(do_card_ids_start_with_job)

