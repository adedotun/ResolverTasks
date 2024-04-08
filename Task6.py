import time
from selenium.webdriver.common.by import By
from Home import filename, driver


def get_cell_value(row_index, column_index):
    # Locate the table element
    table = driver.find_element(By.CLASS_NAME, "table")

    # Find the cell at the specified row and column index
    cell_xpath = f"//tbody/tr[{row_index + 1}]/td[{column_index + 1}]"
    cell = table.find_element(By.XPATH, cell_xpath)

    # Return the text of the cell
    return cell.text


driver.get(filename)

# Find the value of the cell at coordinates (2, 2)
cell_value = get_cell_value(2, 2)

# Assert that the value of the cell is "Ventosanzap"
assert cell_value == "Ventosanzap", f"Cell value is not 'Ventosanzap', actual value: {cell_value}"
print("Task 6 completed ✅")

# Close the browser
time.sleep(3)

# Close the browser
driver.quit()
