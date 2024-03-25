import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.saucedemo.com/'
ENDPOINT_PRODUCTS = 'inventory.html'
ENDPOINT_CART = 'cart.html'


def test_auth_positive():
    """
    Авторизация, используя корректные данные (standard_user, secret_sauce)
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    assert driver.current_url == URL + ENDPOINT_PRODUCTS, 'url does not match expected'
    driver.quit()


def test_auth_negative():
    """
    Авторизация используя некорректные данные (user, user)
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    error_message = 'Epic sadface: Username and password do not match any user in this service'
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("user")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    text_error = driver.find_element(By.XPATH, '//h3[contains(text(), "Username and password do not match")]')

    assert text_error.text == error_message, 'error text does not match expected'
    driver.quit()


def test_add_product_to_cart_from_catalog():
    """
    Добавление товара в корзину через каталог
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
    count_products_cart = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')

    assert count_products_cart.text == '1', 'count of products does not correspond to added'
    driver.quit()


def test_remove_product_from_cart():
    """
    Удаление товара из корзины через корзину
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-backpack"]').click()
    removed_product = driver.find_element(By.XPATH, '//div[@class="removed_cart_item"]')

    assert removed_product.is_enabled(), 'product not removed from cart'
    driver.quit()


def test_add_product_to_cart_from_item():
    """
    Добавление товара в корзину из карточки товара
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]').click()
    driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    product = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
    assert product is not None, \
        'count of products does not correspond to added'
    driver.quit()


def test_removed_product_to_cart_from_item():
    """
    Удаление товара из корзины через карточку товара
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]').click()
    driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    assert not len(driver.find_elements(By.XPATH, '//div[@class="cart_item"]')), 'cart is not empty'
    driver.quit()


def test_move_to_card_by_click_on_image():
    """
    Успешный переход к карточке товара после клика на картинку товара
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//a[@id="item_4_img_link"]').click()
    test_label = driver.find_element(By.XPATH, '//div[contains(text(),"Sauce Labs")]')

    assert test_label.text == 'Sauce Labs Backpack', 'product card did not exist'
    driver.quit()


def test_move_to_card_by_click_on_title():
    """
    Успешный переход к карточке товара после клика на название товара
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]').click()
    test_label = driver.find_element(By.XPATH, '//div[contains(text(),"Sauce Labs")]')

    assert test_label.text == 'Sauce Labs Backpack', 'product card did not exist'
    driver.quit()


def test_placing_an_order_positive():
    """
    Оформление заказа используя корректные данные
    """
    first_name = "Ivan"
    last_name = "Ivanov"
    postal_code = "300000"
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    driver.find_element(By.XPATH, '//button[@id="checkout"]').click()
    driver.find_element(By.XPATH, '//input[@id="first-name"]').send_keys(first_name)
    driver.find_element(By.XPATH, '//input[@id="last-name"]').send_keys(last_name)
    driver.find_element(By.XPATH, '//input[@id="postal-code"]').send_keys(postal_code)
    driver.find_element(By.XPATH, '//input[@id="continue"]').click()
    driver.find_element(By.XPATH, '//button[@id="finish"]').click()

    assert driver.find_element(By.XPATH, '//h2[@class="complete-header"]').text == "Thank you for your order!", \
        'order has not been processed'
    driver.quit()


def test_check_filter_az():
    """
    Проверка работоспособности фильтра (A to Z)
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//select/option[@value="az"]').click()
    products_name = driver.find_elements(By.XPATH, '//div[@class="inventory_item_description"]//a//div')
    list_products = [name.text for name in products_name]
    list_products_sort = sorted(list_products)
    assert list_products_sort == list_products, 'filter from A to Z does not work'
    driver.quit()


def test_check_filter_za():
    """
    Проверка работоспособности фильтра (Z to A)
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//select/option[@value="za"]').click()
    products_name = driver.find_elements(By.XPATH, '//div[@class="inventory_item_description"]//a//div')
    list_products = [name.text for name in products_name]
    list_products_sort = sorted(list_products, reverse=True)
    assert list_products_sort == list_products, 'filter from Z to A does not work'
    driver.quit()


def test_check_filter_lohi():
    """
    Проверка работоспособности фильтра (low to high)
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//select/option[@value="lohi"]').click()
    products_price = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    price_products = [float(price.text[1:]) for price in products_price]
    list_products_sort = sorted(price_products)
    assert list_products_sort == price_products, 'filter from low to high does not work'
    driver.quit()


def test_check_filter_hilo():
    """
    Проверка работоспособности фильтра (high to low)
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//select/option[@value="hilo"]').click()
    products_price = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    price_products = [float(price.text[1:]) for price in products_price]
    list_products_sort = sorted(price_products, reverse=True)
    assert list_products_sort == price_products, 'filter from low to high does not work'
    driver.quit()


def test_menu_logout():
    """
    Выход из системы
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click()

    assert driver.current_url == URL, 'url does not match expected'
    driver.quit()


def test_menu_about():
    """
    Проверка работоспособности кнопки "About" в меню
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]').click()

    assert driver.current_url == 'https://saucelabs.com/', 'url does not match expected'
    driver.quit()


def test_menu_reset():
    """
    Проверка работоспособности кнопки "Reset App State"
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]').click()

    assert len(driver.find_elements(By.XPATH, '//button[@id="react-burger-menu-btn"]')), \
        'button "Reset App State" does not work as expected'
    driver.quit()
