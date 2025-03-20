import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to fill Google Form
def fill_google_form(form_link, text_data):
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(form_link)

        time.sleep(2)  # Wait for the form to load

        # Fill text fields
        text_fields = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//input[@type="text"]'))
        )
        for field, text in zip(text_fields, text_data):
            field.send_keys(text)
            time.sleep(1)

        # Submit the form
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Submit")]'))
        )
        submit_button.click()

        time.sleep(2)
        driver.quit()
        return "Form submitted successfully!"
    
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Google Form Auto-Filler")

form_link = st.text_input("Google Form Link", "")
num_fields = st.number_input("Number of Fields to Fill", min_value=1, value=1, step=1)

text_data = []
for i in range(num_fields):
    text = st.text_input(f"Field {i + 1} Text")
    text_data.append(text)

if st.button("Submit Form"):
    if form_link and all(text_data):
        status = fill_google_form(form_link, text_data)
        st.success(status)
    else:
        st.error("Please provide all required details!")
