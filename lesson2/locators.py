# Main page
USER_FIELD = "//input[@id='user-name']"
PASSWORD_FIELD = "//input[@id='password']"
LOGIN_BUTTON = "//*[@id='login-button']"
ERROR_TEXT = "//h3[contains(text(), 'Username and password do not match')]"

# Products page
ADD_TO_CART_BUTTON = "//button[@id='add-to-cart-sauce-labs-backpack']"
REMOVE_CART_BUTTON = "//button[@id='remove-sauce-labs-backpack']"
COUNT_CART_TEXT = "//span[@class='shopping_cart_badge']"
CART_BUTTON = "//a[@class='shopping_cart_link']"
ITEM_NAME_LINK = "//a[@id='item_4_title_link']"
ITEM_IMG_LINK = "//a[@id='item_4_img_link']"
FILTER_NAME_AZ = "//select/option[@value='az']"
FILTER_NAME_ZA = "//select/option[@value='za']"
FILTER_PRICE_LOHI = "//select/option[@value='lohi']"
FILTER_PRICE_HILO = "//select/option[@value='hilo']"
ITEM_HEADINGS = "//div[@class='inventory_item_description']//a//div"
PRICES = "//div[@class='inventory_item_price']"
MENU_BAR_BUTTON = "//button[@id='react-burger-menu-btn']"
LOGOUT_LINK = "//a[@id='logout_sidebar_link']"
ABOUT_LINK = "//a[@id='about_sidebar_link']"
RESET_LINK = "//a[@id='reset_sidebar_link']"

# Item page
ADD_TO_CART_BUTTON_ITEM = "//button[@id='add-to-cart']"
REMOVE_BUTTON_ITEM = "//button[@id='remove']"
ITEMS_NAME = "//div[contains(text(),'Sauce Labs')]"

# Cart page
REMOVE_BUTTON = "//button[contains(@id,'remove')]"
REMOVE_DIV = "//div[@class='removed_cart_item']"
ITEMS_TEXT = "//div[@class='cart_item']"
CHECKOUT_BUTTON = "//button[@id='checkout']"

# Checkout page step one
FIRST_NAME_FIELD = "//input[@id='first-name']"
LAST_NAME_FIELD = "//input[@id='last-name']"
ZIP_CODE_FIELD = "//input[@id='postal-code']"
CONTINUE_BUTTON = "//input[@id='continue']"

# Checkout page step two
FINISH_BUTTON = "//button[@id='finish']"

# Checkout complete
COMPLETE_TEXT = "//h2[@class='complete-header']"

# Checkbox page
USER_FIELD_REG = "//input[@id='username']"
PASSWORD_FIELD_REG = "//input[@id='password']"
AGREEMENT_CHECKBOX = "//input[@type='checkbox']"
REGISTER_BUTTON = "//button[@id='registerButton']"
