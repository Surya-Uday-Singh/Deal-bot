from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Filterations:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def star_rating(self, *star_values):
        filter_star = self.driver.find_element(By.XPATH, '//*[@id="left_col_wrapper"]/div[2]/div/div/div[2]/div[6]')
        star_elem = filter_star.find_elements(By.CSS_SELECTOR, '*')

        for value in star_values:
            for elements in star_elem:
                if str(elements.get_attribute('innerHTML')).strip() == f'{value} star':
                    elements.click()
                if str(elements.get_attribute('innerHTML')).strip() == f'{value} stars':
                    elements.click()

    def price_sorting(self):
        price_sort = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]'))
        )
        price_sort.click()
        lowest_price = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]')
        lowest_price.click()
