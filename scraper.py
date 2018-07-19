from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from random import randint
import time
import csv
import ast



def scrape():
    with open('', 'r') as userfile:
        userfilereader = csv.reader(userfile)
        for col in userfilereader:
            productlist.append(col)

    product_list = ast.literal_eval(str(productlist[0]))
    product_list = list(set(product_list))
    userfile.close()
    exp_list = []
    counter = 0
    for product in product_list:
        counter += 1
        k = randint(80, 120)
        n = randint(70, k)
        time.sleep(n)
        try:
            driver.find_element_by_xpath('//*[@id="gh-ac"]')
            button = driver.find_element_by_xpath('//*[@id="gh-ac"]')
        except NoSuchElementException:
            break
            pass
        if counter > 1:
            button.send_keys(Keys.CONTROL + "a")
        button.send_keys(product)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        source = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('li', {'class': 's-item'})
        for item in items:
            title = item.find('h3', {'class', 's-item__title'}).text
            link = item.find('a', {'class', 's-item__link'}).get('href')
            price = item.find('span', {'class': 's-item__link'}).text
            location = item.find('span', {'class': 's-item__location s-item__itemLocation'}).text
            print(title)
            print(link)
            print(location)
            print(price)






opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
driver = webdriver.Chrome("", chrome_options=opts)
driver.get("https://ebay.com")  # opens up chrome - okcupid
agent = driver.execute_script("return navigator.userAgent")
productlist = []
scrape()
driver.close()
