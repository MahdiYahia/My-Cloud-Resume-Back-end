import os
import boto3
import pytest
import json
from moto import mock_dynamodb
from lambda_function import lambda_handler

# Data to be stored in the mock table
@pytest.fixture 
def initial_data():
    initial_data = {
        'ID': '1',
        'visitor_counter': 0
    }
    return initial_data
# Creating a DynamoDB mock table with initial data
@pytest.fixture 
def call_mock_table():
    @mock_dynamodb
    def dynamodb_mock(initial_data):
        dynamodb = boto3.resource('dynamodb')
        dynamodb_mock_table = dynamodb.create_table(
            TableName = 'counterUpdater',
            KeySchema = [
                {
                    'AttributeName': 'ID',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions = [
                {
                    'AttributeName': 'ID',
                    'AttributeType': 'S'
                }
            ],
            BillingMode = 'PAY_PER_REQUEST'
        )

        dynamodb_mock_table.put_item(Item=initial_data)

        return dynamodb
    return mock_dynamodb

os.environ['TABLE_NAME'] = 'counterUpdater'

# Testing the receipt of a response
@mock_dynamodb
def valid_lambda_response(call_mock_table, intial_data):
    call_mock_table(initial_data)
    response = lambda_handler(None, None)

    assert response != None

#Testing the increment of the counter by one 
@mock_dynamodb
def counter_increment(call_mock_table, initial_data):
    call_mock_table(initial_data)
    before_response = lambda_handler(None, None)
    before_count = int(json.loads(before_response['body'])['visitor_counter'])

    after_response = lambda_handler(None, None)
    after_count = int(json.loads(after_response['body'])['visitor_counter'])

    assert (after_count - before_count) == 1 
