import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Task1 import filename

driver = webdriver.Chrome()

driver.get(filename)

# Find the div with id "test-3-div"
test_3_div = driver.find_element(By.ID, "test-3-div")

# Assert that "Option 1" is the default selected value
dropdown_button = test_3_div.find_element(By.ID, "dropdownMenuButton")
default_selected_option = dropdown_button.text.strip()
assert default_selected_option == "Option 1", f"Default selected value is not 'Option 1', actual value: {default_selected_option}"

# Select "Option 3" from the dropdown list
dropdown_button.click()
option_3 = test_3_div.find_element(By.XPATH, "//a[text()='Option 3']")
option_3.click()

# Wait for the dropdown button text to change to "Option 3"
wait = WebDriverWait(driver, 10)
wait.until(EC.text_to_be_present_in_element((By.ID, "dropdownMenuButton"), "Option 3"))
print("Task 3 completed ✅")

# Close the browser
time.sleep(10)

# Close the browser
driver.quit()
