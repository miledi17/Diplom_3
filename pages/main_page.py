from pages.base_page import BasePage
from locators.main_locators import MainLocators
import allure



class MainPage(BasePage):
    @allure.step('Вход в аккаунт')
    def login_to_account(self, create_user):
        user_data, _, _ = create_user
        email = user_data["email"]
        password = user_data["password"]

        self.wait_visibility_element(MainLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_element(MainLocators.BUTTON_PERSONAL_ACCOUNT)
        self.enter_text(MainLocators.EMAIL, email)
        self.enter_text(MainLocators.PASSWORD, password)
        self.click_element(MainLocators.BUTTON_LOGIN)
        

    @allure.step('Клик по кнопке «Конструктор»')
    def click_button_constructor(self):
        self.wait_visibility_element(MainLocators.CONSTRUCTOR_BUTTON)
        self.click_element(MainLocators.CONSTRUCTOR_BUTTON)
        

    @allure.step('Клик по кнопке «Лента заказов»')
    def click_button_order_feed(self):
        self.click_element(MainLocators.ORDER_FEED_BUTTON)
       
    @allure.step('Проверить наличие на странице заголовка «Лента заказов»')
    def check_displaying_title_feed_order(self):
        return self.displaying_element(MainLocators.TITLE_ORDER_FEED)

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.click_element(MainLocators.BUN)
       

    @allure.step('Открытие карточки ингредиента')
    def check_ingredient_info(self):
        return self.displaying_element(MainLocators.BUN_INFO)

    @allure.step('Клик по крестику')
    def click_close(self):
        self.wait_clickable_element(MainLocators.INGREDIENT_MODAL_CLOSED)
        self.click_element(MainLocators.INGREDIENT_MODAL_CLOSED)
       
    @allure.step('Проверить закрытие модального окна')
    def check_closed(self):
        return self.displaying_element(MainLocators.TITLE)

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_ingredient_to_burger_area(self):
        source_element = self.find_element(MainLocators.BUN)
        target_element = self.find_element(MainLocators.BURGER_AREA)

        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получить количество ингредиентов')
    def get_count_ingredients(self):
        return self.get_text_element(MainLocators.COUNT_BUN)

    @allure.step('Ожидание булочки')
    def wait_bun(self):
        self.wait_clickable_element(MainLocators.BUN)

    @allure.step('Оформить заказ')
    def click_order(self):
        self.click_element(MainLocators.CREATE_ORDER)
       
    @allure.step('Проверить появление окна заказа')
    def check_order(self):
        return self.displaying_element(MainLocators.MSG_ORDER)

    @allure.step('Получить ссылку текущей страницы')
    def check_url(self):
        return self.get_url()