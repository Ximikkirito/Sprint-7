import random
import string

import requests

from urls import BASE_URL, API


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }


def register_new_courier_and_return_login_password():
    courier = generate_courier_data()

    response = requests.post(
        f"{BASE_URL}{API}/courier",
        data=courier
    )

    if response.status_code == 201:
        return [
            courier["login"],
            courier["password"],
            courier["firstName"]
        ]

    return []