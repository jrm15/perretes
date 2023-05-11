from unittest import TestCase
from unittest.mock import patch
from api.exceptions import NotExistItemBD, ErrorAlterItemDB
from fastapi.testclient import TestClient
from api.models.user import User
import os


class TestSite(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        os.environ["MODE"] = "TEST"
        from api.main import app

        cls.client = TestClient(app)

    @patch("api.models.user.User.get_all")
    def test_get_all_users(self, mock_get_all):
        mock_get_all.return_value = [
            User(
                id=1,
                name="Marta",
                password="assd"
            ),
            User(
                id=2,
                name="Javi",
                password="assd"
            )]

        expected_user = [
            {
                "id": 1,
                "name": "Marta",
                "password": "assd"
            },
            {
                "id": 2,
                "name": "Javi",
                "password": "assd"
            }
        ]

        response = self.client.get("/user")

        self.assertEqual(response.json(), expected_user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_get_all.call_count, 1)

    @patch("api.models.user.User.get_id")
    def test_get_user(self, mock_get_user):
        mock_get_user.return_value = User(
            id=1,
            name="Marta",
            password="assd"
        )
        expected_user = {
            "id": 1,
            "name": "Marta",
            "password": "assd"
        }

        response = self.client.get("/user/1")

        self.assertEqual(response.json(), expected_user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_get_user.call_count, 1)

    @patch("api.models.user.User.get_id")
    def test_get_user_error_item_bd(self, mock_get_user):
        mock_get_user.side_effect = NotExistItemBD("Site 1 not found")
        expected = {"detail": "Not Found"}

        response = self.client.get("/site/1")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), expected)
        self.assertEqual(mock_get_user.call_count, 0)



