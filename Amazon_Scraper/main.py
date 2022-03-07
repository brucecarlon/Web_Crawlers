import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

DRIVER = webdriver.Chrome(chrome_options = chrome_options,executable_path = ChromeDriverManager().install())

#DRIVER = webdriver.Chrome(r"home/catalyst/Downloads/chromedriver")
#URL = 'https://www.amazon.com'
#DRIVER.get(URL)

def get_url(search_term):
    TEMPLATE = 'https://www.amazon.com/s?k={}&sprefix=ultawi%2Caps%2C354&ref=nb_sb_ss_sc_2_7'
    search_term.replace(' ', '+')
    return TEMPLATE.format(search_term)


URL = get_url('Apple Laptops')
DRIVER.get(URL)

soup = BeautifulSoup(DRIVER.page_source, 'html.parser')
results = soup.find_all('div',{'data-component-type': 's-search-result'})
# item = results[0]
# atag = item.h2.a
# description = atag.text.strip()
# url = 'https://www.amazon.com' + atag.get('href')
# price_parent = item.find('span', 'a-price')
# price = price_parent.find('span', 'a-offscreen').text
# rating = item.i.text

def extract_record(item):
    # description and url
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')

    #price
    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return    

    #rank
    try:
        rating = item.i.text
    except AttributeError:
        rating = ''

    result = (description,price,rating, url)

    return result

records = []
for item in results:
    record = extract_record(item)
    if record:
        records.append(record)

print(records[0])



