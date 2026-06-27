import allure

from data.courier_data import CourierData
from data.messages import Messages
from methods.courier_methods import CourierMethods


@allure.epic("Courier")
@allure.feature("Create courier")
class TestCreateCourier:

    @staticmethod
    def delete_created_courier(courier):
        login_response = CourierMethods.login(
            CourierData.login_data(courier)
        )

        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            CourierMethods.delete(courier_id)

    @allure.title("Создание нового курьера")
    def test_create_courier_success(self):

        courier = CourierData.valid_courier()

        with allure.step("Создать курьера"):
            response = CourierMethods.create_courier(courier)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 201

        with allure.step("Проверить тело ответа"):
            assert response.json() == Messages.CREATED

        self.delete_created_courier(courier)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):

        courier = CourierData.valid_courier()

        CourierMethods.create_courier(courier)

        response = CourierMethods.create_courier(courier)

        assert response.status_code == 409
        assert response.json()["message"] == Messages.LOGIN_ALREADY_EXISTS

        self.delete_created_courier(courier)

    @allure.title("Создание курьера без логина")
    def test_create_without_login(self):

        response = CourierMethods.create_courier(
            CourierData.without_login()
        )

        assert response.status_code == 400
        assert response.json()["message"] == Messages.NOT_ENOUGH_DATA

    @allure.title("Создание курьера без пароля")
    def test_create_without_password(self):

        response = CourierMethods.create_courier(
            CourierData.without_password()
        )

        assert response.status_code == 400
        assert response.json()["message"] == Messages.NOT_ENOUGH_DATA

    @allure.title("Создание курьера без имени")
    def test_create_without_first_name(self):

        response = CourierMethods.create_courier(
            CourierData.without_first_name()
        )

        assert response.status_code == 201

        courier = CourierData.without_first_name()
        self.delete_created_courier(courier)

    @allure.title("Создание существующего логина")
    def test_create_existing_login(self):

        courier = CourierData.valid_courier()

        CourierMethods.create_courier(courier)

        response = CourierMethods.create_courier(courier)

        assert response.status_code == 409
        assert response.json()["message"] == Messages.LOGIN_ALREADY_EXISTS

        self.delete_created_courier(courier)