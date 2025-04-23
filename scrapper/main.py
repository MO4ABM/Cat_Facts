from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # To automatically manage ChromeDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
if __name__ == "__main__": 
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run in headless mode (without opening the browser window)
    # options.add_argument("--disable-gpu")

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # URL of the Django home page
    url = "http://127.0.0.1:8000/"

    # Navigate to the home page
    driver.get(url)

    # Wait until the <p> tag with class 'fact-text' becomes visible (explicit wait)
    fact_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.fact-text"))
    )

    # Extract the cat fact text from the element
    fact = fact_element.text  # Extract the text content of the <p> tag

    # Print the scraped fact
    print(f"Scraped Cat Fact: {fact}")

    # Close the browser
    driver.quit()
