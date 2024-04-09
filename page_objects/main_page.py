from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://sbis.ru/"

    def open(self):
        self.driver.get(self.url)

    def go_to_contacts(self):
        contacts_link = self.driver.find_element(By.LINK_TEXT, "Контакты")
        contacts_link.click()

    # Другие методы для взаимодействия с элементами на главной странице могут быть добавлены здесь
