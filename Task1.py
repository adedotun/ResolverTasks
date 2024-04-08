import time
from selenium.webdriver.common.by import By
from Home import filename, driver


# Navigate to the homepage
driver.get(filename)

email_input = driver.find_element(By.ID, "inputEmail")
assert email_input.is_displayed() and email_input.is_enabled(), "Email input is not present or enabled"
email_input.clear()
email_input.send_keys("adedotun@resolver.com")
time.sleep(1)

password_input = driver.find_element(By.ID, "inputPassword")
assert password_input.is_displayed() and password_input.is_enabled(), "Password input is not present or enabled"
password_input.clear()
password_input.send_keys("Qw@ty4321")
time.sleep(1)

# Assert that login button is present
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
assert login_button.is_displayed() and login_button.is_enabled(), "Login button is not present or enabled"
time.sleep(1)
login_button.click()
print("Task 1 completed ✅")

time.sleep(3)
driver.quit()
