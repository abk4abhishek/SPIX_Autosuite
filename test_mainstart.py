import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def defaultConfig(cls):
    # Set the configuration for following variables #
    SetBrowser='chrome'


    # Upto here #

    if SetBrowser=='firefox':
        cls.driver = webdriver.Firefox(executable_path=r'F:\Abk\supportdrivers\geckodriver.exe')
    elif SetBrowser=='chrome':
        cls.driver = webdriver.Chrome(executable_path=r"F:\Abk\supportdrivers\chromedriver.exe")
    return cls

class StartpageSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        defaultConfig(cls)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print ('\nEnd of all Test Cases')

    def setUp(self):
        print (self.shortDescription())

    def tearDown(self):
        print ("\n----- End of Test Case ------",self.shortDescription())


    def test_search_in_startpage_org1(self):
        """Validation of search1"""
        driver = self.driver
        driver.get("https://www.startpage.com")
        elem = driver.find_element_by_id("query")
        elem.send_keys("paris")
        elem = driver.find_element_by_id("submit1")
        elem.click()
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "by_time"))
            )
        finally:
            assert "paris - Startpage Web Search" in driver.title

    def test_search_in_startpage_org2(self):
        """Validation of search2"""
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


if __name__ == "__main__":
    unittest.main()