from common.base_page import *
from common.file_reader import *


class TestValidTransaction(BasePage, unittest.TestCase):
    unique_id = None
    response_data = None

    def test_01_valid_payment_transaction(self):
        data = FileReader.json_reader('../tests_api_data/test_valid_payment_transaction.json')
        response = self.api_requests(json_data=data, request_type='POST')
        self.response_data = (json.loads(response.text))
        self.__class__.unique_id = self.response_data["unique_id"]
        # Creating data structure to compare with the data from verification response
        self.__class__.response_data = {f'status: {self.response_data["status"]}, '
                                        f'usage: {self.response_data["usage"]}, '
                                        f'amount: {self.response_data["amount"]}, '
                                        f'message: Your transaction has been voided successfully'}

        self.assertEqual(200, response.status_code, 'Different status code than expected!')

    def test_02_verify_valid_payment_transaction(self):
        # Creating verification request structure and passing unique_id
        verification_req = {
            "payment_transaction": {
                "reference_id": self.__class__.unique_id,
                "transaction_type": "void"
            }
        }

        response_verification = self.api_requests(json_data=verification_req, request_type='POST')

        self.assertEqual(200, response_verification.status_code, 'Different status code than expected!')

        response_verification_data = (json.loads(response_verification.text))
        # Data structure for verification response
        response_verification_data = {f'status: {response_verification_data["status"]}, '
                                      f'usage: {response_verification_data["usage"]}, '
                                      f'amount: {response_verification_data["amount"]}, '
                                      f'message: {response_verification_data["message"]}'}
        # Comparing the expected and actual data
        self.assertEqual(self.__class__.response_data, response_verification_data,
                         "Verification data is different than expected!")


if __name__ == "__main__":
    unittest.main()
