from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

class DoctorSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_list_all_doctors(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        self.assertIn("Vite + React", driver.title)

    def tearDown(self):
        self.driver.close()

    


