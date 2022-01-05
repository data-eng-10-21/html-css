from bs4 import BeautifulSoup as bs
from src.adapters.indeed_adapter import *
import pdb

html_doc = """<a id="job_2bcc7676b2ad9c78" data-mobtk="1foljk4slu39p802" data-jk="2bcc7676b2ad9c78" data-hiring-event="false" rel="nofollow" data-hide-spinner="true" class="tapItem fs-unmask result job_2bcc7676b2ad9c78 resultWithShelf sponTapItem desktop" href="/company/Qloo/jobs/Data-Engineer-2bcc7676b2ad9c78?fccid=02d77e04eff44b30&amp;vjs=3" target="_blank"><div class="slider_container"><div class="slider_list"><div class="slider_item"><div class="job_seen_beacon"><table class="jobCard_mainContent big6_visualChanges" cellpadding="0" cellspacing="0" role="presentation"><tbody><tr><td class="resultContent"><div class="heading4 color-text-primary singleLineTitle tapItem-gutter"><h2 class="jobTitle jobTitle-color-purple"><span title="Data Engineer">Data Engineer</span></h2></div><div class="heading6 company_location tapItem-gutter"><pre><span class="companyName">Qloo</span><div class="companyLocation">New York, NY<!-- --> <!-- -->10012<!-- --> <span class="companyLocation--extras">(<!-- -->SoHo area<!-- -->)</span><span class="remote-bullet">•</span><span>Temporarily Remote</span></div></pre></div><div class="heading6 tapItem-gutter metadataContainer noJEMChips salaryOnly"><div class="metadata salary-snippet-container"><div class="attribute_snippet"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 13" role="presentation" aria-hidden="true" aria-label="Salary"><defs></defs><path fill="#595959" fill-rule="evenodd" d="M2.45168 6.10292c-.30177-.125-.62509-.18964-.95168-.1903V4.08678c.32693-.00053.6506-.06518.95267-.1903.30331-.12564.57891-.30979.81105-.54193.23215-.23215.4163-.50775.54194-.81106.12524-.30237.18989-.62638.19029-.95365H9.0902c0 .3283.06466.65339.1903.9567.12564.30331.30978.57891.54193.81106.23217.23215.50777.41629.81107.54193.3032.12558.6281.19024.9562.1903v1.83556c-.3242.00155-.6451.06616-.9448.19028-.3033.12563-.5789.30978-.81102.54193-.23215.23214-.4163.50774-.54193.81106-.12332.2977-.18789.61638-.19024.93849H3.99496c-.00071-.32645-.06535-.64961-.19029-.95124-.12564-.30332-.30979-.57891-.54193-.81106-.23215-.23215-.50775-.4163-.81106-.54193zM0 .589843C0 .313701.223858.0898438.5.0898438h12.0897c.2762 0 .5.2238572.5.5000002V9.40715c0 .27614-.2238.5-.5.5H.5c-.276143 0-.5-.22386-.5-.5V.589843zM6.54427 6.99849c1.10457 0 2-.89543 2-2s-.89543-2-2-2-2 .89543-2 2 .89543 2 2 2zm8.05523-2.69917v7.10958H2.75977c-.27615 0-.5.2238-.5.5v.5c0 .2761.22385.5.5.5H15.422c.4419 0 .6775-.2211.6775-.6629V4.29932c0-.27615-.2239-.5-.5-.5h-.5c-.2761 0-.5.22385-.5.5z" clip-rule="evenodd"></path></svg>$50,000 - $150,000 a year</div></div></div><div class="heading6 error-text tapItem-gutter"></div></td></tr></tbody></table><table class="jobCardShelfContainer big6_visualChanges" role="presentation"><tbody><tr class="jobCardShelf"><td class="shelfItem indeedApply"><span class="iaIcon"></span><span class="ialbl iaTextBlack">Easily apply</span></td></tr><tr class="underShelfFooter"><td><div class="heading6 tapItem-gutter result-footer"><div class="job-snippet"><ul style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;"> 
 <li style="margin-bottom:0px;">Experience working with <b>data</b> visualization tools like Tableau.</li>
 <li>Assist with architecting <b>data</b> solutions for incoming client projects.</li>
</ul></div><span class="date"><span class="visually-hidden">Employer</span>Active 15 days ago</span><span class="result-link-bar-separator">·</span><button type="button" class="sl resultLink more_links_button" aria-expanded="false">More...</button></div><div class="tab-container"><div class="more-links-container result-tab" role="presentation"><div class="more_links"><button type="button" class="close-button" title="Close" aria-label="Close"></button><ul><li><span class="mat">View all <a href="/q-Qloo-l-New-York,-NY-jobs.html">Qloo jobs in New York, NY</a> - <a href="/l-New-York,-NY-jobs.html">New York jobs</a></span></li><li><span class="mat">Salary Search: <a href="/career/data-engineer/salaries/10012--NY?campaignid=serp-more&amp;fromjk=2bcc7676b2ad9c78&amp;from=serp-more">Data Engineer salaries in New York, NY</a></span></li></ul></div></div></div></td></tr></tbody></table><div aria-live="polite"></div></div></div><div class="slider_sub_item"></div></div></div><div class="kebabMenu"><button aria-label="Job Actions" aria-haspopup="true" aria-expanded="false" class="kebabMenu-button"><svg width="24" height="24" role="presentation" aria-hidden="true" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 7C13.1 7 14 6.1 14 5C14 3.9 13.1 3 12 3C10.9 3 10 3.9 10 5C10 6.1 10.9 7 12 7ZM12 10C10.9 10 10 10.9 10 12C10 13.1 10.9 14 12 14C13.1 14 14 13.1 14 12C14 10.9 13.1 10 12 10ZM12 17C10.9 17 10 17.9 10 19C10 20.1 10.9 21 12 21C13.1 21 14 20.1 14 19C14 17.9 13.1 17 12 17Z" fill="#2d2d2d"></path></svg></button></div></a>
"""
html_doc = bs(html_doc, 'html.parser')
card = html_doc.find('a')

