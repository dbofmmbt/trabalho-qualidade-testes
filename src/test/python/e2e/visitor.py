from selenium import webdriver
from selenium.webdriver.common.by import By


def visitor_sees_food_menu(driver: webdriver.Chrome):
    visitor_goes_to_food_menu(driver)

    food_list = driver.find_element(by=By.CLASS_NAME, value="divLanche")
    food_items = food_list.find_elements(by=By.CLASS_NAME, value="row")
    assert len(food_items) != 0

    food_item = food_items[0]

    assert_food(food_item)


def visitor_goes_to_food_menu(driver):
    driver.get(
        "http://localhost:8080/trabalho-qualidade-testes/view/home/home.html")

    assert 'lanchonete' in driver.title.lower()

    menu_access_btn = driver.find_element(
        by=By.XPATH, value="//*[contains(text(), 'Acessar Cardápio')]")
    menu_access_btn.click()


def assert_food(food_item):
    image = food_item.find_element(by=By.TAG_NAME, value="img")
    assert image != None and loaded_succesfully(image)

    price = food_item.find_element(by=By.CLASS_NAME, value="preco").text
    symbol, price = price.strip().split()
    assert symbol == 'R$'
    # throws exception if can't be converted
    float(price)


def loaded_succesfully(image):
    return image.get_property('naturalWidth') != 0


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(5.0)

    try:
        visitor_sees_food_menu(driver)
    finally:
        driver.quit()
