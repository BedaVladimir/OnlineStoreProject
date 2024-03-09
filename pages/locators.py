from selenium.webdriver.common.by import By


class AuthPageLocators:
    """Локаторы элементов на странице авторизации"""
    LOGIN_INPUT = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    ERROR_MSG_CONTAINER = (By.XPATH, "//div[@class='error-message-container error']")
    ERROR_MESSAGE = (By.XPATH, "//div/h3[@data-test='error']")


class ProductsPageLocators:
    """Локаторы элементов на странице выбора товаров"""
    PAGE_TITLE = (By.XPATH, "//span[@class='title']")
    SORT_SELECTOR = (By.XPATH, "//select[@class='product_sort_container']")
    SHOPPING_CART_LINK = (By.XPATH, "//a[@class='shopping_cart_link']")
    PRODUCT_COUNT = (By.XPATH, "//span[@class='shopping_cart_badge']")  # счетчик кол-ва товаров в корзине
    # локаторы элементов карточки товара
    CARD_PRODUCT = (By.XPATH, "//div[@class='inventory_item']")  # карточка товара
    PRODUCT_PICTURE = (By.XPATH, "//img[@class='inventory_item_img']")  # картинка с изображением товара
    PRODUCT_NAME = (By.XPATH, "//div[@class='inventory_item_name ']")
    PRODUCT_DESCRIPTION = (By.XPATH, "//div[@class='inventory_item_desc']")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")
    REMOVE_BTN = (By.XPATH, "//button[@class='btn btn_secondary btn_small btn_inventory ']")


class CartPageLocators:
    """Локаторы элементов на странице корзины"""
    CART_TITLE = (By.XPATH, "//span[@class='title']")
    CART_ITEM = (By.XPATH, "//div[@class='cart_item']")
    NAME_PRODUCT_IN_CART = (By.XPATH, "//div[@class='inventory_item_name']")
    DESC_PRODUCT_IN_CART = (By.XPATH, "//div[@class='inventory_item_desc']")
    PRICE_PRODUCT_IN_CART = (By.XPATH, "//div[@class='inventory_item_price']")
    REMOVE_BTN_IN_CART = (By.XPATH, "//button[@class='btn btn_secondary btn_small cart_button']")
    CONTINUE_SHOP_BTN = (By.XPATH, "//button[@id='continue-shopping']")
    CHECKOUT_BTN = (By.XPATH, "//button[@id='checkout']")


class UserInfoLocators:
    """Страница с вводом информации пользователя (инфо для отправки товара)"""
    USER_INFO_TITLE = (By.XPATH, "//div/span[@class='title']")
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    ZIP_CODE = (By.XPATH, "//input[@id='postal-code']")
    CANCEL_BTN = (By.XPATH, "//button[@id='cancel']")
    CONTINUE_BTN = (By.XPATH, "//input[@id='continue']")
    ERROR_MSG_ELEMENT = (By.XPATH, "//div[@class='error-message-container error']")
    ERROR_MSG_TEXT = (By.XPATH, "//div/h3[@data-test='error']")


class CheckoutPageLocators:
    """Страница подтверждения заказа"""
    #  Возможно, надо унаследовать от другого класса, чтобы не прописывать по новой локаторы