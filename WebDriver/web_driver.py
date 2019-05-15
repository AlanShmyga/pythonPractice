from pytest import fixture
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_some(driver):
    driver.get("http://www.google.com")
    driver.find_element_by_name("q").send_keys("some shit")
    driver.find_element_by_name("q").send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "hdtbSum")))
