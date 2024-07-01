import unittest
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DoctorCreate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("backend/doctor/post_data.json") as file:
            cls.data = json.load(file)
            cls.data = cls.data["doctors"][0]
            file.close()

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close() 
    
    def test_require_name(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/new")

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys(doctor["lastname"])

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(doctor["rut"])

        input_birthdate = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div[1]/div[4]/div/span/input")
        input_birthdate.send_keys(doctor["birthdate"])

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys(doctor["city"])

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys(doctor["email"].lower())

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys(doctor["phone"])

        specialty_dropdown = driver.find_element(By.ID, "multiselect_specialties")
        specialty_dropdown.click()

        specialty_option_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[1]/span")
        specialty_option_1.click()

        specialty_option_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[5]/span")
        specialty_option_2.click()

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_require_lastname(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/new")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys(doctor["name"])

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(doctor["rut"])

        input_birthdate = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div[1]/div[4]/div/span/input")
        input_birthdate.send_keys(doctor["birthdate"])

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys(doctor["city"])

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys(doctor["email"].lower())

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys(doctor["phone"])

        specialty_dropdown = driver.find_element(By.ID, "multiselect_specialties")
        specialty_dropdown.click()

        specialty_option_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[1]/span")
        specialty_option_1.click()

        specialty_option_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[5]/span")
        specialty_option_2.click()

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_require_rut(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/new")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys(doctor["name"])

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys(doctor["lastname"])

        input_birthdate = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div[1]/div[4]/div/span/input")
        input_birthdate.send_keys(doctor["birthdate"])

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys(doctor["city"])

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys(doctor["email"].lower())

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys(doctor["phone"])

        specialty_dropdown = driver.find_element(By.ID, "multiselect_specialties")
        specialty_dropdown.click()

        specialty_option_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[1]/span")
        specialty_option_1.click()

        specialty_option_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[5]/span")
        specialty_option_2.click()

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_require_city(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/new")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys(doctor["name"])

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys(doctor["lastname"])

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(doctor["rut"])

        input_birthdate = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div[1]/div[4]/div/span/input")
        input_birthdate.send_keys(doctor["birthdate"])

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys(doctor["email"].lower())

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys(doctor["phone"])

        specialty_dropdown = driver.find_element(By.ID, "multiselect_specialties")
        specialty_dropdown.click()

        specialty_option_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[1]/span")
        specialty_option_1.click()

        specialty_option_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[5]/span")
        specialty_option_2.click()

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")
    
    def test_require_email(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/new")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys(doctor["name"])

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys(doctor["lastname"])

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(doctor["rut"])

        input_birthdate = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div[1]/div[4]/div/span/input")
        input_birthdate.send_keys(doctor["birthdate"])

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys(doctor["city"])

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys(doctor["phone"])

        specialty_dropdown = driver.find_element(By.ID, "multiselect_specialties")
        specialty_dropdown.click()

        specialty_option_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[1]/span")
        specialty_option_1.click()

        specialty_option_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[5]/span")
        specialty_option_2.click()

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_require_phone(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/new")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys(doctor["name"])

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys(doctor["lastname"])

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(doctor["rut"])

        input_birthdate = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div[1]/div[4]/div/span/input")
        input_birthdate.send_keys(doctor["birthdate"])

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys(doctor["city"])

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys(doctor["email"].lower())

        specialty_dropdown = driver.find_element(By.ID, "multiselect_specialties")
        specialty_dropdown.click()

        specialty_option_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[1]/span")
        specialty_option_1.click()

        specialty_option_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[5]/span")
        specialty_option_2.click()

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    
    def test_require_birthdate(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/new")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys(doctor["name"])

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys(doctor["lastname"])

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(doctor["rut"])

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys(doctor["city"])

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys(doctor["email"].lower())

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys(doctor["phone"])

        specialty_dropdown = driver.find_element(By.ID, "multiselect_specialties")
        specialty_dropdown.click()

        specialty_option_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[1]/span")
        specialty_option_1.click()

        specialty_option_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[5]/span")
        specialty_option_2.click()

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")
    
    def test_require_specialty(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/new")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys(doctor["name"])

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys(doctor["lastname"])

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(doctor["rut"])

        input_birthdate = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div[1]/div[4]/div/span/input")
        input_birthdate.send_keys(doctor["birthdate"])

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys(doctor["city"])

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys(doctor["email"].lower())

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys(doctor["phone"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")
    
    def test_cancel_create(self):
        driver = self.driver
        driver.get("http://localhost:3000/medics/new")

        cancel_button = driver.find_element(By.ID, "cancel_button")
        cancel_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/")

    def test_create_doctor(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/new")

        input_name = driver.find_element(By.ID, "input_name")
        input_name.send_keys(doctor["name"])

        input_lastname = driver.find_element(By.ID, "input_lastname")
        input_lastname.send_keys(doctor["lastname"])

        input_rut = driver.find_element(By.ID, "input_rut")
        input_rut.send_keys(doctor["rut"])

        input_birthdate = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/div[1]/div[4]/div/span/input")
        input_birthdate.send_keys(doctor["birthdate"])

        input_city = driver.find_element(By.ID, "input_city")
        input_city.send_keys(doctor["city"])

        input_email = driver.find_element(By.ID, "input_email")
        input_email.send_keys(doctor["email"].lower())

        input_phone = driver.find_element(By.ID, "input_phone")
        input_phone.send_keys(doctor["phone"])

        specialty_dropdown = driver.find_element(By.ID, "multiselect_specialties")
        specialty_dropdown.click()

        specialty_option_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[1]/span")
        specialty_option_1.click()

        specialty_option_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[5]/span")
        specialty_option_2.click()

        submit_button = driver.find_element(By.ID, "create_button")
        submit_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/")




