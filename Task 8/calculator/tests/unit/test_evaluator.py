import pytest
from src.calculator.evaluator import evaluate_expression

def test_evaluate_addition():
    assert evaluate_expression([5, 3], ['+']) == 8

def test_evaluate_subtraction():
    assert evaluate_expression([10, 4], ['-']) == 6

def test_evaluate_multiplication():
    assert evaluate_expression([6, 7], ['*']) == 42

def test_evaluate_division():
    assert evaluate_expression([20, 4], ['/']) == 5

def test_evaluate_multiple_operations():
    assert evaluate_expression([1, 2, 3], ['+', '-']) == 0

def test_evaluate_floating_point_numbers():
    assert evaluate_expression([1.5, 2.5], ['+']) == 4.0

def test_evaluate_negative_numbers():
    assert evaluate_expression([-1, 2], ['+']) == 1

def test_evaluate_division_by_zero():
    with pytest.raises(ZeroDivisionError, match="Division by zero"):
        evaluate_expression([10, 0], ['/'])

