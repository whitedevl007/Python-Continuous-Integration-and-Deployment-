"""
    Unit Test file for views
"""
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pydjango_ci_integration.settings import SITE_URL

class TaskListViewTest(TestCase):
    """
    Test View class
    """
    def test_chrome_site_homepage(self):
        # Specify the path to the ChromeDriver
        chrome_driver_path = "/usr/local/bin/chromedriver"
        
        # Set up the ChromeDriver service
        service = Service(executable_path=chrome_driver_path)
        
        # Initialize the Chrome WebDriver with the service
        browser = webdriver.Chrome(service=service)
        
        # Open the site URL
        browser.get(SITE_URL)
        
        # Check the title of the page
        self.assertIn('Semaphore', browser.title)
        
        # Close the browser
        browser.quit()
