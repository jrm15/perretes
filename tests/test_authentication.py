from unittest import TestCase
from api.authentication import create_access_token, get_user


class TestAuthentication(TestCase):

    def test_create_access_token(self):
        value = create_access_token(data={"sub": "prueba"}, expires_delta=30)
        print(value)

    def test_get_user(self):
        user = get_user("javi")
        print(user)
