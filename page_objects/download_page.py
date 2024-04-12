from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep


DOWNLOADED_FILE_PATH = os.path.expanduser("~/projects/tenzor_test_project/tenzor_test_project/tests/sabyapps-setup")

class DownloadPage:
    def __init__(self, driver):
        self.driver = driver

    def download_plugin(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-id="plugin"]')))
        sleep(1)
        plugin_link = self.driver.find_element(By.XPATH, '//div[@data-id="plugin"]')
        plugin_link.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-id="linux"]')))
        sleep(1)
        plugin_link = self.driver.find_element(By.XPATH, '//div[@data-id="linux"]')
        plugin_link.click()
        sleep(1)
        plugin_download_url = self.driver.find_element(By.XPATH, '//a[@href="https://update.sbis.ru/Sbis3Plugin/master/linux/sabyapps-setup"]')
        plugin_download_url.click()
        sleep(2)
    def check_dounload_file(self):
        assert os.path.exists(DOWNLOADED_FILE_PATH), "Файл не загружен"

    def check_size_file(self):
        expected_file_size = 22628
        downloaded_file_size = os.path.getsize(DOWNLOADED_FILE_PATH)
        assert downloaded_file_size == expected_file_size, "Размер скачанного файла не совпадает с ожидаемым"
