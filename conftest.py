import pytest

from data.courier_data import CourierData
from data.order_data import OrderData
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture
def courier():
    """
    Создает курьера перед тестом
    и удаляет после выполнения теста.
    """

    courier_data = CourierData.valid_courier()

    CourierMethods.create_courier(courier_data)

    login_response = CourierMethods.login(
        CourierData.login_data(courier_data)
    )

    courier_id = login_response.json()["id"]

    yield courier_data, courier_id

    # Если курьер уже удален в тесте,
    # API просто вернет ошибку, которая нам здесь не мешает.
    CourierMethods.delete(courier_id)


@pytest.fixture
def order():
    """
    Создает заказ перед тестом
    и отменяет после выполнения теста.
    """

    payload = OrderData.ORDER.copy()

    response = OrderMethods.create_order(payload)

    track = response.json()["track"]

    yield track

    OrderMethods.cancel_order(track)