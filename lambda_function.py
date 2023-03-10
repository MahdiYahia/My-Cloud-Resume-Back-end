import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor_count')
def lambda_handler(event, context):
    response = table.get_item(Key={
            'ID':'1'
    })  
    visitor_counter = response['Item']['visitor_counter']
    visitor_counter = visitor_counter + 1
    print(visitor_counter)
    response = table.put_item(
        Item={
            'ID':'1',
            'visitor_counter': visitor_counter
    })
    return visitor_counter
