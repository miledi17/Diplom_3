import pytest
import requests
from selenium import webdriver
from faker import Faker
from urls import Urls

fake = Faker()


@pytest.fixture(params=['chrome'])
def driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        browser = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {request.param}")

    browser.get(Urls.BASE_URL)

    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def create_user():
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }

    response = requests.post(Urls.REGISTER_USER, json=user_data)
    response_data = response.json()

    yield user_data, response_data, response.status_code

    access_token = response_data['accessToken']
    requests.delete(Urls.DELETE_USER, headers={'Authorization': access_token})