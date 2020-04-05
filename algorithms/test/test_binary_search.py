from algorithms.binary_search_or_half_interval_search import guess_secret_number
import unittest


class TestGetSecretNumber(unittest.TestCase):

    def test_guessed_first_number_from_list(self):
        self.assertEqual(guess_secret_number([x for x in range(0, 101)], 0), 0)

    def test_guessed_last_number_from_list(self):
        self.assertEqual(guess_secret_number([x for x in range(0, 101)], 100), 100)

    def test_guessed_middle_number_from_list(self):
        self.assertEqual(guess_secret_number([x for x in range(0, 101)], 50), 50)

    def test_guessed_non_existing_number_from_list(self):
        self.assertEqual(guess_secret_number([x for x in range(0, 101)], 500), None)

    def test_guessed_number_from_one_element_list(self):
        self.assertEqual(guess_secret_number([5], 5), 5)


if __name__ == "main":
    unittest.main()

