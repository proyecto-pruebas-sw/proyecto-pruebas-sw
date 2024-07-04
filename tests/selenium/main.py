import unittest
from search_doctor import DoctorSearch
from list_specialty import SpecialtyList
from create_specialty import SpecialtyCreate
from create_doctor import DoctorCreate
from edit_doctor_personal import EditPersonalInfo
from upload_delete_image import UploadDeleteImage
from create_academic_info import CreateAcademicInfo
from detail_doctor import DetailDoctor

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    
    # Order of the execution
    suite.addTests(loader.loadTestsFromTestCase(DoctorSearch))
    suite.addTests(loader.loadTestsFromTestCase(SpecialtyList))
    suite.addTests(loader.loadTestsFromTestCase(SpecialtyCreate))
    suite.addTests(loader.loadTestsFromTestCase(DoctorCreate))
    suite.addTests(loader.loadTestsFromTestCase(EditPersonalInfo))
    suite.addTests(loader.loadTestsFromTestCase(UploadDeleteImage))
    suite.addTests(loader.loadTestsFromTestCase(CreateAcademicInfo))
    suite.addTests(loader.loadTestsFromTestCase(DetailDoctor))

    runner = unittest.TextTestRunner()
    runner.run(suite)