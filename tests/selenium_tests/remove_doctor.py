import unittest
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DoctorRemove(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("selenium_tests/data/patch_data.json") as file:
            cls.data = json.load(file)
            cls.data = cls.data["doctors"][0]
            file.close()

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)

    def tearDown(self):
        self.driver.close() 

    def test_remove_doctor(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/medics/1")

        remove_button = driver.find_element(By.ID, "remove_medic")
        remove_button.click()

        confirm_dialog = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".p-confirm-dialog"))
        )

        accept_button = confirm_dialog.find_element(By.XPATH, "//button[contains(@class, 'p-confirm-dialog-accept')]")
        accept_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/")