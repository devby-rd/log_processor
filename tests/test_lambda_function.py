import pytest
from lambda_function import lambda_handler

def test_lambda_handler_with_empty_data():
    event = {}  # Example event data (can be more complex)
    context = {} #Example context
    expected_response = {
        "statusCode": 200,
        "body": {
            "candidate_id": '',
            "result": {
                'total_errors': 0,
                'unique_error_messages': []
            }
        } 
    }
    actual_response = lambda_handler(event, context)
    assert actual_response == expected_response

def test_lambda_handler_with_data():
    event = {
        "candidate_id": "YOUR_ID",
        "log_content": "[2024-01-07 10:15:30] ERROR: Database connection failed"
    }
    context = {}
    expected_response = {
        "statusCode": 200,
        "body": {
            "candidate_id": 'YOUR_ID',
            "result": {
                'total_errors': 1,
                'unique_error_messages': ['Database connection failed']
            }
        } 
    }
    actual_response = lambda_handler(event, context)
    assert actual_response == expected_response

def test_lambda_handler_invalid_json():
    event = {
        "candidate_id": "YOUR_ID",
        "log_content": {}
    }
    context = {}
    expected_response = {
        'statusCode': 400,
        'error': "An error occurred while processing the log file: 'dict' object has no attribute 'strip'"
    }
    actual_response = lambda_handler(event, context)
    assert actual_response == expected_response