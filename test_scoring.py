import unittest

def calculate_frame_score(first_throw, second_throw):
    if first_throw < 0 or second_throw < 0 or first_throw + second_throw > 10:
        raise ValueError("Invalid input: Pins must be between 0 and 10.")
    frame_score = first_throw + second_throw
    return frame_score


class TestBowlingScoring(unittest.TestCase):
    def test_strike_score(self):
        self.assertEqual(calculate_frame_score(10, 0), 10)

    def test_spare_score(self):
        self.assertEqual(calculate_frame_score(5, 5), 10)
    
    def test_open_frame_score(self):
        self.assertEqual(calculate_frame_score(3, 4), 7 )

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_frame_score(11, 0)

if __name__ == '__main__':
    unittest.main()
