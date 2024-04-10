from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page_objects import MainPage, ContactsPage, TenzorPage


@pytest.fixture
def browser():
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service)
    yield driver
    driver.quit()

def test_scenario_1(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.go_to_contacts()

    contacts_page = ContactsPage(browser)
    contacts_page.find_tensor_banner()
    tenzor_page = TenzorPage(browser)
    tenzor_page.verify_tensor_block()
    tenzor_page.go_to_details()
    tenzor_page.verify_tensor_url()
    tenzor_page.verify_photo_dimensions()
