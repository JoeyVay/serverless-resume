import boto3
dynamodb = boto3.resource('dynamodb', region_name= 'us-east-1')
table = dynamodb.Table('joevaycom-site-count')

def lambda_handler(event,context):
    response = table.update_item(TableName='joevaycom-site-count', Key={'ID': 'visitors'},
        ExpressionAttributeNames = {'#count': 'count'},
        ExpressionAttributeValues = {':increase': 1,},
        #UpdateExpression = "SET #count = #count + :increase",
        UpdateExpression = 'ADD #count :increase',
        ReturnValues = 'UPDATED_NEW'
    )

    current_visitor_count = (response['Attributes']['count'])

    return {
        "statusCode" : 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Credentials": "*",    #<<<tighten all of these CORS policies
            "Content-Type": "application/json"
        },
        "body": "stored value: " + str(current_visitor_count)
    }