import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# ✅ Your BrowserStack Credentials
USERNAME = "rohansonwane_BNJH2r"
ACCESS_KEY = "5fLorEcifzp35JgNM3z1"
SELENIUM_GRID_URL = f"https://rohansonwane_BNJH2r:5fLorEcifzp35JgNM3z1@hub-cloud.browserstack.com/wd/hub"

# ✅ Sample Answers for Form Filling
WORDS = ['apple', 'banana', 'orange', 'grape', 'mango', 'peach', 'pear', 'kiwi', 'plum', 'berry']

def fill_google_form(form_link):
    try:
        # ✅ Setup BrowserStack options
        options = Options()
        options.browser_version = 'latest'
        options.platform_name = 'Windows 10'
        options.set_capability('bstack:options', {
            "os": "Windows",
            "osVersion": "10",
            "browserName": "Chrome",
            "browserVersion": "latest",
            "sessionName": "Google Form Automation",
            "buildName": "Selenium Streamlit Build"
        })

        # ✅ Connect to BrowserStack Grid
        driver = webdriver.Remote(
            command_executor=SELENIUM_GRID_URL,
            options=options
        )
        
        # ✅ Open the Form
        driver.get(form_link)
        time.sleep(2)

        # ✅ Fill Text Fields with Random Words
        text_fields = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//input[@type="text"]'))
        )
        for field in text_fields:
            try:
                field.send_keys(random.choice(WORDS))
                time.sleep(0.5)
            except:
                pass

        # ✅ Select Multiple Choice Answers
        choices = driver.find_elements(By.XPATH, '//div[@role="radio"]')
        for choice in choices:
            if random.choice([True, False]):
                try:
                    choice.click()
                    time.sleep(0.5)
                except:
                    pass

        # ✅ Submit the Form
        submit_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Submit")]'))
        )
        submit_button.click()

        time.sleep(2)
        driver.quit()

        return "✅ Form filled and submitted successfully!"

    except Exception as e:
        return f"❌ Error: {e}"

# ✅ Streamlit UI
st.title("Google Form Auto-Filler (Remote Selenium)")

# ✅ Input Form Link
form_link = st.text_input("Google Form Link", "")

if st.button("Submit Form with Random Data"):
    if form_link:
        status = fill_google_form(form_link)
        st.success(status)
    else:
        st.error("⚠️ Please provide a valid Google Form link!")
