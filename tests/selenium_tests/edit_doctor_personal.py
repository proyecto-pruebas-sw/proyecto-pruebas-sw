import unittest
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class EditPersonalInfo(unittest.TestCase):
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

    def test_edit_name(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)
        input_name.send_keys(doctor["name"])

        submit_button = driver.find_element(By.ID, "save_changes")
        submit_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/medics/1")

    def test_edit_lastname(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys(Keys.CONTROL + "a")
        input_lastname.send_keys(Keys.DELETE)
        input_lastname.send_keys(doctor["lastname"])

        submit_button = driver.find_element(By.ID, "save_changes")
        submit_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/medics/1")

    def test_edit_rut(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(Keys.CONTROL + "a")
        input_rut.send_keys(Keys.DELETE)
        input_rut.send_keys(doctor["rut"])

        submit_button = driver.find_element(By.ID, "save_changes")
        submit_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/medics/1")

    def test_edit_birthdate(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_birthdate = driver.find_element(By.XPATH, "//*[@id='input_birthdate']")
        input_birthdate.send_keys(Keys.CONTROL + "a")
        input_birthdate.send_keys(Keys.DELETE)
        input_birthdate.send_keys(doctor["birthdate"])

        submit_button = driver.find_element(By.ID, "save_changes")
        submit_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/medics/1")

    def test_edit_city(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys(Keys.CONTROL + "a")
        input_city.send_keys(Keys.DELETE)
        input_city.send_keys(doctor["city"])

        submit_button = driver.find_element(By.ID, "save_changes")
        submit_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/doctors/1")

    def test_edit_email(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys(Keys.CONTROL + "a")
        input_email.send_keys(Keys.DELETE)
        input_email.send_keys(doctor["email"].lower())

        submit_button = driver.find_element(By.ID, "save_changes")
        submit_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/medics/1")

    def test_edit_phone(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys(Keys.CONTROL + "a")
        input_phone.send_keys(Keys.DELETE)
        input_phone.send_keys(doctor["phone"])

        submit_button = driver.find_element(By.ID, "save_changes")
        submit_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/medics/1")

    def test_empty_name(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)

        submit_button = driver.find_element(By.ID, "save_changes")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_empty_lastname(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys(Keys.CONTROL + "a")
        input_lastname.send_keys(Keys.DELETE)

        submit_button = driver.find_element(By.ID, "save_changes")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_empty_rut(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(Keys.CONTROL + "a")
        input_rut.send_keys(Keys.DELETE)

        submit_button = driver.find_element(By.ID, "save_changes")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_empty_birthdate(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_birthdate = driver.find_element(By.XPATH, "//*[@id='input_birthdate']")
        input_birthdate.send_keys(Keys.CONTROL + "a")
        input_birthdate.send_keys(Keys.DELETE)

        submit_button = driver.find_element(By.ID, "save_changes")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_edit_city(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys(Keys.CONTROL + "a")
        input_city.send_keys(Keys.DELETE)

        submit_button = driver.find_element(By.ID, "save_changes")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_empty_email(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys(Keys.CONTROL + "a")
        input_email.send_keys(Keys.DELETE)

        submit_button = driver.find_element(By.ID, "save_changes")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_empty_phone(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys(Keys.CONTROL + "a")
        input_phone.send_keys(Keys.DELETE)

        submit_button = driver.find_element(By.ID, "save_changes")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_cancel_edit(self):
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/editPersonalInfo")

        cancel_button = driver.find_element(By.ID, "cancel_button")
        cancel_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/medics/1")