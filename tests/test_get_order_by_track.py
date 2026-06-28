import allure

from data.messages import Messages
from methods.order_methods import OrderMethods


@allure.epic("Order")
@allure.feature("Get order by track")
class TestGetOrderByTrack:

    @allure.title("Получение заказа по track")
    def test_get_order_by_track_success(self, order):

        response = OrderMethods.get_order_by_track(order)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 200

        with allure.step("Проверить наличие заказа"):
            assert "order" in response.json()

    @allure.title("Получение заказа без track")
    def test_get_order_by_track_without_track(self):

        response = OrderMethods.get_order_by_track("")

        with allure.step("Проверить код ответа"):
            assert response.status_code == 400

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.TRACK_REQUIRED

    @allure.title("Получение заказа с неверным track")
    def test_get_order_by_track_wrong_track(self):

        response = OrderMethods.get_order_by_track(999999999)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.ORDER_NOT_FOUND