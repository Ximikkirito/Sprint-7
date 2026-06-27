import allure
import pytest

from data.order_data import OrderData
from methods.order_methods import OrderMethods


@allure.epic("Order")
@allure.feature("Create order")
class TestCreateOrder:

    @allure.title("Создание заказа с разными цветами")
    @pytest.mark.parametrize(
        "color",
        [
            OrderData.BLACK,
            OrderData.GREY,
            OrderData.BOTH,
            OrderData.WITHOUT_COLOR
        ]
    )
    def test_create_order_with_different_colors(self, color):

        payload = OrderData.ORDER.copy()
        payload["color"] = color

        with allure.step("Создать заказ"):
            response = OrderMethods.create_order(payload)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 201

        with allure.step("Проверить наличие track"):
            assert "track" in response.json()