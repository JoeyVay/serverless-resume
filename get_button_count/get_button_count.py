import json
import boto3

#set table name
table_name = 'joevaycom-site-count'

#make DynamoDB client
visitor_count_dynamodb_client = boto3.client('dynamodb')

#set key to retrive
current_visitor_count_get = {'ID':{'S':'visitors'}}

def return_count(event,context):
    
    #request current count of viewers from db
    response = visitor_count_dynamodb_client.get_item(TableName = table_name, Key = current_visitor_count_get)

    #parse out and store vlaue
    current_visitor_count = response['Item']['count']['N']

    return {
        "statusCode" : 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Credentials": "*",    #<<<tighten all of these CORS policies
            "Content-Type": "application/json"
        },
        "body": "{ \"count\": \"" + current_visitor_count + "\" }"
    }