import os
import boto3
import pytest
import json
from moto import mock_dynamodb


@pytest.fixture # Data to be stored in the mock table
def initial_data():
    initial_data = {
        'ID': '1',
        'visitor_counter': 0
    }
    return initial_data

@pytest.fixture # DynamoDB mock table with initial data
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

@mock_dynamodb
def valid_lambda_response(call_mock_table, intial_data):
    call_mock_table(initial_data)
    from lambda_update_view_count import lambda_handler
    response = lambda_handler(None, None)

    assert response != None

@mock_dynamodb
def counter_increment_and_(call_mock_table, initial_data):
    call_mock_table(initial_data)
    from lambda_update_view_count import lambda_handler
    before_count = lambda_handler(None, None)
    before_count = int(json.loads(before_response['body'])['visitor_counter'])

    after_response = lambda_handler(None, None)
    after_count = int(json.loads(after_response['body'])['visitor_counter'])

    assert after_count > before_count # Lambda function increments count & successfully saves it back to DB table
    assert (after_count - before_count) == 1 # Lambda function increments count by one
