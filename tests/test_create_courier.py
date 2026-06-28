import allure
import pytest

from data.courier_data import CourierData
from data.messages import Messages
from methods.courier_methods import CourierMethods


@allure.epic("Courier")
@allure.feature("Create courier")
class TestCreateCourier:

    @allure.title("Создание нового курьера")
    def test_create_courier_success(self, new_courier):

        response = CourierMethods.create_courier(new_courier)

        with allure.step("Проверить статус код"):
            assert response.status_code == 201

        with allure.step("Проверить тело ответа"):
            assert response.json() == Messages.CREATED

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, courier):

        courier_data, _ = courier

        response = CourierMethods.create_courier(courier_data)

        with allure.step("Проверить статус код"):
            assert response.status_code == 409

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.LOGIN_ALREADY_EXISTS

    @allure.title("Создание курьера без обязательных полей")
    @pytest.mark.parametrize(
        "courier_data",
        [
            CourierData.without_login(),
            CourierData.without_password()
        ]
    )
    def test_create_without_required_fields(self, courier_data):

        response = CourierMethods.create_courier(courier_data)

        with allure.step("Проверить статус код"):
            assert response.status_code == 400

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.NOT_ENOUGH_DATA

    @allure.title("Создание курьера без имени")
    def test_create_without_first_name(self):

        courier = CourierData.without_first_name()

        response = CourierMethods.create_courier(courier)

        with allure.step("Проверить статус код"):
            assert response.status_code == 201

        with allure.step("Проверить тело ответа"):
            assert response.json() == Messages.CREATED

    @allure.title("Создание курьера с существующим логином")
    def test_create_existing_login(self, courier):

        courier_data, _ = courier

        response = CourierMethods.create_courier(courier_data)

        with allure.step("Проверить статус код"):
            assert response.status_code == 409

        with allure.step("Проверить сообщение"):
            assert response.json()["message"] == Messages.LOGIN_ALREADY_EXISTS