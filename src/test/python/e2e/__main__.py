from selenium import webdriver

from visitor import visitor_sees_food_menu

driver = webdriver.Chrome()
driver.implicitly_wait(3.0)

try:
    visitor_sees_food_menu(driver)
finally:
    driver.quit()

print("tests passed successfully!")
