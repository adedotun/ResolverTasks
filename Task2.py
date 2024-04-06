import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Task1 import filename


driver = webdriver.Chrome()


driver.get(filename)

wait = WebDriverWait(driver, 10)
test_2_div = wait.until(EC.presence_of_element_located((By.ID, "test-2-div")))

list_group = test_2_div.find_element(By.CLASS_NAME, "list-group")
list_items = list_group.find_elements(By.TAG_NAME, "li")

# Assertion 1: Verifying there are three list items
assert len(list_items) == 3, "List group does not contain 3 items"

second_list_item = list_items[1]
# Assertion 2: Verifying the text content of the second list item
assert second_list_item.text.strip() == "List Item 2", "Second list item text is incorrect"


badge_element = second_list_item.find_element(By.CLASS_NAME, "badge")
# Assertion 3: Verifying the badge value of the second list item
assert badge_element.text.strip() == "6", "Second list item badge value is incorrect"
print("Task 2 completed ✅")

# Close the browser
time.sleep(10)

# Close the browser
driver.quit()
