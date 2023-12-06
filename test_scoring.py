import unittest

def calculate_frame_score(first, second, third=None):
    if first < 0 or second < 0 or first + second > 10:
        raise ValueError("Invalid input: Pins must be between 0 and 10.")
    
    if third is not None:
        return first + second + third
    
    return first + second

def get_perfect_game_frames():
    frames = [[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 10, 10]]
    return frames


class TestBowlingScoring(unittest.TestCase):

    def test_strike_score(self):
        # Arrange
        first_throw = 10  
        second_throw = 0

        # Act
        score = calculate_frame_score(first_throw, second_throw)

        # Assert
        self.assertEqual(score, 10)


    def test_spare_score(self):
        # Arrange
        first_throw = 5
        second_throw = 5

        # Act  
        score = calculate_frame_score(first_throw, second_throw)

        # Assert
        self.assertEqual(score, 10)

    def test_open_frame_score(self):
        # Arrange
        first_throw = 3
        second_throw = 4

        # Act
        score = calculate_frame_score(first_throw, second_throw)

        # Assert
        self.assertEqual(score, 7)

    def test_invalid_input(self):
        # Arrange
        first_throw = 11
        second_throw = 0

        # Act & Assert
        with self.assertRaises(ValueError):
            calculate_frame_score(first_throw, second_throw)
        

    def test_strike_on_first_ball(self):
        # Arrange
        first_throw = 10  
        second_throw = 0
        third_throw = 0

        # Act
        score = calculate_frame_score(first_throw, second_throw, third_throw)

        # Assert
        self.assertEqual(score, 10)

    def test_spare_on_first_two_balls(self):
        # Arrange
        first_throw = 5 
        second_throw = 5
        third_throw = 0

        # Act
        score = calculate_frame_score(first_throw, second_throw, third_throw)

        # Assert
        self.assertEqual(score, 10)

    def test_total_of_three_balls(self):
        # Arrange
        first_throw = 3
        second_throw = 4 
        third_throw = 3

        # Act
        score = calculate_frame_score(first_throw, second_throw, third_throw)

        # Assert
        self.assertEqual(score, 10)
    
    def test_miss_frame_score(self):

        # Arrange 
        first_throw = 0
        second_throw = 0

        # Act
        score = calculate_frame_score(first_throw, second_throw)  

        # Assert
        self.assertEqual(score,0)


if __name__ == '__main__':
    unittest.main()

