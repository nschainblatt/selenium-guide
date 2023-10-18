"""Example usecase of selenium feel free to add onto this to test more feature of selenium"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Make sure to download ChromeDriver and add to PATH or if using Firefox see selenium documentation
# ChromeDriver must be opened before running script (open from terminal ./chromedriver.exe)
# ChromeDriver: https://googlechromelabs.github.io/chrome-for-testing/#stable

def main() -> None:
    """Web Driver Function"""
    service = Service('C:/webdrivers/chromedriver.exe')
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.get('http://www.google.com/') # Enter webapp url

    try:
        google_search = driver.find_element(By.ID, "APjFqb")
        google_search.send_keys("How to use selenium like a pro")
        google_search.send_keys(Keys.ENTER)

        videos_button = driver.find_element(By.XPATH, "//div[@jsname = 'bVqjv']")
        videos_button.click()

    except NoSuchElementException as err:
        print(err)

    time.sleep(60) # This is here as temp
    driver.quit()

if __name__ == "__main__":
    main()