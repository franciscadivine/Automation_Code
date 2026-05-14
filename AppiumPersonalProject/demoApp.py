from selenium.webdriver.common.actions import interaction
from selenium.webdriver.support import expected_conditions as EC

from appium import webdriver
import time
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
#from appium.options.common import AppiumOptions
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from pycparser.c_ast import ID
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.mobile import Mobile
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_clickable(driver, locator, timeout=60):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable(locator))

def wait_for_visible(driver, locator, timeout=60):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def loginWithWrongUserDetails(driver):

 wait_for_visible(driver, (AppiumBy.ACCESSIBILITY_ID, "open menu"))
 menu = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "open menu"))
 menu.click()
 loginclick = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID,"menu item log in"))
 loginclick.click()
 userName = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Username input field"))
 userName.send_keys("monic@gmail.com")
 password = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Password input field"))
 password.send_keys("test123#")
 loginbtn = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Login button"))
 loginbtn.click()
 errorMessage = wait_for_visible(driver,(By.XPATH, "//android.view.ViewGroup[@content-desc=\"generic-error-message\"]/android.widget.TextView")).text
 print("Attribute:text:", errorMessage)

 assert errorMessage == "Provided credentials do not match any user in this service."



def emptyFieldValidation(driver):
    time.sleep(5)
    userName =wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Username input field"))
    userName.clear()
    loginbtn = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Login button"))
    loginbtn.click()
    fieldErrorMessage = driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Username-error-message"]/android.widget.TextView').text
    print("Attribute:text:", fieldErrorMessage)
    assert fieldErrorMessage == "Username is required"
    userName = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Username input field"))
    userName.send_keys("monic@gmail.com")
    password = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Password input field"))
    password.clear()
    loginbtn = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Login button"))
    loginbtn.click()
    fieldErrorMessage1 = wait_for_visible(driver,(By.XPATH,'//android.view.ViewGroup[@content-desc="Password-error-message"]/android.widget.TextView')).text
    print("Attribute:text:", fieldErrorMessage1)
    assert fieldErrorMessage1 == "Password is required"

def correctUserLogin(driver):
    time.sleep(5)
    userName = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Username input field")
    userName.clear()

    password = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Password input field")
    password.clear()
    nameOfUser =driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="bob@example.com-autofill"]/android.widget.TextView')
    nameOfUser.click()
    loginbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login button")
    loginbtn.click()
    productText = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().text("Products"))'
    )
    print("Attribute:text:", productText.text)
    print("Is Displayed:", productText.is_displayed())
    assert  productText.text == "Products"

def swipe_up(driver):
    size = driver.get_window_size()

    start_x = size["width"] // 2
    start_y = int(size["height"] * 0.8)
    end_y = int(size["height"] * 0.2)

    finger = PointerInput(interaction.POINTER_TOUCH, "finger")
    actions = ActionBuilder(driver)
    actions.pointer_action.move_to_location(start_x, start_y)
    actions.pointer_action.pointer_down()
    actions.pointer_action.pause(0.2)
    actions.pointer_action.move_to_location(start_x, end_y)
    actions.pointer_action.release()

    actions.perform()
def open_product_by_name(driver, product_name):
    product = WebDriverWait(driver, 80).until(
        EC.visibility_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR,
             f'new UiScrollable(new UiSelector().scrollable(true))'
             f'.scrollIntoView(new UiSelector().text("{product_name}"))')
        )
    )
    product.click()




