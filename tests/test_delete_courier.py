import allure

from data.messages import Messages
from methods.courier_methods import CourierMethods


@allure.epic("Courier")
@allure.feature("Delete courier")
class TestDeleteCourier:

    @allure.title("Успешное удаление курьера")
    def test_delete_courier_success(self, courier):

        _, courier_id = courier

        response = CourierMethods.delete(courier_id)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 200

        with allure.step("Проверить тело ответа"):
            assert response.json() == Messages.COURIER_DELETED

    @allure.title("Удаление курьера без id")
    def test_delete_courier_without_id(self):

        response = CourierMethods.delete("")

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить наличие сообщения"):
            assert "message" in response.json()

    @allure.title("Удаление курьера с неверным id")
    def test_delete_courier_wrong_id(self):

        response = CourierMethods.delete(999999999)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND