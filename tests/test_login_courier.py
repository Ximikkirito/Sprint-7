import allure
import pytest

from data.courier_data import CourierData
from data.messages import Messages
from methods.courier_methods import CourierMethods


@allure.epic("Courier")
@allure.feature("Login courier")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, courier):

        courier_data, _ = courier

        response = CourierMethods.login(
            CourierData.login_data(courier_data)
        )

        with allure.step("Проверить код ответа"):
            assert response.status_code == 200

        with allure.step("Проверить наличие id"):
            assert "id" in response.json()

    @allure.title("Авторизация без логина")
    @pytest.mark.parametrize(
        "payload",
        [
            CourierData.login_without_login(CourierData.valid_courier()),
            CourierData.login_without_password(CourierData.valid_courier())
        ]
    )
    def test_login_without_required_fields(self, payload):

        response = CourierMethods.login(payload)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 400

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.LOGIN_REQUIRED

    @allure.title("Авторизация с неверным логином")
    def test_login_wrong_login(self, courier):

        courier_data, _ = courier

        response = CourierMethods.login(
            CourierData.wrong_login(courier_data)
        )

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND

    @allure.title("Авторизация с неверным паролем")
    def test_login_wrong_password(self, courier):

        courier_data, _ = courier

        response = CourierMethods.login(
            CourierData.wrong_password(courier_data)
        )

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND

    @allure.title("Авторизация несуществующего курьера")
    def test_login_nonexistent_courier(self):

        response = CourierMethods.login(
            CourierData.nonexistent_login()
        )

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND