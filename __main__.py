from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import csv
import re
import departments


def main():
    driver = webdriver.Edge()
    website_url = "https://annuaire-plombier-france.fr/"
    driver.get(website_url)
    # acceptCookies(driver)
    driver.implicitly_wait(30)
    element = driver.find_element(by.CLASS_NAME, value='')
    print()

