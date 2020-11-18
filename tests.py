import unittest

from auth import check_login


class TestLoginChecker(unittest.TestCase):

    def test_login(self):
        ValidLogin1 = 'aaddfs.-dfgd43qqw'
        ValidLogin2 = 'aaddfs.-dfgd43q22'
        WrongLogin1 = '2addfs.-dfgd43q22'
        WrongLogin2 = 'Addfs.-dfgd43q22'
        LongLogin2 = 'Addfs.-dfgd43q22aalalalllalal'
        MissedSymbol = 'aaddfs3dfgd43qa'

        self.assertTrue(check_login(ValidLogin1))
        self.assertTrue(check_login(ValidLogin2))
        self.assertFalse(check_login(WrongLogin1))
        self.assertFalse(check_login(WrongLogin2))
        self.assertFalse(check_login(LongLogin2))
        self.assertFalse(check_login(MissedSymbol))


if __name__ == '__main__':
    unittest.main()
