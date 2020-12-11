#Presented by NoobiesForNow

import html5lib
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

HEADER = {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language':'en-US , en;q=0.5'
}

URL = "https://www.amazon.in/"
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(10)
driver.get(URL)


print("What do you want?")
search_term = str(input(": "))
search_button = driver.find_element_by_id("twotabsearchtextbox")
search_term.send_keys(search_term)
search_term.send_keys(Keys.ENTER)

soup = bs4.BeautifulSoup(driver.page_source, "html5lib")

links = soup.find_all('a', attrs={"class":"a-link-normal s-no-outline"})
links_storage = []
for link in links:
    links_storage.append(link.get('href'))

for link in links_storage:
    new_webpage = driver.get(URL + link)
    new_soup = bs4.BeautifulSoup(driver.page_source, "html5lib")
    