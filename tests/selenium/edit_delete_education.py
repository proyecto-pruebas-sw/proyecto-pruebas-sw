import unittest
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

class EditDoctorEducation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("backend/doctor/education_data.json") as file:
            cls.edit_data = json.load(file)
            file.close()
    
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    '''def test_1_edit_button_only(self):
        driver = self.driver
        driver.get("http://localhost:3000/medics/1")
        time.sleep(1)

        # Click edit button
        edit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Editar']")
        edit_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/medics/1/1/edit-education")

    def test_2_correct_edit(self):
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/1/edit-education")
        correct_edit_data = self.edit_data["educations"]["correct_edit"]

        text_inputs_ids = ["input_degree", "input_institution", "input_city", "input_country",]
        date_inputs_ids = ["input_start", "input_end"]

        for id in text_inputs_ids:
            element = driver.find_element(By.ID, id)
            element.clear()
            element.send_keys(correct_edit_data[id])

        for id in date_inputs_ids:
            element = driver.find_element(By.CSS_SELECTOR, f"#{id} input")
            element.send_keys(correct_edit_data[id])

        save_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Crear Antecedente']")
        save_button.click()

        self.assertEqual(driver.current_url, "http://localhost:3000/medics/1")

        time.sleep(1)

        # Check if the doctor's edited education is correct
        container_with_educations = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/div[8]')
        div_with_education = container_with_educations.find_elements(By.XPATH, ".//div[@class='education-detail']")[0]

        # Get job title
        education_degree_html = div_with_education.find_element(By.CSS_SELECTOR, "h4")
        education_degree = education_degree_html.text
        self.assertEqual(education_degree, correct_edit_data["input_degree"])

        # Get institution
        education_institution_html = div_with_education.find_element(By.XPATH, ".//span[@class='block']")
        education_institution = education_institution_html.text
        self.assertEqual(education_institution, correct_edit_data["input_institution"])

        # Get city and country
        education_city_country_html = div_with_education.find_element(By.XPATH, ".//span[@class='block'][2]")
        education_city_country = education_city_country_html.text
        self.assertEqual(education_city_country, correct_edit_data["input_city"]+", "+correct_edit_data["input_country"])

        # Get end date
        education_end_date_html = div_with_education.find_element(By.XPATH, ".//span[@class='block'][3]")
        education_end_date_raw = education_end_date_html.text
        regex = re.compile(r'(\d{4}-\d{2}-)(?:\d{1})(\d{1})')
        find_date = regex.search(education_end_date_raw)
        education_end_date = find_date.group(1) + find_date.group(2)
        self.assertEqual(education_end_date, correct_edit_data["input_end"])
    
    def default_missing_fields(self, empty_field):
        driver = self.driver
        driver.get("http://localhost:3000/medics/1/1/edit-education")
        empty_data = self.edit_data["educations"][empty_field]

        text_inputs_ids = ["input_degree", "input_institution", "input_city", "input_country",]
        date_inputs_ids = ["input_start", "input_end"]

        for id in text_inputs_ids:
            element = driver.find_element(By.ID, id)
            element.clear()
            element.send_keys(empty_data[id])

        for id in date_inputs_ids:
            element = driver.find_element(By.CSS_SELECTOR, f"#{id} input")
            element.send_keys(empty_data[id])

        save_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Crear Antecedente']")
        self.assertEqual(save_button.get_attribute("disabled"), "true")

    def test_3_all_empty(self):
        self.default_missing_fields("all_empty")

    def test_4_degree_empty(self):
        self.default_missing_fields("degree_empty")

    def test_5_institution_empty(self):
        self.default_missing_fields("institution_empty")

    def test_6_city_empty(self):
        self.default_missing_fields("city_empty")

    def test_7_country_empty(self):
        self.default_missing_fields("country_empty")

    def test_8_start_empty(self):
        self.default_missing_fields("start_empty")

    def test_9_end_empty(self):
        self.default_missing_fields("end_empty")

    def test_10_end_before_start(self):
        self.default_missing_fields("end_before_start")'''
    
    def test_11_delete_education(self):
        driver = self.driver
        driver.get("http://localhost:3000/medics/1")
        time.sleep(1)

        # Click delete button
        edit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Eliminar']")
        edit_button.click()

        time.sleep(3)

        # Click confirm button
        confirm_button = driver.find_element(By.CSS_SELECTOR, "button.p-confirm-dialog-accept")
        confirm_button.click()

        # Refresh page
        driver.refresh()

        # Search for the education
        try:
            edit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Eliminar']")
        except:
            edit_button = None
        
        self.assertEqual(edit_button, None)