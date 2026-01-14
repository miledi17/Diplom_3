from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Ожидание прогрузки элемента
    def wait_visibility_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # Ожидание кликабельности элемента
    def wait_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    # Кликнуть на элемент
    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.click()

    # Ввести значение в поле ввода
    def enter_text(self, locator, text):
        element = self.wait_visibility_element(locator)
        element.send_keys(text)

    # Получить текст на элементе
    def get_text_element(self, locator):
        element = self.wait_visibility_element(locator)
        return element.text

    # Получить URL
    def get_url(self):
        return self.driver.current_url

    # Проверить отображение элемента
    def displaying_element(self, locator):
        return self.wait_visibility_element(locator).is_displayed()

    # Поиск элемента
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    # драг анд дроп
    def drag_and_drop_element(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    # Ждём, пока элемент перестанет быть видимым
    def wait_until_element_invisible(self, locator, timeout=100):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))