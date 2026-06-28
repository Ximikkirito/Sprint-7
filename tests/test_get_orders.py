import allure

from methods.order_methods import OrderMethods


@allure.epic("Order")
@allure.feature("Get orders")
class TestGetOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):

        response = OrderMethods.get_orders()

        with allure.step("Проверить код ответа"):
            assert response.status_code == 200

        with allure.step("Проверить наличие списка заказов"):
            assert "orders" in response.json()