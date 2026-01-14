from selenium.webdriver.common.by import By


"""Локаторы для раздела 'Лента заказов'"""
class OrderFeedLocators:
    ORDER_FEED = (By.XPATH, '(//ul[contains(@class,"OrderFeed_list")]/*)[1]') #Заказ из списка
    ORDER_INFO = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]') #Окно заказа
    MODAL_GET_ORDER = (By.XPATH, ".//p[text()= 'Ваш заказ начали готовить']")
    ORDER_EXIT_BUTTON = (By.XPATH, "(//button[contains(@type,'button')])[1]") #Кнопка закрытия оформления заказа
    CREATE_ORDER = (By.XPATH, '//button[text() = "Оформить заказ"]') #Оформить заказ
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')  #кнопка Конструктор
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text() = "Лента Заказов"]')  #кнопка Лента Заказов
    BUTTON_ORDER_HISTORY = (By.XPATH, '//a[text() = "История заказов"]')  # История заказов
    BUN = (By.XPATH, '//p[text() = "Флюоресцентная булка R2-D3"]')  #Флюоресцентная булка R2-D3
    BURGER_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')  # Область для перетаскивания бургера
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text() = "Личный Кабинет"]')  # Личный кабинет
    EMAIL = (By.XPATH, '//input[@name="name"]')  #поле ввода email
    PASSWORD = (By.XPATH, '//input[@name="Пароль"]')  #поле ввода password
    BUTTON_LOGIN = (By.XPATH, '//button[text() = "Войти"]') #кнопка Войти
    HISTORY_ORDER = (By.XPATH, '//a[text() = "История заказов"]')  #История заказов
    ORDER_NUMBER_HISTORY = (By.XPATH, '//p[@class="text text_type_digits-default"]') #Номер заказа в Истории заказов
    ORDER_NUMBER_FEED = (By.XPATH, '(//p[@class="text text_type_digits-default"])[1]') #Номер заказа в Ленте заказов
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow' )]")  # Номер заказа в окне после оформления
    ORDER_NUMBER_WORK = (By.XPATH, "//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]")  # Номер заказа в работе
    ORDER_ALL_TIME = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]') #Выполнено за все время
    ORDER_TODAY = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]') #Выполнено за сегодня
    INCORRECT_NUMBER = (By.XPATH, "//h2[contains(.,'9999')]")