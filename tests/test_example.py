from unittest import TestCase


class FakeTest(TestCase):
    def test_fake(self) -> None:
        self.assertEqual(1, 1)
