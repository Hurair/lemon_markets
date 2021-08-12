from datetime import datetime, timedelta
from unittest import TestCase

from service.app import create_app


class TestBase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.app = create_app()
        cls.client = cls.app.app.test_client()


class TestOrders(TestBase):

    @classmethod
    def setUpClass(cls):
        super(TestOrders, cls).setUpClass()

    def test_successful_order_post(self):
        request_body = {
            'isin': 'AMZN',
            'limit_price': 145.32,
            'quantity': 1,
            'side': 'buy',
            'valid_until':
                (datetime.now() + timedelta(days=2) - datetime(1970, 1, 1)).total_seconds()  # convert into epoch UTC
        }

        response = self.client.post('/orders', json=request_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, request_body)

    def test_invalid_time(self):
        utc_time = (datetime.now() - timedelta(days=2) - datetime(1970, 1, 1)).total_seconds()
        request_body = {
            'isin': 'MFST',
            'limit_price': 145.32,
            'quantity': 1,
            'side': 'buy',
            'valid_until': utc_time  # convert into epoch UTC
        }

        response = self.client.post('/orders', json=request_body)
        self.assertEqual(f"{utc_time} is not a valid time or not in future.", response.json.get('detail'))
        self.assertEqual(response.status_code, 400)

    def test_invalid_request_body(self):
        request_body = {
            'isin': 'thisshouldbegreaterthan12characters',
            'limit_price': 145,
            'quantity': 0,
            'side': 'Buy',
            'valid_until':
                (datetime.now() - timedelta(days=2) - datetime(1970, 1, 1)).total_seconds()  # convert into epoch UTC
        }

        response = self.client.post('/orders', json=request_body)
        self.assertEqual(response.status_code, 400)
