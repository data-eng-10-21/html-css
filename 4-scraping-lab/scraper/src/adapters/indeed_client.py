import re
from bs4 import BeautifulSoup as bs
import requests
import pdb
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

def get_indeed_html(position = 'data engineer', location = 'United States', start = 0):
    url = 'https://www.indeed.com/jobs'
    params = {'q': position, 'l': location, 'explvl':'entry_level', 'start': start}
    response = requests.get(url, params = params, timeout=10)
    return response.text

    
def get_job_cards(position = 'data engineer', location = 'United States', start = 0):
  html_string = get_indeed_html(position = position, location = location, start = start)
  
  soup = bs(html_string, 'html.parser')
  cards = soup.findAll('a', {'class': 'result'})
  return cards