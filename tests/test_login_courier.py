import allure

from data.courier_data import CourierData
from data.messages import Messages
from methods.courier_methods import CourierMethods


@allure.epic("Courier")
@allure.feature("Login courier")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, courier):

        courier_data, _ = courier

        with allure.step("Авторизоваться"):
            response = CourierMethods.login(
                CourierData.login_data(courier_data)
            )

        with allure.step("Проверить код ответа"):
            assert response.status_code == 200

        with allure.step("Проверить наличие id"):
            assert "id" in response.json()

    @allure.title("Авторизация без логина")
    def test_login_without_login(self, courier):

        courier_data, _ = courier

        response = CourierMethods.login(
            CourierData.login_without_login(courier_data)
        )

        assert response.status_code == 400
        assert response.json()["message"] == Messages.LOGIN_REQUIRED

    @allure.title("Авторизация без пароля")
    def test_login_without_password(self, courier):

        courier_data, _ = courier

        response = CourierMethods.login(
            CourierData.login_without_password(courier_data)
        )

        assert response.status_code == 400
        assert response.json()["message"] == Messages.LOGIN_REQUIRED

    @allure.title("Авторизация с неверным логином")
    def test_login_wrong_login(self, courier):

        courier_data, _ = courier

        response = CourierMethods.login(
            CourierData.wrong_login(courier_data)
        )

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND

    @allure.title("Авторизация с неверным паролем")
    def test_login_wrong_password(self, courier):

        courier_data, _ = courier

        response = CourierMethods.login(
            CourierData.wrong_password(courier_data)
        )

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND

    @allure.title("Авторизация несуществующего курьера")
    def test_login_nonexistent_courier(self):

        response = CourierMethods.login(
            CourierData.nonexistent_login()
        )

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND