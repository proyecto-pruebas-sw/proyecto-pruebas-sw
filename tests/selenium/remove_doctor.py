import unittest
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DoctorRemove(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("backend/doctor/patch_data.json") as file:
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

        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Eliminar')]"))
        )
        accept_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/")