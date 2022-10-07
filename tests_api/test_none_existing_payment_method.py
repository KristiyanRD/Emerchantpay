from common.base_page import *
from common.file_reader import *


class TestNoneExistingPaymentTransaction(BasePage, unittest.TestCase):

    def test_01_valid_payment_transaction(self):
        data = FileReader.json_reader('../tests_api_data/test_nonexcisting_payment_transaction.json')
        response = self.api_requests(json_data=data, request_type='POST')
        self.response_data = (json.loads(response.text))

        self.assertEqual(422, response.status_code, 'Different status code than expected!')


if __name__ == "__main__":
    unittest.main()