def test_get_id_gets_id():
    indeed_adapter = IndeedAdapter(card)
    id = indeed_adapter.get_id()
    assert id == "2bcc7676b2ad9c78"

def test_get_title():
    indeed_adapter = IndeedAdapter(card)
    assert indeed_adapter.get_title() == "Data Engineer"

def test_get_salaries():
    indeed_adapter = IndeedAdapter(card)
    return indeed_adapter.get_salaries()

def test_get_company_name():
    indeed_adapter = IndeedAdapter(card)
    assert indeed_adapter.get_company_name() == "Qloo"

def test_get_city_state():
    indeed_adapter = IndeedAdapter(card)
    city, state = indeed_adapter.get_city_state()
    assert city == 'New York'
    assert state == 'NY'

def test_run_adapter_returns_instance_of_position():
    indeed_adapter = IndeedAdapter(card)
    position = indeed_adapter.run()
    assert type(position) == Position

def test_run_adapter_returns_obj_with_correct_attributes():
    indeed_adapter = IndeedAdapter(card)
    position = indeed_adapter.run()
    obj_keys = ['id', 'title', 'salaries', 'city', 'state', 'company_name']
    obj_vals = ['2bcc7676b2ad9c78', 'Data Engineer', [50000, 150000], 
     'New York', 'NY', 'Qloo']
    
    keys = list(vars(position).keys())
    assert obj_keys == keys

def test_run_adapter_returns_obj_with_correct_values():
    indeed_adapter = IndeedAdapter(card)
    position = indeed_adapter.run()
    obj_keys = ['id', 'title', 'salaries', 'city', 'state', 'company_name']
    obj_vals = ['2bcc7676b2ad9c78', 'Data Engineer', [50000, 150000], 
     'New York', 'NY', 'Qloo']
    vals = list(vars(position).values())
    keys = list(vars(position).keys())
    assert obj_keys == keys


    



