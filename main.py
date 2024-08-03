from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_appium(plaform_name: str, device_name: str, udid: str):
    desired_caps = {
        'platformName': plaform_name,
        'deviceName': device_name,
        'appPackage': 'com.uxbert.sfa',
        'appActivity': 'com.uxbert.sfa.MainActivity',
        'automationName': 'UiAutomator2',
        'noReset': True,
        'udid': udid
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


def change_language_to_arabic(driver):
    wait = WebDriverWait(driver, 10)

    settings_button = wait.until(EC.element_to_be_clickable((By.ID, 'com.uxbert.sfa:id/settings_button')))
    settings_button.click()

    # Navigate to language settings
    language_option = wait.until(EC.element_to_be_clickable((By.ID, 'com.uxbert.sfa:id/language_option')))
    language_option.click()

    # Select Arabic language
    arabic_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="العربية"]')))
    arabic_option.click()


def navigate_screens(driver):
    wait = WebDriverWait(driver, 10)

    # Navigate to Login screen
    login_button = wait.until(EC.element_to_be_clickable((By.ID, 'com.uxbert.sfa:id/login_button')))
    login_button.click()

    # Navigate to Explore by category screen
    explore_button = wait.until(EC.element_to_be_clickable((By.ID, 'com.uxbert.sfa:id/explore_button')))
    explore_button.click()

    # Navigate to Edit Profile screen
    profile_button = wait.until(EC.element_to_be_clickable((By.ID, 'com.uxbert.sfa:id/profile_button')))
    profile_button.click()
    edit_profile_button = wait.until(EC.element_to_be_clickable((By.ID, 'com.uxbert.sfa:id/edit_profile_button')))
    edit_profile_button.click()


if __name__ == "__main__":

    driver = setup_appium("Android", "POCO F5 Pro", "bf703b8")
    try:
        change_language_to_arabic(driver)
        navigate_screens(driver)
    finally:
        driver.quit()
