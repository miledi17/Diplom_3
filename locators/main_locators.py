from selenium.webdriver.common.by import By


"""Локаторы для Проверка основного функционала"""
class MainLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]') #кнопка Конструктор
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text() = "Лента Заказов"]')  #кнопка Лента Заказов
    TITLE_ORDER_FEED = (By.XPATH, '//h1[text() = "Лента Заказов"]')  #Лента Заказов
    TITLE = (By.XPATH, '//h1[text() = "Соберите бургер"]') #Соберите бургер
    BUN = (By.XPATH, '//p[text() = "Флюоресцентная булка R2-D3"]')  #Флюоресцентная булка R2-D3
    BUN_INFO = (By.XPATH, '//h2[text() = "Детали ингредиента"]') #Детали Флюоресцентная булка R2-D3
    INGREDIENT_DETAILS = (By.XPATH, '//h2[text() = "Детали ингредиента"]')  #Детали ингредиента
    INGREDIENT_MODAL_CLOSED = (By.XPATH, '(//button[@type="button" and contains(@class, "Modal_modal__close_modified")])[1]')  # Крестик у всплывающего окна
    BURGER_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')  # Область для перетаскивания бургера
    COUNT_BUN = (By.XPATH, './/a[contains(@class, "BurgerIngredient_ingredient")]//p[contains(@class, "counter_counter__num")][1]') # Счётчик у булочки

    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text() = "Личный Кабинет"]')  # Личный кабинет
    PROFILE = (By.XPATH, '//a[text() = "Профиль"]')  # Профиль
    EMAIL = (By.XPATH, '//input[@name="name"]')  # поле ввода email
    PASSWORD = (By.XPATH, '//input[@name="Пароль"]')  #поле ввода password
    BUTTON_LOGIN = (By.XPATH, '//button[text() = "Войти"]') #кнопка Войти
    CREATE_ORDER = (By.XPATH, '//button[text() = "Оформить заказ"]') #Оформить заказ
    MSG_ORDER = (By.XPATH, '//p[text() = "Ваш заказ начали готовить"]') #Ваш заказ начали готовить