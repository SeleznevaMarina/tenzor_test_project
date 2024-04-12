from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactsPage:
    def __init__(self, driver):
        self.driver = driver

    def find_tensor_banner(self):
        tensor_banner = self.driver.find_element(By.XPATH, "//img[@alt='Разработчик системы СБИС — компания «Тензор»']")
        tensor_banner.click()

    def check_region_and_partners(self):
        params = {
            "latitude": 56.228895,
            "longitude": 41.299621,
            "accuracy": 100
            }

        self.driver.execute_cdp_cmd("Page.setGeolocationOverride", params)
        self.driver.get('https://sbis.ru/contacts/')
        location = self.driver.find_element(By.XPATH, "//span[text()='Владимирская обл.']")
        partners = self.driver.find_element(By.XPATH, '//div[@class="sbisru-Contacts-List__item sbisru-text--standart sbisru-Contacts__text--500 pv-8 pv-xm-16 pl-24 pr-12 ph-xm-12 mb-xm-8 ws-flexbox ws-justify-content-between ws-align-items-start"]')
        partner_1 = self.driver.find_element(By.XPATH, '//div[text()="СБИС - Владимир"]')
        assert location.is_displayed(), "Локация не определилась"
        assert partners.is_displayed(), "Партнеры не определились"
        assert partner_1.is_displayed(), "Первый партнер не тот"

    def change_region(self, region):
        current_region = self.driver.find_element(By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
        current_region.click()
        wait = WebDriverWait(self.driver, 10)
        modal_window = wait.until(EC.visibility_of_element_located((By.ID, "popup")))
        new_region = self.driver.find_element(By.XPATH, f"//span[@title='{region}']")
        new_region.click()

    def verify_region_change(self, region):
        wait = WebDriverWait(self.driver, 10)
        location = wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[text()='{region}']")))
        partners = self.driver.find_element(By.XPATH, '//div[@class="sbisru-Contacts-List__item sbisru-text--standart sbisru-Contacts__text--500 pv-8 pv-xm-16 pl-24 pr-12 ph-xm-12 mb-xm-8 ws-flexbox ws-justify-content-between ws-align-items-start"]')
        partner_1 = self.driver.find_element(By.XPATH, '//div[text()="Петропавловск-Камчатский"]')
        current_url = self.driver.current_url
        current_title = self.driver.find_element(By.CLASS_NAME, "state-1").get_attribute('innerText')
        assert location.is_displayed(), "Локация не определилась"
        assert partners.is_displayed(), "Партнеры не определились"
        assert partner_1.is_displayed(), "Первый партнер не тот"
        assert current_url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients', "URL не соответствует ожидаемому"
        assert current_title == 'СБИС Контакты — Камчатский край'
