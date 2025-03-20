import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import shutil

# Sample word list for text fields
WORDS = ['apple', 'banana', 'orange', 'grape', 'mango', 'peach', 'pear', 'kiwi', 'plum', 'berry']

# Path to Chromium and Chromedriver
CHROMEDRIVER_PATH = shutil.which("chromedriver")
CHROME_PATH = shutil.which("chromium")

def fill_google_form(form_link):
    try:
        options = Options()
        options.binary_location = CHROME_PATH
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(form_link)

        time.sleep(2)

        # Fill text fields with a single random word
        text_fields = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//input[@type="text"]'))
        )
        for field in text_fields:
            field.send_keys(random.choice(WORDS))
            time.sleep(0.5)

        # Fill multiple-choice questions (select a random option)
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
st.title("Google Form Auto-Filler (Multiple Choice + Text)")

form_link = st.text_input("Google Form Link", "")

if st.button("Submit Form with Random Data"):
    if form_link:
        status = fill_google_form(form_link)
        st.success(status)
    else:
        st.error("Please provide a valid Google Form link!")
