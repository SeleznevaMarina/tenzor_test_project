from selenium.webdriver.common.by import By

class ContactsPage:
    def __init__(self, driver):
        self.driver = driver

    def find_tensor_banner(self):
        tensor_banner = self.driver.find_element(By.XPATH, "//img[@alt='Тензор']")
        tensor_banner.click()

    def verify_tensor_block(self):
        tensor_block = self.driver.find_element(By.XPATH, "//div[@id='tensor-block']")
        assert tensor_block.is_displayed(), "Тензор блок не найден на странице"

    def go_to_details(self):
        details_link = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Подробнее')]")
        details_link.click()

    def verify_tensor_url(self):
        current_url = self.driver.current_url
        assert current_url == "https://tenzor.ru/about/", "URL не соответствует ожидаемому"

    def verify_photo_dimensions(self):
        photos = self.driver.find_elements(By.XPATH, "//div[@class='timeline']//img")
        for photo in photos:
            assert photo.size['height'] == 100, "Высота фотографии не соответствует ожидаемой"
            assert photo.size['width'] == 100, "Ширина фотографии не соответствует ожидаемой"

    def check_region_and_partners(self):
        # Реализация проверки региона и списка партнеров
        pass

    def change_region(self, region):
        # Реализация изменения региона
        pass

    def verify_region_change(self, region):
        # Реализация проверки изменения региона
        pass
