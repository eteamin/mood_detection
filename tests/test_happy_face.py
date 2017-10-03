import unittest

from mood_detection.detector import MoodDetector
from tests.variables import HAPPY


class TestCase(unittest.TestCase):

    def test_happy_face(self):
        detector = MoodDetector(HAPPY)
        assert detector.detect() == 'Happy!'


if __name__ == '__main__':
    unittest.main()
