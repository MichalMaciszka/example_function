import pytest
from unittest.mock import patch
from io import StringIO
import example
import importlib

@pytest.fixture(autouse=True)
def reset_example_module():
    # Reset the function's shared list before each test
    importlib.reload(example)

@patch('sys.stdout', new_callable=StringIO)
def test_single_call_with_default(mock_stdout):
    # Test a single call to the function with the default list
    example.example_function(1)
    assert mock_stdout.getvalue().strip() == "[1]"

@patch('sys.stdout', new_callable=StringIO)
def test_multiple_calls_with_default(mock_stdout):
    # Test multiple calls to demonstrate shared state
    example.example_function(2)
    example.example_function(3)
    assert mock_stdout.getvalue().strip() == "[2]\n[2, 3]"

@patch('sys.stdout', new_callable=StringIO)
def test_provided_list_is_not_affected(mock_stdout):
    # Test that providing a list avoids the shared state problem
    custom_list = [10, 20]
    example.example_function(30, custom_list)
    assert mock_stdout.getvalue().strip() == "[10, 20, 30]"

@patch('sys.stdout', new_callable=StringIO)
def test_provided_list_multiple_two_lists(mock_stdout):
    # Test that shows when we provide two lists there's no shared state problem
    custom_list = [10, 20]
    custom_list2 = [20, 30]
    example.example_function(30, custom_list)
    example.example_function(40, custom_list2)
    assert mock_stdout.getvalue().strip() == "[10, 20, 30]\n[20, 30, 40]"

@patch('sys.stdout', new_callable=StringIO)
def test_provided_list_multiple_one_list(mock_stdout):
    # Test that shows when we provide two calls with the same list both elements are added
    custom_list = [10, 20]
    example.example_function(30, custom_list)
    example.example_function(40, custom_list)
    assert mock_stdout.getvalue().strip() == "[10, 20, 30]\n[10, 20, 30, 40]"

@patch('sys.stdout', new_callable=StringIO)
def test_provided_empty_list_argument(mock_stdout):
    # Test that shows when we provide an empty list as argument the shared state problem is avoided
    example.example_function(30, [])
    example.example_function(40, [])
    assert mock_stdout.getvalue().strip() == "[30]\n[40]"