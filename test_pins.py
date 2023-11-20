import unittest
from unittest.mock import patch
from io import StringIO
import sys
from bowling import print_pins

class TestPins(unittest.TestCase):
    def test_print_pins(self):
        expected_output = (
            "          1         \n"
            "         2 3        \n"
            "        4 5 6       \n"
            "       7 8 9 10     \n"
            "___________________\n"
            "|░░|░░|░░|░░|\n"
            "| |░░|░░|░░| |\n"
            "| | |░░|░░| | |\n"
            "| | | |░░| | | |\n"
            "|_|_|_|_|_|_|_|_|\n\n"
        )

        captured_output = StringIO()
        sys.stdout = captured_output

        print_pins(0)

        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()


