import allure

from data.messages import Messages
from methods.order_methods import OrderMethods


@allure.epic("Order")
@allure.feature("Accept order")
class TestAcceptOrder:

    @allure.title("Успешное принятие заказа")
    def test_accept_order_success(self, courier, order):

        _, courier_id = courier

        order_response = OrderMethods.get_order_by_track(order)

        order_id = order_response.json()["order"]["id"]

        response = OrderMethods.accept_order(
            order_id,
            courier_id
        )

        with allure.step("Проверить код ответа"):
            assert response.status_code == 200

        with allure.step("Проверить тело ответа"):
            assert response.json() == Messages.ORDER_ACCEPTED

    @allure.title("Принятие заказа без id курьера")
    def test_accept_order_without_courier_id(self, order):

        order_response = OrderMethods.get_order_by_track(order)

        order_id = order_response.json()["order"]["id"]

        response = OrderMethods.accept_order(
            order_id,
            ""
        )

        with allure.step("Проверить код ответа"):
            assert response.status_code == 400

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.COURIER_ID_REQUIRED

    @allure.title("Принятие заказа с неверным id курьера")
    def test_accept_order_wrong_courier_id(self, order):

        order_response = OrderMethods.get_order_by_track(order)

        order_id = order_response.json()["order"]["id"]

        response = OrderMethods.accept_order(
            order_id,
            999999999
        )

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить наличие сообщения"):
            assert "message" in response.json()

    @allure.title("Принятие заказа без id заказа")
    def test_accept_order_without_order_id(self, courier):

        _, courier_id = courier

        response = OrderMethods.accept_order(
            "",
            courier_id
        )

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить наличие сообщения"):
            assert "message" in response.json()

    @allure.title("Принятие заказа с неверным id заказа")
    def test_accept_order_wrong_order_id(self, courier):

        _, courier_id = courier

        response = OrderMethods.accept_order(
            999999999,
            courier_id
        )

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.ORDER_NOT_FOUND