import random
import string

import requests

from urls import BASE_URL, CREATE_COURIER


def generate_random_string(length):
    """
    Генерирует случайную строку из строчных латинских букв.
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_courier_data():
    """
    Генерирует данные нового курьера.
    """
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }


def register_new_courier_and_return_login_password():
    """
    Регистрирует нового курьера.

    Возвращает:
        [login, password, first_name]
    либо пустой список, если регистрация не удалась.
    """
    courier = generate_courier_data()

    response = requests.post(
        f'{BASE_URL}{CREATE_COURIER}',
        data=courier
    )

    if response.status_code == 201:
        return [
            courier["login"],
            courier["password"],
            courier["firstName"]
        ]

    return []