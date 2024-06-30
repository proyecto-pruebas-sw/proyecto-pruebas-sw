from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import json

class SpecialtyList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("backend/doctor/initial_data.json") as file:
            cls.initial_data = json.load(file)
            file.close()

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_list_specialty(self):
        driver = self.driver
        driver.get("http://localhost:3000/specialties")
        # Verify if the list is empty
        specialties = driver.find_elements(By.XPATH, "/html/body/div/div/div/div[2]/div[3]/div[1]/table/tbody/tr")

        for i in range(len(specialties)):
            self.assertIn(self.initial_data["specialties"][i]["name"], specialties[i].text)