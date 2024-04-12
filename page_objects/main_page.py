from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://sbis.ru/"

    def open(self):
        self.driver.get(self.url)

    def go_to_contacts(self):
        contacts_link = self.driver.find_element(By.LINK_TEXT, "Контакты")
        contacts_link.click()

    def download_local_versions(self):
        download_link = self.driver.find_element(By.LINK_TEXT, "Скачать локальные версии")
        self.driver.execute_script("arguments[0].click();", download_link)