def addProductToCart(driver):
    time.sleep(5)
    sortPrice = wait_for_clickable(driver,(By.XPATH, '//android.view.ViewGroup[@content-desc="sort button"]/android.widget.ImageView'))
    sortPrice.click()
    Asc = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "priceAsc"))
    Asc.click()
    product1 = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().text("Sauce Labs Onesie"))'
    )
    product1.click()
    #open_product_by_name(driver, "Sauce Labs Onesie")
    time.sleep(5)
    starReview = driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="review star 5"]/android.widget.TextView')
    starReview.click()
    closeModel = wait_for_clickable(AppiumBy.ACCESSIBILITY_ID, "Close Modal button")
    closeModel.click()
    time.sleep(15)

    wait_for_visible(driver, (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn.click()
    menu = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "open menu"))
    menu.click()
    catalog = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "open menu"))
    catalog.click()

    #wait_for_visible(driver, open_product_by_name(driver, "Sauce Labs Bike Light"))
    product2 = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().text("Sauce Labs Bike Light"))'
    )
    #open_product_by_name(driver, "Sauce Labs Bike Light")
    product2.click()

    wait_for_visible(driver, (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn.click()
    menu = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "open menu"))
    menu.click()
    catalog = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "open menu"))
    catalog.click()

    #wait_for_visible(driver, open_product_by_name(driver, "Sauce Labs Bolt T-Shirt"))
    product3 = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().text("Sauce Labs Bolt T-Shirt"))'
    )
    #open_product_by_name(driver, "Sauce Labs Bolt T-Shirt")
    product3.click()
    wait_for_visible(driver, (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn = wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn.click()

    menu = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "open menu"))
    menu.click()
    catalog = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "open menu"))
    catalog.click()

    #wait_for_visible(driver, open_product_by_name(driver, "Test.allTheThings() T-Shirt"))
    product4 = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().text("Test.allTheThings() T-Shirt"))'
    )
    #open_product_by_name(driver, "Test.allTheThings() T-Shirt")
    product4.click()
    wait_for_visible(driver, (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn.click()

    menu = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "open menu"))
    menu.click()
    catalog = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "open menu"))
    catalog.click()

    product5 = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().text("Sauce Labs Backpack"))'
    )
    open_product_by_name(driver, "Sauce Labs Backpack")
    #wait_for_clickable(driver, open_product_by_name(driver, "Sauce Labs Backpack"))
    product5.click()

    wait_for_visible(driver, (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn.click()

    menu = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "open menu"))
    menu.click()
    catalog = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "open menu"))
    catalog.click()

    open_product_by_name(driver, "Sauce Labs Fleece Jacket")
    #product6 = wait_for_clickable(driver, open_product_by_name(driver, "Sauce Labs Fleece Jacket"))
    #product6.click()

    wait_for_visible(driver, (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn = wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button"))
    addToCartBtn.click()

    cart = wait_for_clickable(driver,(By.XPATH, '//android.view.ViewGroup[@content-desc="cart badge"]/android.widget.ImageView'))
    cart.click()
    totalItem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "total number")
    print("Attribute: text:", totalItem.text)
    assert totalItem.text == "6 items"
    removeItem1 = driver.find_element(By.XPATH, '(//android.view.ViewGroup[@content-desc="remove item"])[1]/android.widget.TextView')
    removeItem1.click()
    removeItem2 = driver.find_element(By.XPATH,'(//android.view.ViewGroup[@content-desc="remove item"])[1]/android.widget.TextView')
    removeItem2.click()
    totalItem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "total number")
    print("Attribute: text:",totalItem.text)
    assert totalItem.text == "4 items"

def shippingDetails(driver):
    time.sleep(5)
    checkoutBtn = wait_for_clickable(driver,(By.XPATH, '//android.view.ViewGroup[@content-desc="Proceed To Checkout button"]/android.widget.TextView'))
    checkoutBtn.click()
    wait = WebDriverWait(driver, 20)
    fullName = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Full Name* input field"))
    )
    wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "Full Name* input field"))
    fullName.click()
    fullName.send_keys("Monic Yola")

    wait = WebDriverWait(driver, 20)
    addressLine1 = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Address Line 1* input field"))
    )
    wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "Address Line 1* input field"))
    addressLine1.click()
    addressLine1.send_keys("123 Main Street")

    driver.hide_keyboard()
    wait = WebDriverWait(driver, 20)
    addressLine2 = wait.until(
       EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Address Line 2 input field"))
    )
    wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "Address Line 2 input field"))
    addressLine2.click()
    addressLine2.send_keys("123 Main door")

    driver.hide_keyboard()
    wait = WebDriverWait(driver, 20)
    city = wait.until(   EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "City* input field"))
    )
    wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "City* input field"))
    city.click()
    city.send_keys("Lagos Badagry")

    driver.hide_keyboard()
    wait = WebDriverWait(driver, 20)
    state = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "State/Region input field"))
    )
    wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "State/Region input field"))
    state.click()
    state.send_keys("Lagos")
    driver.hide_keyboard()

    wait = WebDriverWait(driver, 20)
    zipCode = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Zip Code* input field"))
    )
    wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "Zip Code* input field"))
    zipCode.click()
    zipCode.send_keys("100001")
    driver.hide_keyboard()

    wait = WebDriverWait(driver, 20)
    country =wait.until( EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Country* input field"))
     )
    wait_for_clickable(driver, (AppiumBy.ACCESSIBILITY_ID, "Country* input field"))
    country.click()
    country.send_keys("Nigeria")

