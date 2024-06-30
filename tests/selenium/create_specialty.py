from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import json

class SpecialtyCreate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("backend/doctor/expected_data.json") as file:
            cls.expected_data = json.load(file)
            file.close()

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_create_specialty(self):
        driver = self.driver
        driver.get("http://localhost:3000/specialties")
        
        # Click on the create button
        create_button = driver.find_element(By.ID, "link_new_specialty")
        create_button.click()
        # Fill the form
        input_name = driver.find_element(By.ID, "specialty")
        input_name.send_keys("hematologia")
        # Submit the form
        submit_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div/button")
        submit_button.click()

    def test_create_require_name(self):
        driver = self.driver
        driver.get("http://localhost:3000/specialties")
        
        # Click on the create button
        create_button = driver.find_element(By.ID, "link_new_specialty")
        create_button.click()
        # Submit the form
        submit_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div/button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")
    
    def test_cancel_create(self):
        driver = self.driver
        driver.get("http://localhost:3000/specialties")
        
        # Click on the create button
        create_button = driver.find_element(By.ID, "link_new_specialty")
        create_button.click()
        # Click on the cancel button
        cancel_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div/a/button")
        cancel_button.click()
        # Verify if the route changed to /specialties
        self.assertEqual(driver.current_url, "http://localhost:3000/specialties")