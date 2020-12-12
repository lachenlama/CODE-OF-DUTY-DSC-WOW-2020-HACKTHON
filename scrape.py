#Presented by NoobiesForNow
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Search import search
from Deal_of_the_day import deal_of_the_day

HEADER = {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language':'en-US , en;q=0.5'
}

URL = "https://www.amazon.in/"
while True:
    choose = int(input("'1' to search,\n'2' to open deals of the day\n: "))
    
    if choose == 1:
        search()

    elif choose == 2:
        deal_of_the_day()

    else:
        print("Try again")