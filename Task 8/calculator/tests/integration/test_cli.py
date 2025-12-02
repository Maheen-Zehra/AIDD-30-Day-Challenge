import pytest
from unittest.mock import patch
from src.calculator.main import main

@patch('builtins.input', side_effect=["5+3"])
@patch('builtins.print')
def test_cli_simple_addition(mock_print, mock_input):
    main()
    mock_print.assert_called_with("Result: 8.0")

@patch('builtins.input', side_effect=["10-4"])
@patch('builtins.print')
def test_cli_simple_subtraction(mock_print, mock_input):
    main()
    mock_print.assert_called_with("Result: 6.0")

@patch('builtins.input', side_effect=["6*7"])
@patch('builtins.print')
def test_cli_simple_multiplication(mock_print, mock_input):
    main()
    mock_print.assert_called_with("Result: 42.0")

@patch('builtins.input', side_effect=["20/4"])
@patch('builtins.print')
def test_cli_simple_division(mock_print, mock_input):
    main()
    mock_print.assert_called_with("Result: 5.0")

@patch('builtins.input', side_effect=["10/0"])
@patch('builtins.print')
def test_cli_division_by_zero(mock_print, mock_input):
    main()
    mock_print.assert_called_with("Error: Division by zero")

@patch('builtins.input', side_effect=["5++3"])
@patch('builtins.print')
def test_cli_invalid_expression_sequence(mock_print, mock_input):
    main()
    mock_print.assert_called_with("Error: Invalid character in expression")

@patch('builtins.input', side_effect=["hello"])
@patch('builtins.print')
def test_cli_invalid_expression_characters(mock_print, mock_input):
    main()
    mock_print.assert_called_with("Error: Invalid character in expression")