def paymentProceedure(driver):
    time.sleep(5)
    paymentBtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "To Payment button")
    paymentBtn.click()
    paymentScreenText = driver.find_element(By.XPATH, "//android.widget.ScrollView[@content-desc=\"checkout payment screen\"]/android.view.ViewGroup/android.widget.TextView[1]")
    print("Payment Screen:",paymentScreenText.text)
    assert paymentScreenText.text == "Enter a payment method"
    print("Is Displayed:", paymentScreenText.is_displayed())
    wait = WebDriverWait(driver, 20)
    cardName = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Full Name* input field"))
    )
    cardName.click()
    cardName.send_keys("Jake Yola")

    driver.hide_keyboard()
    wait = WebDriverWait(driver, 20)
    cardNumber = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Card Number* input field"))
    )
    cardNumber.click()
    cardNumber.send_keys("5401234567890561")

    driver.hide_keyboard()
    wait = WebDriverWait(driver, 20)
    expirationDate = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Expiration Date* input field"))
    )
    expirationDate.click()
    expirationDate.send_keys("03/30")

    driver.hide_keyboard()
    wait = WebDriverWait(driver, 20)
    securityCode = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Security Code* input field"))
    )
    securityCode.click()
    securityCode.send_keys("089")
    driver.hide_keyboard()
    reviewOrderBtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Review Order button")
    reviewOrderBtn.click()
    reviewOrderBtn.click()

def placeOrder(driver):
    time.sleep(5)
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(5)'
    )
    driver.save_screenshot("placeOrder.png")
    placeOrderBtn = wait_for_visible(driver, (AppiumBy.ACCESSIBILITY_ID, "Place Order button"))
    wait_for_clickable(driver,(AppiumBy.ACCESSIBILITY_ID, "Place Order button"))
    placeOrderBtn.click()

    orderValidationText = wait_for_visible(driver,(By.XPATH, '//android.view.ViewGroup[@content-desc="checkout complete screen"]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[2]'))
    print("orderValidationText:", orderValidationText.text)
    assert orderValidationText.text == "Thank you for your order"
    print("Is Displayed:", orderValidationText.is_displayed())




















def main():
    print("SCRIPT STARTED")

    # Create Appium options
    options = UiAutomator2Options()
    options.platform_name = "android"
    options.device_name = "emulator-5554"
    options.platform_version = "13"
    options.app = "C:/Users/Francisca/Downloads/Android-MyDemoAppRN.1.1.0.build-226.apk"
    options.app_package= "com.saucelabs.mydemoapp.rn"
    options.app_activity= "com.saucelabs.mydemoapp.rn.MainActivity"
    options.automation_name = "UiAutomator2"
    options.noSign = True
    options.no_reset = False
    options.full_reset = True

    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    driver.implicitly_wait(15)
    loginWithWrongUserDetails(driver)
    emptyFieldValidation(driver)
    correctUserLogin(driver)
    addProductToCart(driver)
    shippingDetails(driver)
    paymentProceedure(driver)
    placeOrder(driver)



if __name__ == "__main__":
        main()
