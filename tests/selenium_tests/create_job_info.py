import unittest
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CreateJobInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("data/patch_data.json") as file:
            cls.data = json.load(file)
            cls.data = cls.data["doctors"][0]
            file.close()

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)

    def tearDown(self):
        self.driver.close()

    def test_requires_job_title(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addExperienceInfo")

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["experiences"][0]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["experiences"][0]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["experiences"][0]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["experiences"][0]["country"])

        input_start = driver.find_element(By.XPATH, "//*[@id='input_start']")
        input_start.send_keys(doctor["experiences"][0]["start_date"])

        input_end = driver.find_element(By.XPATH, "//*[@id='input_end']")
        input_end.send_keys(doctor["experiences"][0]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_requires_description(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addExperienceInfo")

        input_lastname = driver.find_element(By.ID, "input_job_title")
        input_lastname.send_keys(doctor["experiences"][0]["job_title"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["experiences"][0]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["experiences"][0]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["experiences"][0]["country"])

        input_start = driver.find_element(By.XPATH, "//*[@id='input_start']")
        input_start.send_keys(doctor["experiences"][0]["start_date"])

        input_end = driver.find_element(By.XPATH, "//*[@id='input_end']")
        input_end.send_keys(doctor["experiences"][0]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_requires_institution(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addExperienceInfo")

        input_lastname = driver.find_element(By.ID, "input_job_title")
        input_lastname.send_keys(doctor["experiences"][0]["job_title"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["experiences"][0]["description"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["experiences"][0]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["experiences"][0]["country"])

        input_start = driver.find_element(By.XPATH, "//*[@id='input_start']")
        input_start.send_keys(doctor["experiences"][0]["start_date"])

        input_end = driver.find_element(By.XPATH, "//*[@id='input_end']")
        input_end.send_keys(doctor["experiences"][0]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_requires_city(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addExperienceInfo")

        input_lastname = driver.find_element(By.ID, "input_job_title")
        input_lastname.send_keys(doctor["experiences"][0]["job_title"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["experiences"][0]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["experiences"][0]["institution"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["experiences"][0]["country"])

        input_start = driver.find_element(By.XPATH, "//*[@id='input_start']")
        input_start.send_keys(doctor["experiences"][0]["start_date"])

        input_end = driver.find_element(By.XPATH, "//*[@id='input_end']")
        input_end.send_keys(doctor["experiences"][0]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_requires_country(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addExperienceInfo")

        input_lastname = driver.find_element(By.ID, "input_job_title")
        input_lastname.send_keys(doctor["experiences"][0]["job_title"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["experiences"][0]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["experiences"][0]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["experiences"][0]["city"])

        input_start = driver.find_element(By.XPATH, "//*[@id='input_start']")
        input_start.send_keys(doctor["experiences"][0]["start_date"])

        input_end = driver.find_element(By.XPATH, "//*[@id='input_end']")
        input_end.send_keys(doctor["experiences"][0]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_requires_start(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addExperienceInfo")

        input_lastname = driver.find_element(By.ID, "input_job_title")
        input_lastname.send_keys(doctor["experiences"][0]["job_title"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["experiences"][0]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["experiences"][0]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["experiences"][0]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["experiences"][0]["country"])

        input_end = driver.find_element(By.XPATH, "//*[@id='input_end']")
        input_end.send_keys(doctor["experiences"][0]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")

    def test_requires_end(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addExperienceInfo")

        input_lastname = driver.find_element(By.ID, "input_job_title")
        input_lastname.send_keys(doctor["experiences"][0]["job_title"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["experiences"][0]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["experiences"][0]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["experiences"][0]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["experiences"][0]["country"])

        input_start = driver.find_element(By.XPATH, "//*[@id='input_start']")
        input_start.send_keys(doctor["experiences"][0]["start_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        self.assertEqual(submit_button.get_attribute("disabled"), "true")


    def test_create_experience(self):
        doctor = self.data
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/addExperienceInfo")

        input_lastname = driver.find_element(By.ID, "input_job_title")
        input_lastname.send_keys(doctor["experiences"][0]["job_title"])

        input_lastname = driver.find_element(By.ID, "input_description")
        input_lastname.send_keys(doctor["experiences"][0]["description"])

        input_lastname = driver.find_element(By.ID, "input_institution")
        input_lastname.send_keys(doctor["experiences"][0]["institution"])

        input_lastname = driver.find_element(By.ID, "input_city")
        input_lastname.send_keys(doctor["experiences"][0]["city"])

        input_lastname = driver.find_element(By.ID, "input_country")
        input_lastname.send_keys(doctor["experiences"][0]["country"])

        input_start = driver.find_element(By.XPATH, "//*[@id='input_start']")
        input_start.send_keys(doctor["experiences"][0]["start_date"])

        input_end = driver.find_element(By.XPATH, "//*[@id='input_end']")
        input_end.send_keys(doctor["experiences"][0]["end_date"])

        submit_button = driver.find_element(By.ID, "create_button")
        submit_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/medics/1")