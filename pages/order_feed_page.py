from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
import allure



class OrderFeedPage(BasePage):
    @allure.step('Вход в аккаунт')
    def login_to_account(self, create_user):
        user_data, _, _ = create_user
        email = user_data["email"]
        password = user_data["password"]

        self.wait_visibility_element(OrderFeedLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_element(OrderFeedLocators.BUTTON_PERSONAL_ACCOUNT)
        self.enter_text(OrderFeedLocators.EMAIL, email)
        self.enter_text(OrderFeedLocators.PASSWORD, password)
        self.click_element(OrderFeedLocators.BUTTON_LOGIN)

    @allure.step('Клик по кнопке «Лента заказов»')
    def click_button_order_feed(self):
        self.wait_visibility_element(OrderFeedLocators.ORDER_FEED_BUTTON)
        self.click_element(OrderFeedLocators.ORDER_FEED_BUTTON)
        
    @allure.step('Клик по заказу')
    def click_order(self):
        self.wait_visibility_element(OrderFeedLocators.ORDER_FEED)
        self.click_element(OrderFeedLocators.ORDER_FEED)
       
    @allure.step('Проверить наличие на странице окна заказа')
    def check_displaying_order_info(self):
        return self.displaying_element(OrderFeedLocators.ORDER_INFO)

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_ingredient_to_burger_area(self):
        source_element = self.find_element(OrderFeedLocators.BUN)
        target_element = self.find_element(OrderFeedLocators.BURGER_AREA)
        self.drag_and_drop_element(source_element, target_element)
        
    @allure.step('Ожидание булочки')
    def wait_bun(self):
        self.wait_clickable_element(OrderFeedLocators.BUN)
       
    @allure.step('Оформить заказ')
    def click_create_order(self):
        self.click_element(OrderFeedLocators.CREATE_ORDER)
       
    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_button_personal_account(self):
        self.wait_clickable_element(OrderFeedLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_element(OrderFeedLocators.BUTTON_PERSONAL_ACCOUNT)
        
    @allure.step('Клик кнопки «История заказов»')
    def click_history_order(self):
        self.wait_clickable_element(OrderFeedLocators.BUTTON_ORDER_HISTORY)
        self.click_element(OrderFeedLocators.BUTTON_ORDER_HISTORY)
        
    @allure.step('Закрытия окна с заказом')
    def click_order_exit_button(self):
        self.wait_clickable_element(OrderFeedLocators.ORDER_EXIT_BUTTON)
        self.click_element(OrderFeedLocators.ORDER_EXIT_BUTTON)
        
    @allure.step('Получить номер заказа из истории')
    def text_history_order_number(self):
        self.wait_clickable_element(OrderFeedLocators.ORDER_NUMBER_HISTORY)
        return self.get_text_element(OrderFeedLocators.ORDER_NUMBER_HISTORY)

    @allure.step('Получить номер заказа из ленты заказов')
    def text_feed_order_number(self):
        self.wait_clickable_element(OrderFeedLocators.ORDER_NUMBER_FEED)
        return self.get_text_element(OrderFeedLocators.ORDER_NUMBER_FEED)

    @allure.step('Получить количество заказов за всё время')
    def text_order_all_time(self):
        self.wait_clickable_element(OrderFeedLocators.ORDER_ALL_TIME)
        return self.get_text_element(OrderFeedLocators.ORDER_ALL_TIME)

    @allure.step('Получить количество заказов за сегодня')
    def text_order_today(self):
        self.wait_clickable_element(OrderFeedLocators.ORDER_TODAY)
        return self.get_text_element(OrderFeedLocators.ORDER_TODAY)


    @allure.step('Клик по Конструктор')
    def click_constructor(self):
        self.wait_clickable_element(OrderFeedLocators.CONSTRUCTOR_BUTTON)
        self.click_element(OrderFeedLocators.CONSTRUCTOR_BUTTON)
        
    @allure.step('Получить номер заказа после оформления')
    def text_order_number(self):
        self.wait_visibility_element(OrderFeedLocators.ORDER_NUMBER)
        return self.get_text_element(OrderFeedLocators.ORDER_NUMBER)

    @allure.step('Получить номер заказа в работе')
    def text_order_number_work(self):
        self.wait_clickable_element(OrderFeedLocators.ORDER_NUMBER_WORK)
        return self.get_text_element(OrderFeedLocators.ORDER_NUMBER_WORK)

    @allure.step("Убеждаемся, что номер заказа не 9999")
    def incorrect_number_invisible(self):
        self.wait_until_element_invisible(OrderFeedLocators.INCORRECT_NUMBER)

    @allure.step("Ожидаем видимости текста в модальном окне")
    def wait_until_text_visible(self):
        self.wait_visibility_element(OrderFeedLocators.MODAL_GET_ORDER)