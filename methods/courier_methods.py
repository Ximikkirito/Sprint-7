import allure
import requests

from urls import (
    CREATE_COURIER,
    LOGIN_COURIER,
    DELETE_COURIER
)


class CourierMethods:

    @staticmethod
    @allure.step("Создать курьера")
    def create_courier(payload):
        return requests.post(
            CREATE_COURIER,
            data=payload
        )

    @staticmethod
    @allure.step("Авторизовать курьера")
    def login(payload):
        return requests.post(
            LOGIN_COURIER,
            data=payload
        )

    @staticmethod
    @allure.step("Удалить курьера")
    def delete(courier_id):
        return requests.delete(
            f"{DELETE_COURIER}{courier_id}"
        )