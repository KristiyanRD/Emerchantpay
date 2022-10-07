from common.base_page import *
from common.file_reader import *


class TestInvalidAuthentication(BasePage, unittest.TestCase):

    def test_01_invalid_authentication(self):
        data = FileReader.json_reader('../tests_api_data/test_valid_payment_transaction.json')
        response = self.api_requests(json_data=data, request_type='POST', auth_user='wronglogin', auth_password='wrongpwd')
        self.assertEqual(401, response.status_code, 'Different status code than expected!')


if __name__ == "__main__":
    unittest.main()
