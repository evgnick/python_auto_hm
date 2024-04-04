import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import (USER_FIELD, PASSWORD_FIELD, LOGIN_BUTTON, ADD_TO_CART_BUTTON, REMOVE_BUTTON)
from data import LOGIN_POS, PASSWORD_POS, MAIN_PAGE, CART_PAGE


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    print('\nquit browser...')
    chrome_driver.quit()


@pytest.fixture()
def auth(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(By.XPATH, USER_FIELD).send_keys(LOGIN_POS)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD_POS)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    yield driver


@pytest.fixture()
def add_item_to_cart(driver):
    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON).click()


@pytest.fixture()
def delete_item_to_cart(driver):
    yield
    driver.get(CART_PAGE)
    driver.find_element(By.XPATH, REMOVE_BUTTON).click()
