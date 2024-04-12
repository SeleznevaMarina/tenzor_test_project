import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page_objects import MainPage, DownloadPage
from selenium.webdriver.chrome.options import Options
import os

# Указываем путь к папке загрузки
download_path = os.path.expanduser("~/projects/tenzor_test_project/tenzor_test_project/tests")

# Создаем объект опций для Chrome
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': download_path,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

@pytest.fixture
def browser():
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield driver
    driver.quit()

def test_scenario_3(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.download_local_versions()
    download_page = DownloadPage(browser)
    download_page.download_plugin()
    download_page.check_dounload_file()
    download_page.check_size_file()