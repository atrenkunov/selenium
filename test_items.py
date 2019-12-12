from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_button_visability_with_different_langs(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    # place for time.sleep(30)

    try:
        button = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-add-to-basket")))
    except TimeoutException:
        assert False, "Can't find basket button"
