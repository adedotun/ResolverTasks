import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Task1 import filename


def get_cell_value(row_index, column_index):
    # Locate the table element
    table = driver.find_element(By.CLASS_NAME, "table")

    # Find the cell at the specified row and column index
    cell_xpath = f"//tbody/tr[{row_index + 1}]/td[{column_index + 1}]"
    cell = table.find_element(By.XPATH, cell_xpath)

    # Return the text of the cell
    return cell.text


driver = webdriver.Chrome()
driver.get(filename)

# Find the value of the cell at coordinates (2, 2)
cell_value = get_cell_value(2, 2)

# Assert that the value of the cell is "Ventosanzap"
assert cell_value == "Ventosanzap", f"Cell value is not 'Ventosanzap', actual value: {cell_value}"
print("Task 6 completed ✅")

# Close the browser
time.sleep(10)

# Close the browser
driver.quit()
