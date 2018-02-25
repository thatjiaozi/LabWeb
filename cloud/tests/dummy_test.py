import unittest

class DummyTest(unittest.TestCase):
    """
        Dummy unittest just to prove that the testing infrastructure works
    """

    def testDummyTestCase(self):
        self.assertEqual(2,2)

if __name__ == '__main__':
    unittest.main()
