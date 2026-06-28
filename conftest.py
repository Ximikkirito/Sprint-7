import pytest

from data.courier_data import CourierData
from data.order_data import OrderData
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture
def courier():
    """
    Создает курьера перед тестом и удаляет после выполнения теста.
    Возвращает (данные_курьера, id_курьера).
    """

    courier_data = CourierData.valid_courier()

    CourierMethods.create_courier(courier_data)

    courier_id = None

    login_response = CourierMethods.login(
        CourierData.login_data(courier_data)
    )

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]

    yield courier_data, courier_id

    if courier_id is not None:
        CourierMethods.delete(courier_id)


@pytest.fixture
def new_courier():
    """
    Возвращает данные нового курьера.
    После теста удаляет его, если он был успешно создан.
    """

    courier_data = CourierData.valid_courier()

    yield courier_data

    login_response = CourierMethods.login(
        CourierData.login_data(courier_data)
    )

    if login_response.status_code == 200:
        CourierMethods.delete(login_response.json()["id"])


@pytest.fixture
def order():
    """
    Создает заказ и возвращает track.
    """

    payload = OrderData.ORDER.copy()

    response = OrderMethods.create_order(payload)

    yield response.json()["track"]