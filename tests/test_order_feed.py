from pages.order_feed_page import OrderFeedPage
from conftest import driver
import allure


@allure.feature('Проверка раздела "Лента заказов"')
class TestOrderFeed:
    @allure.title('Проверка, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_info(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.click_button_order_feed()
        order_feed.click_order()

        assert order_feed.check_displaying_order_info()

    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_feed_order_history_order(self, driver, create_user):
        order_feed = OrderFeedPage(driver)
        order_feed.login_to_account(create_user)
        order_feed.wait_bun()
        order_feed.drag_and_drop_ingredient_to_burger_area()
        order_feed.click_create_order()
        order_feed.wait_until_text_visible()
        order_feed.incorrect_number_invisible()
        order_feed.click_order_exit_button()
        order_feed.click_button_personal_account()
        order_feed.click_history_order()
        order_number_history = order_feed.text_history_order_number()
        order_feed.click_button_order_feed()
        order_number_feed = order_feed.text_feed_order_number()
        assert order_number_feed in order_number_history


    allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_feed_order_total_counter(self, driver, create_user):
        order_feed = OrderFeedPage(driver)
        order_feed.login_to_account(create_user)
        order_feed.click_button_order_feed()
        order_all_time = int(order_feed.text_order_all_time())
        order_feed.click_constructor()
        order_feed.wait_bun()
        order_feed.drag_and_drop_ingredient_to_burger_area()
        order_feed.click_create_order()
        order_feed.wait_until_text_visible()
        order_feed.incorrect_number_invisible()
        order_feed.click_order_exit_button()
        order_feed.click_button_order_feed()

        assert order_all_time + 1 == int(order_feed.text_order_all_time())

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_feed_order_today_counter(self, driver, create_user):
        order_feed = OrderFeedPage(driver)
        order_feed.login_to_account(create_user)
        order_feed.click_button_order_feed()
        order_today_time = int(order_feed.text_order_today())
        order_feed.click_constructor()
        order_feed.wait_bun()
        order_feed.drag_and_drop_ingredient_to_burger_area()
        order_feed.click_create_order()
        order_feed.wait_until_text_visible()
        order_feed.incorrect_number_invisible()
        order_feed.click_order_exit_button()
        order_feed.click_button_order_feed()

        assert order_today_time + 1 == int(order_feed.text_order_today())

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_new_orders_are_in_progress(self, driver, create_user):
        order_feed = OrderFeedPage(driver)
        order_feed.login_to_account(create_user)
        order_feed.wait_bun()
        order_feed.drag_and_drop_ingredient_to_burger_area()
        order_feed.click_create_order()
        order_feed.wait_until_text_visible()
        order_feed.incorrect_number_invisible()
        order_number = order_feed.text_order_number()
        order_feed.click_order_exit_button()
        order_feed.click_button_order_feed()
        order_number_work = order_feed.text_order_number_work()

        assert order_number in order_number_work