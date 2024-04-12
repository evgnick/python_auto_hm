import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from data import *
from locators import *


def test_auth_with_explicit_waits(driver, wait):
    """
    Проверка функционала регистрации на сайте с использованием явных ожиданий
    """
    driver.get(MAIN_PAGE)

    assert driver.find_element(By.XPATH, WELCOME_TEXT).text == "Практика с ожиданиями в Selenium", \
        "Текст приветствия не соответствует ожидаемому"

    visible_after_button = wait.until(ec.element_to_be_clickable((By.XPATH, START_BUTTON)))

    assert visible_after_button.text == "Начать тестирование"

    visible_after_button.click()
    driver.find_element(By.XPATH, LOGIN_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, RULES_CHECKBOX).click()
    loader = driver.find_element(By.XPATH, REGISTER_BUTTON)
    loader.click()

    assert wait.until(ec.visibility_of_element_located((By.XPATH, LOADER_DIV))), "Загрузчик не отображается на экране"
    assert wait.until(ec.visibility_of_element_located((By.XPATH, MESSAGE_AUTH_TEXT))).text == \
           "Вы успешно зарегистрированы!", "Сообщение 'Вы успешно зарегистрированы!' не отображается"


def test_auth_with_implicitly_waits(driver, wait):
    """
    Проверка функционала регистрации на сайте с использованием неявных ожиданий
    """
    driver.implicitly_wait(20)
    driver.get(MAIN_PAGE)

    assert driver.find_element(By.XPATH, WELCOME_TEXT).text == "Практика с ожиданиями в Selenium", \
        "Текст приветствия не соответствует ожидаемому"
    visible_after_button = driver.find_element(By.XPATH, START_BUTTON)
    actual_text = visible_after_button.text

    assert actual_text == "Начать тестирование"

    visible_after_button.click()
    driver.find_element(By.XPATH, LOGIN_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, RULES_CHECKBOX).click()
    loader = driver.find_element(By.XPATH, REGISTER_BUTTON)
    loader.click()

    assert driver.find_element(By.XPATH, LOADER_DIV), "Загрузчик не отображается на экране"

    visible_after_message = driver.find_element(By.XPATH, MESSAGE_AUTH_TEXT)
    assert visible_after_message.text == \
           "Вы успешно зарегистрированы!", "Сообщение 'Вы успешно зарегистрированы!' не отображается"


def test_auth_with_timer(driver, wait):
    """
    Проверка функционала регистрации на сайте с использованием time.sleep()
    """
    driver.get(MAIN_PAGE)

    assert driver.find_element(By.XPATH, WELCOME_TEXT).text == "Практика с ожиданиями в Selenium", \
        "Текст приветствия не соответствует ожидаемому"

    time.sleep(6)
    visible_after_button = driver.find_element(By.XPATH, START_BUTTON)
    actual_text = visible_after_button.text

    assert actual_text == "Начать тестирование"

    visible_after_button.click()
    driver.find_element(By.XPATH, LOGIN_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, RULES_CHECKBOX).click()
    loader = driver.find_element(By.XPATH, REGISTER_BUTTON)
    loader.click()

    time.sleep(6)
    assert driver.find_element(By.XPATH, LOADER_DIV), "Загрузчик не отображается на экране"

    visible_after_message = driver.find_element(By.XPATH, MESSAGE_AUTH_TEXT)
    assert visible_after_message.text == \
           "Вы успешно зарегистрированы!", "Сообщение 'Вы успешно зарегистрированы!' не отображается"


def test_add_remove_elements(driver, wait):
    """
    Проверка создания и удаления элемента
    """
    driver.get(HEROKUAPP_ADD_REMOVE_ELEMENTS)
    wait.until(ec.element_to_be_clickable((By.XPATH, ADD_BUTTON))).click()
    delete_button = wait.until(ec.element_to_be_clickable((By.XPATH, DELETE_BUTTON)))

    assert delete_button.is_enabled()

    delete_button.click()

    assert len(driver.find_elements(By.XPATH, ELEMENTS_BOX)) < 1, "Кнопка не удалена"


def test_basic_auth(driver):
    """
    Проверка базовой авторизации
    """
    driver.get(HEROKUAPP_BASIC_AUTH)

    assert driver.find_element(By.XPATH, AUTH_TEXT).is_displayed(), \
        "Пользователь не авторизован"


def test_broken_images(driver, wait):
    """
    Получение сломанных изображений
    """
    driver.get(HEROKUAPP_BROKEN_IMAGE)
    images = driver.find_elements(By.XPATH, IMAGES)
    broken_images_count = 0
    print("\n")
    for image in images:
        # Получение naturalWidth изображения
        natural_width = driver.execute_script("return arguments[0].naturalWidth", image)
        if natural_width == 0:
            print("Image not loaded:", image.get_attribute('src'))
            broken_images_count += 1
    assert broken_images_count == 0, "Имеются не загруженные изображения"


def test_checkboxes(driver, wait):
    """
    Проверка чек-бокса
    """
    driver.get(HEROKUAPP_CHECKBOXES)
    checkbox1 = driver.find_element(By.XPATH, CHECKBOX1)

    assert checkbox1.is_displayed(), "Чек-бокс не найден"

    checkbox1.click()
    assert checkbox1.get_attribute('checked'), "Чек-бокс не нажат"

    checkbox2 = driver.find_element(By.XPATH, CHECKBOX2)

    assert checkbox2.is_displayed(), "Чек-бокс не найден"

    checkbox2.click()
    assert not checkbox2.get_attribute('checked'), "Чек-бокс остался нажатым"
