import json
import boto3

#set table name
table_name = 'joevaycom-site-count'

#make DynamoDB client
visitor_count_dynamodb_client = boto3.client('dynamodb')

#set key to retrive visitor count
current_visitor_count_get = {'ID':{'S':'visitors'}}

def lambda_handler(event,context):
    
    #request current count of viewers from db
    response = visitor_count_dynamodb_client.get_item(TableName = table_name, Key = current_visitor_count_get)

    #parse out and store value as a string
    current_visitor_count = response['Item']['count']['N']


    #current_visitor_count = int(current_visitor_count)
    #current_visitor_count = current_visitor_count + 1
    #current_visitor_count = str(current_visitor_count)
    current_visitor_count = str(int(current_visitor_count) + 1)

    #prepare new visitor count to be stored
    new_visitor_count = {
        'ID':{'S':'visitors'}
        ,'count':{'N':(current_visitor_count)}
    }

    #store updated item in db
    visitor_count_dynamodb_client.put_item(TableName = table_name, Item = (new_visitor_count))

    return {
        "statusCode" : 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Credentials": "*",    #<<<tighten all of these CORS policies
            "Content-Type": "application/json"
        },
        "body": "stored value: \"{ \"count\": \"" + (current_visitor_count) + "\" }\""
    }