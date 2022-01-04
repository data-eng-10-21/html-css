from bs4 import BeautifulSoup as bs
from src.adapters.indeed_adapter import *
import pdb

html_doc = """<a class="tapItem fs-unmask result job_0601c9a2ee3bd7d2 resultWithShelf sponTapItem desktop" data-hide-spinner="true" data-hiring-event="false" data-jk="0601c9a2ee3bd7d2" data-mobtk="1fh4a8803u3h9800" href="/company/Spanidea-Systemms/jobs/Data-Engineer-0601c9a2ee3bd7d2?fccid=0a5e5d99562cc095&amp;vjs=3" id="job_0601c9a2ee3bd7d2" rel="nofollow" target="_blank"><div class="slider_container"><div class="slider_list"><div class="slider_item"><div class="job_seen_beacon"><table cellpadding="0" cellspacing="0" class="jobCard_mainContent" role="presentation"><tbody><tr><td class="resultContent"><div class="heading4 color-text-primary singleLineTitle tapItem-gutter"><h2 class="jobTitle jobTitle-color-purple jobTitle-newJob"><div class="new topLeft holisticNewBlue desktop"><span class="label">new</span></div><span title="Data Engineer">Data Engineer</span></h2></div><div class="heading6 company_location tapItem-gutter"><pre><span class="companyName">Spanidea Systemms</span><div class="companyLocation">San Francisco Bay Area, CA<span class="remote-bullet">•</span><span>Remote</span></div></pre></div><div class="heading6 tapItem-gutter metadataContainer"><div class="metadata salary-snippet-container"><span aria-label="Up to $180,000 a year" class="salary-snippet">Up to $180,000 a year</span></div></div><div class="heading6 error-text tapItem-gutter"></div></td></tr></tbody></table><table class="jobCardShelfContainer" role="presentation"><tbody><tr class="jobCardShelf"><td class="shelfItem indeedApply"><span class="iaIcon"></span><span class="ialbl iaTextBlack">Easily apply</span></td></tr><tr class="underShelfFooter"><td><div class="heading6 tapItem-gutter result-footer"><div class="job-snippet"><ul style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;">
<li>Data Reporting Engineering Contractor, you will work with the data-engineering team to build and enhance partner and client reports using pyspark, spark/scala,…</li>
</ul></div><span class="date">Active 4 days ago</span><span class="result-link-bar-separator">·</span><button aria-expanded="false" class="sl resultLink more_links_button" type="button">More...</button></div><div class="tab-container"><div class="more-links-container result-tab" role="presentation"><div class="more_links"><button class="close-button" title="Close" type="button"></button><ul><li><span class="mat">View all <a href="/q-Spanidea-Systemms-l-San-Francisco-Bay-Area,-CA-jobs.html">Spanidea Systemms jobs in San Francisco Bay Area, CA</a> - <a href="/l-San-Francisco-Bay-Area,-CA-jobs.html">San Francisco Bay Area jobs</a></span></li><li><span class="mat">Salary Search: <a href="/career/data-engineer/salaries/San-Francisco-Bay-Area--CA?campaignid=serp-more&amp;fromjk=0601c9a2ee3bd7d2&amp;from=serp-more">Data Engineer salaries in San Francisco Bay Area, CA</a></span></li></ul></div></div></div></td></tr></tbody></table><div aria-live="polite"></div></div></div><div class="slider_sub_item"></div></div></div><div class="kebabMenu"><button aria-expanded="false" aria-haspopup="true" aria-label="Job Actions" class="kebabMenu-button"><svg fill="none" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M12 7C13.1 7 14 6.1 14 5C14 3.9 13.1 3 12 3C10.9 3 10 3.9 10 5C10 6.1 10.9 7 12 7ZM12 10C10.9 10 10 10.9 10 12C10 13.1 10.9 14 12 14C13.1 14 14 13.1 14 12C14 10.9 13.1 10 12 10ZM12 17C10.9 17 10 17.9 10 19C10 20.1 10.9 21 12 21C13.1 21 14 20.1 14 19C14 17.9 13.1 17 12 17Z" fill="#2d2d2d"></path></svg></button></div></a>
"""
html_doc = bs(html_doc, 'html.parser')
card = html_doc.find('a')

def test_get_id_gets_id():
    indeed_adapter = IndeedAdapter(card)
    id = indeed_adapter.get_id()
    assert id == "0601c9a2ee3bd7d2"

def test_get_title():
    indeed_adapter = IndeedAdapter(card)
    assert indeed_adapter.get_title() == "Data Engineer"

def test_get_salaries():
    indeed_adapter = IndeedAdapter(card)
    return indeed_adapter.get_salaries()

def test_get_description():
    indeed_adapter = IndeedAdapter(card)
    description = indeed_adapter.get_description()
    test_desc = '<p>Data Reporting Engineering Contractor, you will work with the data-engineering team to build and enhance partner and client reports using pyspark, spark/scala, and AWS EMR, S3, and snowflake. Includes Development, testing, and validatio</p><p>Job Type: Full-time</p><p>Salary: Up to $180,000.00 per year</p><p>Schedule:</p><ul><li>8 hour shift</li></ul><p>Work Remotely:</p><ul><li>Yes</li></ul>'
    assert description == test_desc

def test_get_company_name():
    indeed_adapter = IndeedAdapter(card)
    assert indeed_adapter.get_company_name() == "Spanidea Systemms"

def test_get_city_state():
    indeed_adapter = IndeedAdapter(card)
    city, state = indeed_adapter.get_city_state()
    assert city == 'San Francisco Bay Area'
    assert state == 'CA'

def test_run_adapter():
    indeed_adapter = IndeedAdapter(card)
    position = indeed_adapter.run()
    obj_keys = ['id', 'title', 'salaries', 'description', 'city', 'state', 'company_name']
    obj_vals = ['0601c9a2ee3bd7d2', 'Data Engineer', [180000], 
    '<p>Data Reporting Engineering Contractor, you will work with the data-engineering team to build and enhance partner and client reports using pyspark, spark/scala, and AWS EMR, S3, and snowflake. Includes Development, testing, and validatio</p><p>Job Type: Full-time</p><p>Salary: Up to $180,000.00 per year</p><p>Schedule:</p><ul><li>8 hour shift</li></ul><p>Work Remotely:</p><ul><li>Yes</li></ul>',
     'San Francisco Bay Area', 'CA', 'Spanidea Systemms']
    vals = list(vars(position).values())
    keys = list(vars(position).keys())
    assert obj_keys == keys
    assert obj_vals == vals
    
    


