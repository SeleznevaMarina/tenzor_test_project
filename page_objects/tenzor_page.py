from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TenzorPage:
    def __init__(self, driver):
        window_handles = driver.window_handles
        new_window = window_handles[-1]
        driver.switch_to.window(new_window)
        self.driver = driver

    def verify_tensor_block(self):
        tensor_block = self.driver.find_element(By.XPATH, "//p[text()='Сила в людях']")
        assert tensor_block.is_displayed(), "Тензор блок не найден на странице"

    def go_to_details(self):
        details_link = self.driver.find_element(By.XPATH, "//a[@href='/about']")
        details_link.click()

    def verify_tensor_url(self):
        current_url = self.driver.current_url
        assert current_url == "https://tensor.ru/about", "URL не соответствует ожидаемому"

    def verify_photo_dimensions(self):
        photos = self.driver.find_elements(By.XPATH, "//div[@class='tensor_ru-About__block3-image-filter']//img")
        for photo in photos:
            assert photo.size['height'] == 192, "Высота фотографии не соответствует ожидаемой"
            assert photo.size['width'] == 272, "Ширина фотографии не соответствует ожидаемой"

