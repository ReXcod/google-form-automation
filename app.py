import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

WORDS = ['apple', 'banana', 'orange', 'grape', 'mango', 'peach', 'pear', 'kiwi', 'plum', 'berry']

# BrowserStack Credentials
USERNAME = "YOUR_BROWSERSTACK_USERNAME"
ACCESS_KEY = "YOUR_BROWSERSTACK_ACCESS_KEY"
SELENIUM_GRID_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

def fill_google_form(form_link):
    try:
        # Configure BrowserStack options
        capabilities = {
            'browserName': 'Chrome',
            'browserVersion': 'latest',
            'os': 'Windows',
            'os_version': '10'
        }

        # Connect to remote Selenium server
        driver = webdriver.Remote(
            command_executor=SELENIUM_GRID_URL,
            desired_capabilities=capabilities
        )
        driver.get(form_link)

        time.sleep(2)

        # Fill text fields with a single random word
        text_fields = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//input[@type="text"]'))
        )
        for field in text_fields:
            field.send_keys(random.choice(WORDS))
            time.sleep(0.5)

        # Fill multiple-choice questions
        choices = driver.find_elements(By.XPATH, '//div[@role="radio"]')
        for choice in choices:
            if random.choice([True, False]):
                choice.click()
                time.sleep(0.5)

        # Submit the form
        submit_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Submit")]'))
        )
        submit_button.click()

        time.sleep(2)
        driver.quit()

        return "Form filled and submitted successfully!"

    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Google Form Auto-Filler (Remote Selenium)")

form_link = st.text_input("Google Form Link", "")

if st.button("Submit Form with Random Data"):
    if form_link:
        status = fill_google_form(form_link)
        st.success(status)
    else:
        st.error("Please provide a valid Google Form link!")
