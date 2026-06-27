import requests

from urls import (
    BASE_URL,
    CREATE_COURIER,
    LOGIN_COURIER,
    DELETE_COURIER
)


class CourierMethods:

    @staticmethod
    def create_courier(payload):
        return requests.post(
            f'{BASE_URL}{CREATE_COURIER}',
            data=payload
        )

    @staticmethod
    def login(payload):
        return requests.post(
            f'{BASE_URL}{LOGIN_COURIER}',
            data=payload
        )

    @staticmethod
    def delete(courier_id):
        return requests.delete(
            f'{BASE_URL}{DELETE_COURIER}{courier_id}'
        )