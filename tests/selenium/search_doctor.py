from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import json

class DoctorSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("backend/doctor/expected_data.json") as file:
            cls.expected_data = json.load(file)
            file.close()

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_list_all_doctors(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        
        # Verify that the doctors are displayed correctly
        for doctor in self.expected_data["get"]:
            self.assertEqual(doctor["name"] + " " + doctor["lastname"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_name').text)
            self.assertEqual(doctor["city"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_city').text)
            self.assertEqual(doctor["email"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_email').text)
            self.assertEqual(doctor["phone"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_phone').text)

    def test_search_by_specialty(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        
        # Click on the specialties dropdown
        dropdown_specialties = driver.find_element(By.ID, 'dropdown_specialties')
        dropdown_specialties.click()
        # Click on the CARDIOLOGIA option
        option = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/ul/li[1]/span')
        option.click()
        # Click on the search button
        search_button = driver.find_element(By.ID, 'search')
        search_button.click()
        # Verify that the doctors are displayed correctly
        for doctor in self.expected_data["get"]:
            if "CARDIOLOGIA" in [e["name"] for e in doctor["specialties"]]:
                self.assertEqual(doctor["name"] + " " + doctor["lastname"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_name').text)
                self.assertEqual(doctor["city"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_city').text)
                self.assertEqual(doctor["email"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_email').text)
                self.assertEqual(doctor["phone"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_phone').text)

    def test_search_by_name(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        
        # Type "juan" in the search bar
        input_name = driver.find_element(By.ID, 'input_name')
        input_name.send_keys("juan")
        # Click on the search button
        search_button = driver.find_element(By.ID, 'search')
        search_button.click()
        # Verify that the doctors are displayed correctly
        for doctor in self.expected_data["get"]:
            if "juan" in doctor["name"].lower() or "juan" in doctor["lastname"].lower():
                self.assertEqual(doctor["name"] + " " + doctor["lastname"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_name').text)
                self.assertEqual(doctor["city"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_city').text)
                self.assertEqual(doctor["email"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_email').text)
                self.assertEqual(doctor["phone"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_phone').text)

    def test_search_by_city(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        
        # Type "santiago" in the search bar
        input_city = driver.find_element(By.ID, 'input_city')
        input_city.send_keys("santiago")
        # Click on the search button
        search_button = driver.find_element(By.ID, 'search')
        search_button.click()
        # Verify that the doctors are displayed correctly
        for doctor in self.expected_data["get"]:
            if "santiago" in doctor["city"].lower():
                self.assertEqual(doctor["name"] + " " + doctor["lastname"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_name').text)
                self.assertEqual(doctor["city"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_city').text)
                self.assertEqual(doctor["email"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_email').text)
                self.assertEqual(doctor["phone"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_phone').text)
    
    def test_search_by_name_and_city(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        
        # Type "juan" in the search bar
        input_name = driver.find_element(By.ID, 'input_name')
        input_name.send_keys("juan")
        # Type "santiago" in the search bar
        input_city = driver.find_element(By.ID, 'input_city')
        input_city.send_keys("santiago")
        # Click on the search button
        search_button = driver.find_element(By.ID, 'search')
        search_button.click()
        # Verify that the doctors are displayed correctly
        for doctor in self.expected_data["get"]:
            if ("juan" in doctor["name"].lower() or "juan" in doctor["lastname"].lower()) and "santiago" in doctor["city"].lower():
                self.assertEqual(doctor["name"] + " " + doctor["lastname"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_name').text)
                self.assertEqual(doctor["city"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_city').text)
                self.assertEqual(doctor["email"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_email').text)
                self.assertEqual(doctor["phone"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_phone').text)
        
    def test_search_by_specialty_and_city(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        
        # Click on the specialties dropdown
        dropdown_specialties = driver.find_element(By.ID, 'dropdown_specialties')
        dropdown_specialties.click()
        # Click on the CARDIOLOGIA option
        option = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/ul/li[1]/span')
        option.click()
        # Type "santiago" in the search bar
        input_city = driver.find_element(By.ID, 'input_city')
        input_city.send_keys("santiago")
        # Click on the search button
        search_button = driver.find_element(By.ID, 'search')
        search_button.click()
        # Verify that the doctors are displayed correctly
        for doctor in self.expected_data["get"]:
            if "CARDIOLOGIA" in [e["name"] for e in doctor["specialties"]] and "santiago" in doctor["city"].lower():
                self.assertEqual(doctor["name"] + " " + doctor["lastname"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_name').text)
                self.assertEqual(doctor["city"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_city').text)
                self.assertEqual(doctor["email"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_email').text)
                self.assertEqual(doctor["phone"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_phone').text)
    
    def test_search_by_specialty_and_name(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        
        # Click on the specialties dropdown
        dropdown_specialties = driver.find_element(By.ID, 'dropdown_specialties')
        dropdown_specialties.click()
        # Click on the CARDIOLOGIA option
        option = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/ul/li[1]/span')
        option.click()
        # Type "juan" in the search bar
        input_name = driver.find_element(By.ID, 'input_name')
        input_name.send_keys("juan")
        # Click on the search button
        search_button = driver.find_element(By.ID, 'search')
        search_button.click()
        # Verify that the doctors are displayed correctly
        for doctor in self.expected_data["get"]:
            if "CARDIOLOGIA" in [e["name"] for e in doctor["specialties"]] and ("juan" in doctor["name"].lower() or "juan" in doctor["lastname"].lower()):
                self.assertEqual(doctor["name"] + " " + doctor["lastname"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_name').text)
                self.assertEqual(doctor["city"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_city').text)
                self.assertEqual(doctor["email"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_email').text)
                self.assertEqual(doctor["phone"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_phone').text)
        
    def test_search_by_specialty_and_name_and_city(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        
        # Click on the specialties dropdown
        dropdown_specialties = driver.find_element(By.ID, 'dropdown_specialties')
        dropdown_specialties.click()
        # Click on the CARDIOLOGIA option
        option = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/ul/li[1]/span')
        option.click()
        # Type "juan" in the search bar
        input_name = driver.find_element(By.ID, 'input_name')
        input_name.send_keys("juan")
        # Type "santiago" in the search bar
        input_city = driver.find_element(By.ID, 'input_city')
        input_city.send_keys("santiago")
        # Click on the search button
        search_button = driver.find_element(By.ID, 'search')
        search_button.click()
        # Verify that the doctors are displayed correctly
        for doctor in self.expected_data["get"]:
            if "CARDIOLOGIA" in [e["name"] for e in doctor["specialties"]] and ("juan" in doctor["name"].lower() or "juan" in doctor["lastname"].lower()) and "santiago" in doctor["city"].lower():
                self.assertEqual(doctor["name"] + " " + doctor["lastname"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_name').text)
                self.assertEqual(doctor["city"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_city').text)
                self.assertEqual(doctor["email"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_email').text)
                self.assertEqual(doctor["phone"], driver.find_element(By.ID, 'r' + str(self.expected_data["get"].index(doctor) + 1) + '_phone').text)
    
    def tearDown(self):
        self.driver.close()

    


