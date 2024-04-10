from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver
from page_objects import MainPage, ContactsPage


@pytest.fixture
def browser():
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

def test_scenario_1(browser):
    main_page = MainPage(browser)
    main_page.go_to_contacts()

    contacts_page = ContactsPage(browser)
    contacts_page.find_tensor_banner()
    contacts_page.verify_tensor_block()
    contacts_page.go_to_details()
    contacts_page.verify_tensor_url()
    contacts_page.verify_photo_dimensions()
