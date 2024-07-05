import unittest
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import os

class UploadDeleteImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.image_path = os.path.abspath("selenium_tests/data/profile-picture.jpg")

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)

    def tearDown(self):
        self.driver.close()

    def test_1_upload_image(self):
        driver = self.driver
        driver.get("http://localhost:3000/medics/1")

        # Select 'Cambiar foto' button
        select_button1 = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Cambiar foto']")
        select_button1.click()

        # Select 'Seleccionar' button 
        select_button2 = driver.find_element(By.CSS_SELECTOR, "span[class='p-button p-fileupload-choose p-component'] input")
        select_button2.send_keys(self.image_path)

        # Delay to upload the image
        time.sleep(1)

        # Send image
        select_button3 = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Subir']")
        select_button3.click()

        # Delay to upload the image to Cloudinary
        time.sleep(5)

        # Verify if the image was uploaded
        image_url = driver.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
        self.assertRegex(image_url, "cloudinary")

    def test_2_delete_image(self):
        driver = self.driver
        driver.get("http://localhost:3000/medics/1")

        # Delay to load the image
        time.sleep(3)

        # Select 'Eliminar foto' button
        select_button1 = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Eliminar foto']")
        select_button1.click()

        # Select 'Eliminar' button
        select_button2 = driver.find_element(By.CSS_SELECTOR, "button[class='p-confirm-dialog-accept p-button p-component']")
        select_button2.click()

        # Delay to delete the image
        time.sleep(3)

        # Verify if the image was deleted
        image_url = driver.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
        self.assertRegex(image_url, "empty_profile")