from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import json
import re

class DetailDoctor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("backend/doctor/initial_data.json") as file:
            cls.detail_data = json.load(file)
            file.close()
    
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def default_test(self, doctor_id):
        doctor_detail_expected = self.detail_data["doctors"][doctor_id-1]
        specialties = self.detail_data["specialties"]
        driver = self.driver
        driver.get(f"http://localhost:3000/medics/{doctor_id}")

        # Check if the doctor's name is correct
        doctor_name_html = driver.find_element(By.CSS_SELECTOR, "h2")
        doctor_name = doctor_name_html.text
        self.assertEqual(doctor_name, (doctor_detail_expected["name"]+" "+doctor_detail_expected["lastname"]))

        # Check if the doctor's specialties are correct
        container_with_specialties = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[4]')
        divs_with_span = container_with_specialties.find_elements(By.XPATH, ".//div[.//span]")
        for index, div in enumerate(divs_with_span):
            span = div.find_element(By.XPATH, ".//span")
            specialty_index = doctor_detail_expected["specialties"][index] - 1
            self.assertEqual(span.text, specialties[specialty_index]["name"])
        
        # Check if the doctor's city is correct
        doctor_city_html = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[5]/div[1]')
        doctor_city = doctor_city_html.text
        self.assertEqual(doctor_city, doctor_detail_expected["city"])

        # Check if the doctor's email is correct
        doctor_email_html = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[5]/div[2]')
        doctor_email = doctor_email_html.text
        self.assertEqual(doctor_email, doctor_detail_expected["email"])

        # Check if the doctor's phone is correct
        doctor_phone_html = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[5]/div[3]')
        doctor_phone = doctor_phone_html.text
        self.assertEqual(doctor_phone, doctor_detail_expected["phone"])

        # Check if the doctor's educations are correct
        container_with_educations = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[8]')
        divs_with_educations = container_with_educations.find_elements(By.XPATH, ".//div[@class='education-detail']")
        for index, div in enumerate(divs_with_educations):
            doctor_education_detail = doctor_detail_expected["educations"][index]

            # Get job title
            education_degree_html = div.find_element(By.CSS_SELECTOR, "h4")
            education_degree = education_degree_html.text
            self.assertEqual(education_degree, doctor_education_detail["degree"])

            # Get institution
            education_institution_html = div.find_element(By.XPATH, ".//span[@class='block']")
            education_institution = education_institution_html.text
            self.assertEqual(education_institution, doctor_education_detail["institution"])

            # Get city and country
            education_city_country_html = div.find_element(By.XPATH, ".//span[@class='block'][2]")
            education_city_country = education_city_country_html.text
            self.assertEqual(education_city_country, doctor_education_detail["city"]+", "+doctor_education_detail["country"])

            # Get end date
            education_end_date_html = div.find_element(By.XPATH, ".//span[@class='block'][3]")
            education_end_date_raw = education_end_date_html.text
            regex = re.compile(r'(\d{4}-\d{2}-\d{2})')
            education_end_date = regex.search(education_end_date_raw).group(1)
            self.assertEqual(education_end_date, doctor_education_detail["end_date"])

        # Change to experience tab
        experience_tab = driver.find_element(By.CSS_SELECTOR, 'a[aria-label=Experiencia]')
        experience_tab.click()

        # Check if the doctor's experience are correct
        container_with_experiences = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[8]')
        divs_with_experiences = container_with_experiences.find_elements(By.XPATH, ".//div[@class='experience-detail']")
        for index, div in enumerate(divs_with_experiences):
            doctor_experience_detail = doctor_detail_expected["experiences"][index]

            # Get job title
            experience_job_title_html = div.find_element(By.CSS_SELECTOR, "h4")
            experience_job_title = experience_job_title_html.text
            self.assertEqual(experience_job_title, doctor_experience_detail["job_title"])

            # Get institution
            experience_institution_html = div.find_element(By.XPATH, ".//span[@class='block']")
            experience_institution = experience_institution_html.text
            self.assertEqual(experience_institution, doctor_experience_detail["institution"])

            # Get city and country
            experience_city_country_html = div.find_element(By.XPATH, ".//span[@class='block'][2]")
            experience_city_country = experience_city_country_html.text
            self.assertEqual(experience_city_country, doctor_experience_detail["city"]+", "+doctor_experience_detail["country"])

            # Get start date
            experience_start_date_html = div.find_element(By.XPATH, ".//span[@class='block'][3]")
            experience_start_date_raw = experience_start_date_html.text
            regex = re.compile(r'(\d{4}-\d{2}-\d{2})')
            experience_start_date = regex.search(experience_start_date_raw).group(1)
            self.assertEqual(experience_start_date, doctor_experience_detail["start_date"])

            # Get end date
            experience_end_date_html = div.find_element(By.XPATH, ".//span[@class='block'][4]")
            experience_end_date_raw = experience_end_date_html.text
            experience_end_date = regex.search(experience_end_date_raw).group(1)
            self.assertEqual(experience_end_date, doctor_experience_detail["end_date"])
    
    def test_1_detail_doctor_1_specialty_1_or_more_experience_1_education(self):
        self.default_test(doctor_id=1)

    def test_2_detail_doctor_1_or_more_specialty_1_or_more_experience_1_education(self):
        self.default_test(doctor_id=4)

    def test_3_detail_doctor_1_specialty_1__experience_1_education(self):
        self.default_test(doctor_id=3)

    def test_4_detail_doctor_1_specialty_0__experience_1_education(self):
        self.default_test(doctor_id=5)