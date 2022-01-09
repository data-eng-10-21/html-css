prices = [2500, 3000, 2000]
hoods = ['brooklyn', 'queens', 'manhattan']
descs = ['1 br', '3 br', '2 br']

results_infos = []
listings = []
for result_info in result_infos:
    housings = result_info.find_elements(By.CSS_SELECTOR, '.housing')
    price = result_info.find_element(By.CSS_SELECTOR, '.price')
    listing = {'price': price, 'housing': None}
    if len(housings) > 0:
        housing_text = housings[0].text
        listing['housing'] = housing_text
    listings.append(listing)
    
    