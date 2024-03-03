import unittest
from unittest.mock import Mock, patch

from main import grabUserRepos

class testMain(unittest.TestCase):
    
    def testMainForEmpty(self):
        self.assertEqual(grabUserRepos('', ''), -1, "Invalid input")
    
    def testMainForInvalid(self):
        self.assertEqual(grabUserRepos(-1, 98230129830), -1, "Invalid input")
    
    @patch('requests.get')
    def testMainForInvalidUser(self, mock_get):
        mock_get.return_value.json.return_value = {}
        mock_get.return_value.status_code = 404
        res = grabUserRepos("pppfpasdfdaspfpasddfpasdfpasd")
        self.assertEqual(res, 404, 'User does not exist')

    @patch('requests.get')
    def testMainForRepition(self, mock_get):
        mock_get.return_value.json.return_value = {}
        mock_get.return_value.status_code = 403
        res = grabUserRepos('blucas6')
        self.assertEqual(res, 403, 'Need to authenticate')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()