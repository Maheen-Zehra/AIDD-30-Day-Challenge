import pytest
from src.calculator.parser import parse_expression

def test_parse_simple_addition():
    assert parse_expression("1+2") == ([1, 2], ['+'])

def test_parse_simple_subtraction():
    assert parse_expression("5-3") == ([5, 3], ['-'])

def test_parse_simple_multiplication():
    assert parse_expression("2*4") == ([2, 4], ['*'])

def test_parse_simple_division():
    assert parse_expression("10/2") == ([10, 2], ['/'])

def test_parse_multiple_operations():
    assert parse_expression("1+2-3") == ([1, 2, 3], ['+', '-'])

def test_parse_floating_point_numbers():
    assert parse_expression("1.5+2.5") == ([1.5, 2.5], ['+'])

def test_parse_negative_numbers():
    assert parse_expression("-1+2") == ([-1, 2], ['+'])

def test_parse_expression_with_spaces():
    assert parse_expression("1 + 2") == ([1, 2], ['+'])

def test_parse_invalid_character():
    with pytest.raises(ValueError, match="Invalid character in expression"):
        parse_expression("1$2")

def test_parse_invalid_operator_sequence():
    with pytest.raises(ValueError, match="Invalid character in expression"):
        parse_expression("1++2")
