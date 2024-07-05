import unittest
from selenium_tests.search_doctor import DoctorSearch
from selenium_tests.list_specialty import SpecialtyList
from selenium_tests.create_specialty import SpecialtyCreate
from selenium_tests.create_doctor import DoctorCreate
#from selenium_tests.remove_doctor import DoctorRemove
#from selenium_tests.create_job_info import CreateJobInfo
#from selenium_tests.edit_doctor_personal import EditPersonalInfo
from selenium_tests.upload_delete_image import UploadDeleteImage
#from selenium_tests.create_academic_info import CreateAcademicInfo
from selenium_tests.detail_doctor import DetailDoctor

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    
    # Order of the execution
    suite.addTests(loader.loadTestsFromTestCase(DoctorSearch))
    suite.addTests(loader.loadTestsFromTestCase(SpecialtyList))
    suite.addTests(loader.loadTestsFromTestCase(SpecialtyCreate))
    suite.addTests(loader.loadTestsFromTestCase(DoctorCreate))

    #suite.addTests(loader.loadTestsFromTestCase(CreateJobInfo))
    #suite.addTests(loader.loadTestsFromTestCase(EditPersonalInfo))
    
    suite.addTests(loader.loadTestsFromTestCase(UploadDeleteImage))
    
    #suite.addTests(loader.loadTestsFromTestCase(CreateAcademicInfo))
    
    suite.addTests(loader.loadTestsFromTestCase(DetailDoctor))
    
    #suite.addTests(loader.loadTestsFromTestCase(DoctorRemove))

    runner = unittest.TextTestRunner()
    runner.run(suite)