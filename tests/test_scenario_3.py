import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page_objects import MainPage


@pytest.fixture
def browser():
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service)
    yield driver
    driver.quit()

def test_scenario_3(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.download_local_vesions()
    main_page.download_plagin('Ubuntu')
    main_page.check_dounload_file()
    main_page.check_size_file()