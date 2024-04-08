import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Home import filename, driver

# Navigate to the page containing the HTML
driver.get(filename)

# Find the div with id "test-5-div"
test_5_div = driver.find_element(By.ID, "test-5-div")
driver.execute_script("arguments[0].scrollIntoView(true);", test_5_div)

# Wait for the button to be displayed
button = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.ID, "test5-button")))
button.click()

# Assert that a success message is displayed
success_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "test5-alert")))
assert success_message.text == "You clicked a button!", "Success message is not displayed"

# Assert that the button is disabled
assert button.get_attribute("disabled") == "true", "Button is not disabled"
print("Task 5 completed ✅")

time.sleep(10)
driver.quit()
