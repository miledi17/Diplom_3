import pytest
import requests
from selenium import webdriver
from faker import Faker
from urls import Urls
import time

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
    # Генерируем гарантированно уникальный email через временную метку
    timestamp = int(time.time() * 1000)  # Миллисекунды
    unique_email = f"user_{timestamp}@example.org"
    
    
    user_data = {
        "email": unique_email,
        "password": fake.password(length=12, special_chars=True, digits=True),
        "name": fake.name()
    }

    try:
        # Регистрация пользователя
        response = requests.post(
            Urls.REGISTER_USER,
            json=user_data,
            timeout=10
        )
        
        if response.status_code == 200:
            response_data = response.json()
            
            # Проверяем, что ответ содержит accessToken (признак успешной регистрации)
            if 'accessToken' in response_data:
                yield user_data, response_data, response.status_code
                
                # Очистка: удаляем пользователя после теста
                access_token = response_data['accessToken']
                requests.delete(
                    Urls.DELETE_USER,
                    headers={'Authorization': access_token},
                    timeout=5
                )
            else:
                pytest.fail(
                    f"Регистрация прошла, но нет accessToken. "
                    f"Ответ: {response_data}"
                )
        else:
            # Если регистрация не удалась — пытаемся понять причину
            error_msg = response.text
            try:
                error_json = response.json()
                error_msg = error_json.get('message', error_msg)
            except:
                pass
            pytest.fail(
                f"Ошибка регистрации. Статус: {response.status_code}, "
                f"Сообщение: {error_msg}"
            )
            
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Сетевая ошибка при регистрации: {str(e)}")
    except Exception as e:
        pytest.fail(f"Неожиданная ошибка: {str(e)}")