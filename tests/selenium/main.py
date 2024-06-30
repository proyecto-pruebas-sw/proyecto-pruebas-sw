import unittest
from search_doctor import DoctorSearch
from list_specialty import SpecialtyList
from create_specialty import SpecialtyCreate

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    
    # Order of the execution
    suite.addTests(loader.loadTestsFromTestCase(DoctorSearch))
    suite.addTests(loader.loadTestsFromTestCase(SpecialtyList))
    suite.addTests(loader.loadTestsFromTestCase(SpecialtyCreate))

    runner = unittest.TextTestRunner()
    runner.run(suite)