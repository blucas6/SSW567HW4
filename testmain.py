import unittest


from main import grabUserRepos

class testMain(unittest.TestCase):
    def testMainForEmpty(self):
        self.assertEqual(grabUserRepos('', ''), -1, "Invalid input")
    
    def testMainForInvalid(self):
        self.assertEqual(grabUserRepos(-1, 98230129830), -1, "Invalid input")
    
    def testMainForInvalidUser(self):
        self.assertEqual(grabUserRepos("pppfpasdfdaspfpasddfpasdfpasd"), 404, 'User does not exist')

    def testMainForRepition(self):
        self.assertEqual(grabUserRepos('blucas6'), 403, 'Need to authenticate')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()