import re
from bs4 import BeautifulSoup as bs
import requests
import pdb
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

def get_job_cards(index, position = 'data engineer', location = 'United States', start = 0):
    url = 'https://www.indeed.com/jobs'
    params = {'q': position, 'l': location, 'explvl':'entry_level', 'start': index}
    response = requests.get(url, params = params, headers=header, timeout=10)
    soup = bs(response.text, 'html.parser')
    cards = soup.findAll('a', id=re.compile('^job_'))
    return cards

def get_card_from(id):
    desc_string = f"https://www.indeed.com/rpc/jobdescs?jks={id}"
    desc_response = requests.get(desc_string, headers=header)
    description_response = desc_response.json()
    return description_response