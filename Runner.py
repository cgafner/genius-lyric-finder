# Christian Gafner Jan. 25, 2021
# Genius Lyrics Web Scraper

# Necessary Imports for project
# Selenium used for webscraping

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from win32api import GetSystemMetrics
import time


def main():

    # Pass genius link to webdriver (browser)
    # Also sets window size to half screen width (left aligned)

    url = 'https://genius.com/'
    browser = webdriver.Chrome()
    browser.get(url)
    browser.set_window_size((GetSystemMetrics(0)/2), GetSystemMetrics(1))
    browser.set_window_position(-10, 0)

    # Finds the search bar element and enters user's song

    browser.find_element(By.XPATH, '//input[@name="q"]').send_keys(input('Enter your song & artist name. (Ex. The Real Slim Shady Eminem): '))
    time.sleep(2)

    # Using ActionChains to 'press' Enter key.

    actions = ActionChains(browser)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    # Selects the first suggestion (If song is typed incorrectly, or isn't unique specifiying author may help avoid wrong selection error.)

    time.sleep(2)
    browser.find_element_by_class_name('mini_card').send_keys(Keys.ENTER)

    # GETS TO SPECIFIED LYRICS. NOW COPY AND PRINT LYRICS

    time.sleep(2)
    lyrics = browser.find_element(By.CLASS_NAME, 'lyrics')
    print(lyrics.text)

    # PRINTS LYRICS SUCCESSFULLY

    time.sleep(1)

    # Closes browser after printing lyrics

    browser.close()
    choice()


def close():
    exit()

    # Asks user to run again


def choice():
    while 'Error, please try again':
        option = str(input('Find another song? y or n ').lower().strip())
        if option[:1] == 'y':
            main()
        if option[:1] == 'n':
            close()

main()
