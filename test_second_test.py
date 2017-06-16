import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def defaultConfig(self):
    # Set the configuration for following variables #
    SetBrowser='chrome'


    # Upto here #

    if SetBrowser=='firefox':
        self.driver = webdriver.Firefox(executable_path=r'F:\Abk\supportdrivers\geckodriver.exe')
    elif SetBrowser=='chrome':
        self.driver = webdriver.Chrome(executable_path=r"F:\Abk\supportdrivers\chromedriver.exe")
    return self

class StartpageSearch(unittest.TestCase):

    def setUp(self):
        defaultConfig(self)


    def test_search_in_startpage_org(self):
        driver = self.driver
        driver.get("https://www.startpage.com")
        elem = driver.find_element_by_id("query")
        elem.send_keys("london")
        elem = driver.find_element_by_id("submit1")
        elem.click()
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "by_time"))
            )
        finally:
            assert "paris - Startpage Web Search" in driver.title


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()