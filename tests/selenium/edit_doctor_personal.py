import unittest
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class EditPersonalInfo(unittest.TestCase):
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

    def test_edit_name(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys(doctor["name"])

        submit_button = driver.find_element(By.ID, "create_button")
        submit_button.click()

        self.assertEqual(driver.current_url, f"http://localhost:3000/doctors/{doctor["id"]}")

    def test_edit_lastname(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys(doctor["lastname"])

        submit_button = driver.find_element(By.ID, "create_button")
        submit_button.click()

        self.assertEqual(driver.current_url, f"http://localhost:3000/doctors/{doctor["id"]}")

    def test_edit_rut(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(doctor["rut"])

        submit_button = driver.find_element(By.ID, "create_button")
        submit_button.click()

        self.assertEqual(driver.current_url, f"http://localhost:3000/doctors/{doctor["id"]}")

    def test_edit_birthdate(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_birthdate = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div[1]/div[4]/div/span/input")
        input_birthdate.send_keys(doctor["birthdate"])

        submit_button = driver.find_element(By.ID, "create_button")
        submit_button.click()

        self.assertEqual(driver.current_url, f"http://localhost:3000/doctors/{doctor["id"]}")

    def test_edit_city(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys(doctor["city"])

        submit_button = driver.find_element(By.ID, "create_button")
        submit_button.click()

        self.assertEqual(driver.current_url, f"http://localhost:3000/doctors/{doctor["id"]}")

    def test_edit_email(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys(doctor["email"].lower())

        submit_button = driver.find_element(By.ID, "create_button")
        submit_button.click()

        self.assertEqual(driver.current_url, f"http://localhost:3000/doctors/{doctor["id"]}")

    def test_edit_phone(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys(doctor["phone"])

        submit_button = driver.find_element(By.ID, "create_button")
        submit_button.click()

        self.assertEqual(driver.current_url, f"http://localhost:3000/doctors/{doctor["id"]}")

    def test_empty_name(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys("")

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_empty_lastname(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys("")

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_empty_rut(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(doctor["rut"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_empty_birthdate(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_birthdate = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div[1]/div[4]/div/span/input")
        input_birthdate.send_keys("")

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_edit_city(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys("")

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_empty_email(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys("")

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_edit_phone(self):
        doctor = self.data
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys("")

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_cancel_edit(self):
        driver = self.driver
        driver.get(f"http://localhost:3000/doctors/{doctor["id"]}/edit")

        cancel_button = driver.find_element(By.ID, "cancel_button")
        cancel_button.click()

        self.assertEqual(driver.current_url, f"http://localhost:3000/doctors/{doctor["id"]}")