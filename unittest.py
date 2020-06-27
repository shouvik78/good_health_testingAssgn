from unittest.mock import patch, mock_open
import json

class TestMyFunctions(unittest.TestCase):


@patch("builtins.open", new_callable=mock_open,
       read_data=json.dumps({'username' : 'Shouvik','email' : 'shouvikghosh206@gmail.com',
                        'password' : 'shouvik123','contact' : '7541064484'}))
def test_read_file_data(self):
    expected_output = {
                  'username' : 'Shouvik',
                  'email' : 'shouvikghosh206@gmail.com',
                  'password' : 'shouvik123',
                  'contact' : '75410644'
                  }
    filename = 'test.json'
    actual_output = read_file_data(test.json, 'C:\\Users\\Shouvik\\Desktop\\Good Health')


    mock_file.assert_called_with(test.json)

    self.assertEqual(expected_output, actual_output)