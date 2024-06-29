from selenium import webdriver

def test_list_doctors():
    print("selenium-1 test_list_doctors()")

    driver = webdriver.Firefox()
    driver.get("http://localhost:3000")
    try:
        assert "Vite + React" in driver.title
        print("Pass")
        return True
    except AssertionError:
        print("Fail: Title does not match")
        return False
    finally:
        driver.quit()
        print()
    


