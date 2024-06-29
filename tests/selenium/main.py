from selenium import webdriver
import search_doctor

search_doctor_tests = [
    search_doctor.test_list_doctors
]

results = []

def run_tests():
    for test in search_doctor_tests:
        result = test()
        results.append(result)
    
if __name__ == "__main__":
    run_tests()
    print("Pass:", results.count(True))
    print("Fail:", results.count(False))

