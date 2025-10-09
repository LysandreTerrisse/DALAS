# python -m venv my-venv
# my-venv/bin/pip install selenium
# source my-venv/bin/activate
# python -m pip install selenium
# python -m pip install webdrivermanger

# python -m webdrivermanager firefox --linkpath /usr/local/bin (doesn't work)


#import pandas
#import urllib
#from urllib import request


"""
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://youtube.com')
"""
"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import time

binary = FirefoxBinary('/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary)
driver.get('http://example.com')
"""
"""
# Initialize the Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the target website
driver.get('http://example.com')
"""

#url = 'https://youtube.com'
#text = request.urlopen(request.Request(url, headers={"User-Agent": "Mozilla/5.0"})).read()
#print(text[1:-2])


#pip install selenium
#apt install python3-selenium




# python -m venv my-venv
# my-venv/bin/pip install selenium
# source my-venv/bin/activate
# python -m pip install selenium
# python -m pip install webdrivermanger
# python -m pip install --upgrade pip


"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service = Service(executable_path='/users/Etu7/21501137/Bureau/DALAS/Project/Code/geckodriver')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)



#driver = webdriver.Firefox(executable_path='~/Bureau/DALAS/Project/Code/geckodriver')
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
"""

"""
from selenium_firefox import Firefox

ff = Firefox()
ff.get('https://www.google.com')
"""





"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary)
"""


from selenium import webdriver
driver = webdriver.Firefox()


