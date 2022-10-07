from common.base_page import *
from common.file_reader import *


class TestInvalidVoidTransaction(BasePage, unittest.TestCase):
    unique_id = None
    response_data = None

    def test_01_valid_payment_transaction(self):
        data = FileReader.json_reader('../tests_api_data/test_invalid_void_transaction.json')
        response = self.api_requests(json_data=data, request_type='POST')
        self.response_data = (json.loads(response.text))
        self.__class__.unique_id = self.response_data["unique_id"]
        # Creating data structure to compare with the data from verification response
        self.assertEqual(200, response.status_code, 'Different status code than expected!')

    def test_02_verify_invalid_void_transaction_with_wrong_transaction_type(self):
        # Creating verification request structure and passing unique_id
        verification_req = {
            "payment_transaction": {
                "reference_id": self.__class__.unique_id,
                "transaction_type": "none"
            }
        }

        response_verification = self.api_requests(json_data=verification_req, request_type='POST')

        self.assertEqual(422, response_verification.status_code, 'Different status code than expected!')

    def test_03_verify_invalid_void_transaction_with_wrong_reference_id(self):
        # Creating verification request structure and passing unique_id
        verification_req = {
            "payment_transaction": {
                "reference_id": 'none',
                "transaction_type": "void"
            }
        }

        response_verification = self.api_requests(json_data=verification_req, request_type='POST')

        self.assertEqual(422, response_verification.status_code, 'Different status code than expected!')


if __name__ == "__main__":
    unittest.main()
