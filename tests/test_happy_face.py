import unittest

from mood_detection.detector import detect
from tests.variables import HAPPY


class TestCase(unittest.TestCase):
    def setUp(self):
        self.file = open(HAPPY, 'rb')
        super(TestCase, self).setUp()

    def test_happy_face(self):
        assert detect(self.file) == 'Happy!'

    def tearDown(self):
        self.file.close()
        super(TestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()
