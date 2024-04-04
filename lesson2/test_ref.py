import time
from selenium.webdriver.common.by import By
from data import (LOGIN_POS, PASSWORD_POS,
                  MAIN_PAGE, PRODUCTS_PAGE, SAUCELABS_PAGE, ITEM_PAGE, CART_PAGE,
                  FIRST_NAME, LAST_NAME, POSTAL_CODE, ERROR_MESSAGE)
from locators import *


def test_auth_positive(driver, auth):
    """
    Авторизация, используя корректные данные (standard_user, secret_sauce)
    """
    assert driver.current_url == PRODUCTS_PAGE, "Url does not match expected"


def test_auth_negative_user(driver):
    """
    Авторизация с некорректным логином (user)
    """
    driver.get(MAIN_PAGE)
    driver.find_element(By.XPATH, USER_FIELD).send_keys("user")
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD_POS)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    assert driver.find_element(By.XPATH, ERROR_TEXT).text == ERROR_MESSAGE, \
        "Error text does not match expected"


def test_auth_negative_password(driver):
    """
    Авторизация с некорректным паролем (user)
    """
    driver.get(MAIN_PAGE)
    driver.find_element(By.XPATH, USER_FIELD).send_keys(LOGIN_POS)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys("user")
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    assert driver.find_element(By.XPATH, ERROR_TEXT).text == ERROR_MESSAGE, \
        "Error text does not match expected"


def test_add_product_to_cart_from_catalog(driver, auth, add_item_to_cart, delete_item_to_cart):
    """
    Добавление товара в корзину через каталог
    """
    assert driver.find_element(By.XPATH, COUNT_CART_TEXT).text == '1', \
        "Count of products does not correspond to added"


def test_remove_product_from_cart(driver, auth, add_item_to_cart):
    """
    Удаление товара из корзины через корзину
    """
    driver.find_element(By.XPATH, CART_BUTTON).click()
    driver.find_element(By.XPATH, REMOVE_BUTTON).click()

    assert driver.find_element(By.XPATH, REMOVE_DIV).is_enabled(), \
        "Product not removed from cart"


def test_add_product_to_cart_from_item(driver, auth, delete_item_to_cart):
    """
    Добавление товара в корзину из карточки товара
    """
    driver.find_element(By.XPATH, ITEM_NAME_LINK).click()
    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON_ITEM).click()
    driver.find_element(By.XPATH, CART_BUTTON).click()

    assert driver.find_element(By.XPATH, ITEM_NAME_LINK) is not None, \
        "Count of products does not correspond to added"


def test_removed_product_to_cart_from_item(driver, auth, add_item_to_cart):
    """
    Удаление товара из корзины через карточку товара
    """
    driver.get(f"{ITEM_PAGE}?id=4")
    driver.find_element(By.XPATH, REMOVE_BUTTON_ITEM).click()
    driver.find_element(By.XPATH, CART_BUTTON).click()

    assert not len(driver.find_elements(By.XPATH, ITEMS_TEXT)), \
        "Cart is not empty"


def test_move_to_card_by_click_on_image(driver, auth):
    """
    Успешный переход к карточке товара после клика на картинку товара
    """
    driver.find_element(By.XPATH, ITEM_IMG_LINK).click()
    test_label = driver.find_elements(By.XPATH, ITEMS_NAME)

    assert len(test_label) == 1, "Product card did not exist"


def test_move_to_card_by_click_on_title(driver, auth):
    """
    Успешный переход к карточке товара после клика на название товара
    """
    driver.find_element(By.XPATH, ITEM_NAME_LINK).click()

    assert driver.find_element(By.XPATH, ITEMS_NAME).text == "Sauce Labs Backpack", \
        "Product card did not exist"


def test_placing_an_order_positive(driver, auth, add_item_to_cart):
    """
    Оформление заказа с корректными данными
    """
    driver.get(CART_PAGE)
    driver.find_element(By.XPATH, CHECKOUT_BUTTON).click()
    driver.find_element(By.XPATH, FIRST_NAME_FIELD).send_keys(FIRST_NAME)
    driver.find_element(By.XPATH, LAST_NAME_FIELD).send_keys(LAST_NAME)
    driver.find_element(By.XPATH, ZIP_CODE_FIELD).send_keys(POSTAL_CODE)
    driver.find_element(By.XPATH, CONTINUE_BUTTON).click()
    driver.find_element(By.XPATH, FINISH_BUTTON).click()

    assert driver.find_element(By.XPATH, COMPLETE_TEXT).text == "Thank you for your order!", \
        'order has not been processed'


def test_check_filter_name_az(driver, auth):
    """
    Проверка работоспособности фильтра (A to Z)
    """
    driver.find_element(By.XPATH, FILTER_NAME_AZ).click()
    products_name = driver.find_elements(By.XPATH, ITEM_HEADINGS)
    list_products = [name.text for name in products_name]

    assert sorted(list_products) == list_products, "Filter from A to Z does not work"


def test_check_filter_name_za(driver, auth):
    """
    Проверка работоспособности фильтра (Z to A)
    """
    driver.find_element(By.XPATH, FILTER_NAME_ZA).click()
    products_name = driver.find_elements(By.XPATH, ITEM_HEADINGS)
    list_products = [name.text for name in products_name]

    assert sorted(list_products, reverse=True) == list_products, \
        "Filter from Z to A does not work"


def test_check_filter_price_lohi(driver, auth):
    """
    Проверка работоспособности фильтра (low to high)
    """
    driver.find_element(By.XPATH, FILTER_PRICE_LOHI).click()
    products_price = driver.find_elements(By.XPATH, PRICES)
    list_prices = [float(price.text[1:]) for price in products_price]

    assert sorted(list_prices) == list_prices, \
        "Filter from low to high does not work"


def test_check_filter_price_hilo(driver, auth):
    """
    Проверка работоспособности фильтра (high to low)
    """
    driver.find_element(By.XPATH, FILTER_PRICE_HILO).click()
    products_price = driver.find_elements(By.XPATH, PRICES)
    list_prices = [float(price.text[1:]) for price in products_price]

    assert sorted(list_prices, reverse=True) == list_prices, \
        "Filter from low to high does not work"


def test_menu_logout(driver, auth):
    """
    Проверка кнопки "Logout" в меню
    """
    driver.find_element(By.XPATH, MENU_BAR_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.XPATH, LOGOUT_LINK).click()

    assert driver.current_url == MAIN_PAGE, "Url does not match expected"


def test_menu_about(driver, auth):
    """
    Проверка кнопки "About" в меню
    """
    driver.find_element(By.XPATH, MENU_BAR_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.XPATH, ABOUT_LINK).click()

    assert driver.current_url == SAUCELABS_PAGE, "Url does not match expected"


def test_menu_reset(driver, auth):
    """
    Проверка кнопки "Reset App State" в меню
    """
    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON).click()
    driver.find_element(By.XPATH, MENU_BAR_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.XPATH, RESET_LINK).click()

    assert len(driver.find_elements(By.XPATH, COUNT_CART_TEXT)) == 0, \
        "Button 'Reset App State' does not work as expected"
