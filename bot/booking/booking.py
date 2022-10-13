from selenium import webdriver
import bot.booking.constants as const
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bot.booking.Filterations import Filterations
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Booking(webdriver.Chrome):

    def __init__(self, driver_path=r"C:/SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()

        selected_currency_element = self.find_element(By.CSS_SELECTOR,
                                                      f'a[data-modal-header-async-url-param="changed_currency=1'
                                                      f'&selected_currency={currency}&top_currency=1"')
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.NAME, 'ss')

        search_field.send_keys(place_to_go)
        WebDriverWait(self, 40).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'li[data-i="0"]'))
        )
        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')

        first_result.click()

    def date_selection(self, check_in, check_out):
        check_in_elem = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in}"]')
        check_in_elem.click()

        check_out_elem = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out}"]')
        check_out_elem.click()

    def date_if_far(self, num_of_months_from_today):
        next_arrow = self.find_element(By.XPATH, '//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[2]')

        for i in range(num_of_months_from_today):
            next_arrow.click()

    def num_of_travellers(self, adults=2, children=0, rooms=1):
        num_btn = self.find_element(By.XPATH, '//*[@id="xp__guests__toggle"]')
        num_btn.click()

        num_of_adults = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div['
                                                    '2]/span[1]')
        sub_adults_btn = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div['
                                                     '2]/button[1]')
        add_adults_btn = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div['
                                                     '2]/button[2]')

        while int(num_of_adults.text) != adults:
            if int(num_of_adults.text) > adults:
                sub_adults_btn.click()
            else:
                add_adults_btn.click()

        num_of_child = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div['
                                                   '2]/span[1]')
        add_child_btn = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div['
                                                    '2]/button[2]')
        sub_child_btn = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div['
                                                    '2]/button[1]')
        while int(num_of_child.text) != children:
            if int(num_of_child.text) > children:
                sub_child_btn.click()
            else:
                add_child_btn.click()

        num_of_rooms = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[4]/div/div['
                                                   '2]/span[1]')
        add_rooms_btn = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[4]/div/div['
                                                    '2]/button[2]')
        sub_rooms_btn = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[4]/div/div['
                                                    '2]/button[1]')

        while int(num_of_rooms.text) != rooms:
            if int(num_of_rooms.text) > rooms:
                sub_rooms_btn.click()
            else:
                add_rooms_btn.click()

    def age_of_children(self, *age):
        count = 1
        for a in age:
            Select(self.find_element(By.CSS_SELECTOR, f'select[aria-label="Child {count} age"]')).select_by_value(a)
            age_number = self.find_element(By.CSS_SELECTOR, f'option[value="{a}"]')
            age_number.click()
            count = count + 1

    def search_btn(self):
        search = self.find_element(By.XPATH, '//*[@id="frm"]/div[1]/div[4]/div[2]/button')
        search.click()

    def filteration(self):
        filters = Filterations(driver=self)

        filters.price_sorting()
        filters.star_rating(1,2,3)

    def results(self):

        res = self.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

        for items in res:
            hotel_name = items.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute('innerHTML').strip()
            price = items.find_element(By.XPATH, '//*[@id="search_results_table"]/div[2]/div/div/div/div[3]/div['
                                                 '2]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div['
                                                 '2]/span').get_attribute('innerHTML').strip()

            print([hotel_name, price])

