import unittest
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

class DoctorRemove(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("backend/doctor/patch_data.json") as file:
            cls.data = json.load(file)
            cls.data = cls.data["doctors"][0]
            file.close()

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close() 

    def test_remove_doctor(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/medics/1")

        remove_button = driver.find_element(By.ID, "remove_medic")
        remove_button.click()

        Alert(driver).accept()

        self.assertEqual(driver.current_url, "http://localhost:3000/")