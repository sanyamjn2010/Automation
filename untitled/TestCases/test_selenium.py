from threading import Thread

import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope="module")
def set_path():
    path="chromedriver.exe"
    global driver
    driver=Chrome(executable_path=path)

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_record1(set_path):
    driver.get("https:\\google.com")
    driver.maximize_window()
    driver.implicitly_wait(5000)
    driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("sanyam jain facebook")
    btn=driver.find_elements_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")[0]
    btn.click()

@pytest.mark.Regression
def test_record2(set_path):
    driver.get("https:\\google.com")
    driver.maximize_window()
    driver.implicitly_wait(5000)
    driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(
        "sanyam jain facebook")
    btn = driver.find_elements_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")[0]
    btn.click()

@pytest.mark.Regression
def test_record3(set_path):
    driver.get("https:\\google.com")
    driver.maximize_window()
    driver.implicitly_wait(5000)
    driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(
        "sanyam jain facebook")
    btn = driver.find_elements_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")[0]
    btn.click()
