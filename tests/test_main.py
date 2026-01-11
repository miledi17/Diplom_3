from pages.main_page import MainPage
from conftest import driver
import allure
from urls import Urls


@allure.feature('Проверка основного функционала')
class TestMain:
    @allure.title('Переход по клику на "Конструктор"')
    def test_click_constructor(self, driver):
        main = MainPage(driver)
        main.click_button_constructor()

        assert main.check_url() == Urls.BASE_URL

    @allure.title('Переход по клику на "Лента заказов"')
    def test_click_order_feed(self, driver):
        main = MainPage(driver)
        main.click_button_order_feed()

        assert main.check_url() == Urls.ORDER_FEED

    @allure.title('При клике на ингредиент, появляется всплывающее окно с деталями')
    def test_click_ingredient(self, driver):
        main = MainPage(driver)
        main.click_ingredient()

        assert main.check_ingredient_info()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_ingredient_closed(self, driver):
        main = MainPage(driver)
        main.click_ingredient()
        main.click_close()

        assert main.check_closed()

    @allure.title('При добавлении ингредиента в заказ, увеличивается счетчик данного ингредиента')
    def test_counter_ingredient(self, driver):
        main = MainPage(driver)
        main.wait_bun()
        main.drag_and_drop_ingredient_to_burger_area()

        assert main.get_count_ingredients() == '2'


    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorized_user_order(self, driver, create_user):
        main = MainPage(driver)
        main.login_to_account(create_user)
        main.wait_bun()
        main.drag_and_drop_ingredient_to_burger_area()
        main.click_order()

        assert main.check_order()