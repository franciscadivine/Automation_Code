from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# -----------------------
# Wait Helper Class
# -----------------------
class WaitHelper:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator, text):
        element = self.clickable(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        self.clickable(locator).click()


# -----------------------
# Login Flow
# -----------------------
def login_with_wrong_details(wait):
    wait.click((AppiumBy.ACCESSIBILITY_ID, "open menu"))
    wait.click((AppiumBy.ACCESSIBILITY_ID, "menu item log in"))

    wait.send_keys((AppiumBy.ACCESSIBILITY_ID, "Username input field"), "monic@gmail.com")
    wait.send_keys((AppiumBy.ACCESSIBILITY_ID, "Password input field"), "test123#")

    wait.click((AppiumBy.ACCESSIBILITY_ID, "Login button"))

    error = wait.visible(
        (By.XPATH, '//android.view.ViewGroup[@content-desc="generic-error-message"]/android.widget.TextView')
    ).text

    assert error == "Provided credentials do not match any user in this service."


# -----------------------
# Add Product Using Scroll
# -----------------------
def open_product_by_name(driver, product_name):
    product = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR,
             f'new UiScrollable(new UiSelector().scrollable(true))'
             f'.scrollIntoView(new UiSelector().text("{product_name}"))')
        )
    )
    product.click()


# -----------------------
# Cart Validation
# -----------------------
def validate_cart(wait):
    wait.click((By.XPATH, '//android.view.ViewGroup[@content-desc="cart badge"]/android.widget.ImageView'))

    total = wait.visible((AppiumBy.ACCESSIBILITY_ID, "total number")).text
    assert total == "6 items"


# -----------------------
# Main Setup
# -----------------------
def main():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.platform_version = "13"
    options.app = "C:/Users/Francisca/Downloads/Android-MyDemoAppRN.1.1.0.build-226.apk"
    options.app_package = "com.saucelabs.mydemoapp.rn"
    options.app_activity = "com.saucelabs.mydemoapp.rn.MainActivity"
    options.automation_name = "UiAutomator2"
    options.no_reset = False
    options.full_reset = True

    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

    # ❌ REMOVE implicit wait (don’t mix waits)
    # driver.implicitly_wait(10)

    wait = WaitHelper(driver)

    login_with_wrong_details(wait)
    open_product_by_name(driver, "Sauce Labs Backpack")
    validate_cart(wait)

    driver.quit()


if __name__ == "__main__":
    main()
