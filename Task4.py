import time
from selenium.webdriver.common.by import By
from Home import filename, driver

driver.get(filename)

# Find the div with id "test-4-div"
test_4_div = driver.find_element(By.ID, "test-4-div")
driver.execute_script("arguments[0].scrollIntoView(true);", test_4_div)

# Find the first button and check if it is enabled
first_button = test_4_div.find_element(By.XPATH, "//button[1]")
assert first_button.is_enabled(), "First button is not enabled"

# Find the second button and check if it is disabled
second_button = test_4_div.find_element(By.XPATH, "//button[2]")
assert not second_button.is_enabled(), "Second button is not disabled"
print("Task 4 completed ✅")

time.sleep(4)
driver.quit()