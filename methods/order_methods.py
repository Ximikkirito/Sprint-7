import allure
import requests

from urls import (
    CREATE_ORDER,
    GET_ORDERS,
    GET_ORDER_BY_TRACK,
    ACCEPT_ORDER
)


class OrderMethods:

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload):
        return requests.post(
            CREATE_ORDER,
            json=payload
        )

    @staticmethod
    @allure.step("Получить список заказов")
    def get_orders():
        return requests.get(GET_ORDERS)

    @staticmethod
    @allure.step("Получить заказ по треку")
    def get_order_by_track(track):
        return requests.get(
            GET_ORDER_BY_TRACK,
            params={
                "t": track
            }
        )

    @staticmethod
    @allure.step("Принять заказ")
    def accept_order(order_id, courier_id):
        return requests.put(
            f"{ACCEPT_ORDER}{order_id}",
            params={
                "courierId": courier_id
            }
        )