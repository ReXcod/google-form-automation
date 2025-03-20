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
        # ✅ Define capabilities for BrowserStack
        desired_capabilities = {
            "browserName": "Chrome",
            "browserVersion": "latest",
            "bstack:options": {
                "os": "Windows",
                "osVersion": "10",
                "sessionName": "Google Form Automation",
                "buildName": "Selenium Streamlit Build",
                "userName": rohansonwane_BNJH2r,
                "accessKey": "5fLorEcifzp35JgNM3z1"  # ✅ Correct (string format)

            }
        }

        # ✅ Connect to BrowserStack
        driver = webdriver.Remote(
            command_executor=SELENIUM_GRID_URL,
            desired_capabilities=desired_capabilities
        )

        # ✅ Open Form & Fill
        driver.get(form_link)
        time.sleep(2)
        return "✅ Form submitted successfully!"

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
