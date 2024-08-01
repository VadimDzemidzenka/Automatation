import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""

@pytest.mark.parametrize("input_string, expected_output", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("123", "123"),
    ("", ""),
    ("", " "),
    ("12345тест", "12345тест"),
])
def test_capitalize(input_string, expected_output):
    assert utils.capitalize(input_string) == expected_output