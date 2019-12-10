from selenium import webdriver
import time

page = "http://suninjuly.github.io/registration2.html";


def positive_login():
    browser = webdriver.Chrome();
    browser.get(page)

    try:
        browser.find_element_by_css_selector(".first_block input.form-control.first").send_keys("Ivan")
        browser.find_element_by_css_selector(".first_block input.form-control.second").send_keys("Ivanov")
        browser.find_element_by_css_selector(".first_block input.form-control.third").send_keys("Ivan@ya.ru")

        browser.find_element_by_css_selector("button.btn").click();

        time.sleep(2)

        result = browser.find_element_by_tag_name("h1")
        assert "Congratulations! You have successfully registered!" == result.text

    finally:
        browser.quit()


def pass_only_name():
    browser = webdriver.Chrome();
    browser.get(page)

    try:
        browser.find_element_by_css_selector(".first_block input.form-control.first").send_keys("Ivan")
        browser.find_element_by_css_selector("button.btn").click();

        time.sleep(2)

        result = browser.find_element_by_tag_name("h1")
        assert "Congratulations! You have successfully registered!" != result.text

    finally:
        browser.quit()


def pass_only_last_name():
    browser = webdriver.Chrome();
    browser.get(page)

    try:
        browser.find_element_by_css_selector(".first_block input.form-control.second").send_keys("Ivanov")
        browser.find_element_by_css_selector("button.btn").click();

        time.sleep(2)

        result = browser.find_element_by_tag_name("h1")
        assert "Congratulations! You have successfully registered!" != result.text

    finally:
        browser.quit()


def pass_only_email():
    browser = webdriver.Chrome();
    browser.get(page)

    try:
        browser.find_element_by_css_selector(".first_block input.form-control.third").send_keys("Ivan@ya.ru")
        browser.find_element_by_css_selector("button.btn").click();

        time.sleep(2)

        result = browser.find_element_by_tag_name("h1")
        assert "Congratulations! You have successfully registered!" != result.text

    finally:
        browser.quit()


def empty_login():
    browser = webdriver.Chrome();
    browser.get(page)

    try:
        browser.find_element_by_css_selector("button.btn").click();
        time.sleep(2)

        result = browser.find_element_by_tag_name("h1")
        assert "Congratulations! You have successfully registered!" != result.text

    finally:
        browser.quit()


def login_with_all_fields():
    browser = webdriver.Chrome();
    browser.get(page)

    try:
        # required
        browser.find_element_by_css_selector(".first_block input.form-control.first").send_keys("Ivan")
        browser.find_element_by_css_selector(".first_block input.form-control.second").send_keys("Ivanov")
        browser.find_element_by_css_selector(".first_block input.form-control.third").send_keys("Ivan@ya.ru")

        # others
        browser.find_element_by_css_selector(".second_block input.form-control.first").send_keys("8-111-111-11-11")
        browser.find_element_by_css_selector(".second_block input.form-control.second").send_keys("Moscow city")

        browser.find_element_by_css_selector("button.btn").click();

        time.sleep(2)

        result = browser.find_element_by_tag_name("h1")
        assert "Congratulations! You have successfully registered!" == result.text

    finally:
        browser.quit()


def login_tests():
    pass_only_name()
    pass_only_last_name()
    pass_only_email()
    empty_login()

    positive_login()
    login_with_all_fields()


login_tests()