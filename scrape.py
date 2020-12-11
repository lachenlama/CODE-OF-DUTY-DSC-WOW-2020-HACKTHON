#Presented by NoobiesForNow

import bs4
from selenium import webdriver

HEADER = {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language':'en-US , en;q=0.5'
}

URL = "https://www.amazon.in/"
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(10)
driver.get(URL)
