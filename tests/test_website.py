from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (use Chrome in a container-friendly way)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without GUI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Change this URL if necessary
URL = "http://pipelines-vote-ui-test-cop-pipeline.apps.cluster-bxv9v.dynamic.redhatworkshops.io:8080"

# Start WebDriver
driver = webdriver.Chrome(options=options)
driver.get(URL)

try:
    # Verify page title
    assert "My Website" in driver.title, f"Expected title 'My Website', got '{driver.title}'"

    # Verify the H1 text
    h1_text = driver.find_element(By.TAG_NAME, "h1").text
    assert h1_text == "Welcome to My Website!", f"Expected 'Welcome to My Website!', got '{h1_text}'"

    print("✅ Test Passed: Website is displayed correctly.")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")
finally:
    driver.quit()

