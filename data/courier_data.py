from helpers.generator import generate_random_string


class CourierData:

    @staticmethod
    def valid_courier():
        return {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

    @staticmethod
    def duplicate_courier(courier):
        return courier.copy()

    @staticmethod
    def without_login():
        return {
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

    @staticmethod
    def without_password():
        return {
            "login": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

    @staticmethod
    def without_first_name():
        return {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }

    @staticmethod
    def login_data(courier):
        return {
            "login": courier["login"],
            "password": courier["password"]
        }

    @staticmethod
    def wrong_login(courier):
        return {
            "login": generate_random_string(10),
            "password": courier["password"]
        }

    @staticmethod
    def wrong_password(courier):
        return {
            "login": courier["login"],
            "password": generate_random_string(10)
        }

    @staticmethod
    def nonexistent_login():
        return {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }

    @staticmethod
    def login_without_login(courier):
        return {
            "password": courier["password"]
        }

    @staticmethod
    def login_without_password(courier):
        return {
            "login": courier["login"]
        }