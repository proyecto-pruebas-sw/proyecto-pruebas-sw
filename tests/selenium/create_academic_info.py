import unittest
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CreateAcademicInfo(unittest.TestCase):
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

    def test_requires_degree(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addEducationInfo")

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["educations"][1]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["educations"][1]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["educations"][1]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["educations"][1]["country"])

        input_start = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[2]/div/span/input")
        input_start.send_keys(doctor["educations"][1]["start_date"])

        input_end = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[3]/div/span/input")
        input_end.send_keys(doctor["educations"][1]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_requires_description(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addEducationInfo")

        input_lastname = driver.find_element(By.ID, "input_degree")
        input_lastname.send_keys(doctor["educations"][1]["degree"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["educations"][1]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["educations"][1]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["educations"][1]["country"])

        input_start = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[2]/div/span/input")
        input_start.send_keys(doctor["educations"][1]["start_date"])

        input_end = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[3]/div/span/input")
        input_end.send_keys(doctor["educations"][1]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_requires_institution(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addEducationInfo")

        input_lastname = driver.find_element(By.ID, "input_degree")
        input_lastname.send_keys(doctor["educations"][1]["degree"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["educations"][1]["description"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["educations"][1]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["educations"][1]["country"])

        input_start = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[2]/div/span/input")
        input_start.send_keys(doctor["educations"][1]["start_date"])

        input_end = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[3]/div/span/input")
        input_end.send_keys(doctor["educations"][1]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_requires_city(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addEducationInfo")

        input_lastname = driver.find_element(By.ID, "input_degree")
        input_lastname.send_keys(doctor["educations"][1]["degree"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["educations"][1]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["educations"][1]["institution"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["educations"][1]["country"])

        input_start = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[2]/div/span/input")
        input_start.send_keys(doctor["educations"][1]["start_date"])

        input_end = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[3]/div/span/input")
        input_end.send_keys(doctor["educations"][1]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_requires_country(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addEducationInfo")

        input_lastname = driver.find_element(By.ID, "input_degree")
        input_lastname.send_keys(doctor["educations"][1]["degree"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["educations"][1]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["educations"][1]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["educations"][1]["city"])

        input_start = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[2]/div/span/input")
        input_start.send_keys(doctor["educations"][1]["start_date"])

        input_end = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[3]/div/span/input")
        input_end.send_keys(doctor["educations"][1]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")
    
    def test_requires_start(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addEducationInfo")

        input_lastname = driver.find_element(By.ID, "input_degree")
        input_lastname.send_keys(doctor["educations"][1]["degree"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["educations"][1]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["educations"][1]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["educations"][1]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["educations"][1]["country"])

        input_end = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[3]/div/span/input")
        input_end.send_keys(doctor["educations"][1]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_requires_end(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addEducationInfo")

        input_lastname = driver.find_element(By.ID, "input_degree")
        input_lastname.send_keys(doctor["educations"][1]["degree"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["educations"][1]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["educations"][1]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["educations"][1]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["educations"][1]["country"])

        input_start = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[2]/div/span/input")
        input_start.send_keys(doctor["educations"][1]["start_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")


    def test_create_academic(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addEducationInfo")

        input_lastname = driver.find_element(By.ID, "input_degree")
        input_lastname.send_keys(doctor["educations"][1]["degree"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["educations"][1]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["educations"][1]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["educations"][1]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["educations"][1]["country"])

        input_start = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[2]/div/span/input")
        input_start.send_keys(doctor["educations"][1]["start_date"])

        input_end = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div[3]/div/span/input")
        input_end.send_keys(doctor["educations"][1]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        submit_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/medics/1")
