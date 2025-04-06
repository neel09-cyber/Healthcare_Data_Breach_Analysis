from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open window maximized
chrome_options.add_argument("--headless")  # Run in the background (optional)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Provide the path to your chromedriver
service = Service("chromedriver.exe")  # Change this if using another driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Tableau Public URL
url = "https://public.tableau.com/shared/897WFXYZ9?%3Adisplay_static_image=y&%3Aembed=true&%3Aembed=y&%3Alanguage=en-US&%3AshowVizHome=n&%3AapiID=host0#navType=0&navSrc=Parse&1"
driver.get(url)

# Wait for the Tableau div to load
time.sleep(5)  # Adjust based on your internet speed

# Locate the Tableau div
tableau_div = driver.find_element(By.XPATH, "//*[@id='viz-client-container']")
print("Tableau div located!")

# Scroll through the visualization to load all data
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", tableau_div)


# Extract data
data_elements = driver.find_elements(By.XPATH, "//*[@id='tabZoneId3']/div/div/div/div[1]/div[5]")

# Store extracted text
data_list = [element.text for element in data_elements]
print("Data extraction completed!")

# Convert extracted data to DataFrame
df = pd.DataFrame(data_list, columns=["Extracted Data"])

# Save to Excel
df.to_excel("tableau_data.xlsx", index=False)
print("Data saved to 'tableau_data.xlsx'!")

# Close the browser
driver.quit()
