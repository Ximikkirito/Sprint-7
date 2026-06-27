import requests

from urls import (
    BASE_URL,
    CREATE_ORDER,
    GET_ORDERS,
    ACCEPT_ORDER,
    GET_ORDER_BY_TRACK
)


class OrderMethods:

    @staticmethod
    def create_order(payload):
        return requests.post(
            f'{BASE_URL}{CREATE_ORDER}',
            json=payload
        )

    @staticmethod
    def get_orders():
        return requests.get(
            f'{BASE_URL}{GET_ORDERS}'
        )

    @staticmethod
    def accept_order(order_id, courier_id):
        return requests.put(
            f'{BASE_URL}{ACCEPT_ORDER}{order_id}',
            params={
                "courierId": courier_id
            }
        )

    @staticmethod
    def get_order_by_track(track):
        return requests.get(
            f'{BASE_URL}{GET_ORDER_BY_TRACK}',
            params={
                "t": track
            }
        )

    @staticmethod
    def cancel_order(track):
        return requests.put(
            f'{BASE_URL}{CREATE_ORDER}/cancel',
            params={
                "track": track
            }
        )