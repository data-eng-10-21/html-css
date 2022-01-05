from src.adapters.indeed_client import *
from src.models.position import Position
import requests
import re
import pdb

class IndeedAdapter:
    def __init__(self, card):
        self.card = card
        self.spans = None
        self.company_name = None
        self.get_spans()
        
        
    def run(self):
        id = self.get_id()
        title = self.get_title()
        salaries = self.get_salaries()
        location = self.get_location()
        city, state = self.get_city_state()
        company_name = self.get_company_name()
        position = Position(id, title, salaries, city, state, company_name)
        return position

    def get_id(self):
        self.id = self.card['data-jk']
        return self.id

    def get_company_name(self):
        self.company_name = self.company_name or self.card.find_all('span', {"class": "companyName"})[0].text
        return self.company_name

    def get_salaries(self):    
        salary_divs = self.card.find_all('div', {"class": "salary-snippet-container"})
        if salary_divs:
            salary_text = salary_divs[0].text
            salary_text = salary_text.replace(',', '')
            salaries =  re.findall(r'\d+', salary_text)
            self.salaries = list(sorted([int(salary) for salary in salaries]))
            return self.salaries
        else:
            return None

    def get_spans(self):
        self.spans = self.spans or self.card.findAll('span')
        return self.spans


    def get_title(self):
        for span in self.spans:
            if span.has_attr('title'):
                self.title = span.text
                return self.title

    def get_location(self):
        a_tags = self.card.find_all('a')
        hrefs = [a_tag['href'] for a_tag in a_tags]
        for href in hrefs:
            if '-l-' in href:
                _, location = href.split('-l-')
                self.location = location
                return location

    def get_city_state(self):
        location = self.get_location()
        city, state = location.split(',-')
        city, state = (city.replace('-', ' '),  state.split('-')[0])
        self.city = city
        self.state = state
        return (city, state)

    
        

    
