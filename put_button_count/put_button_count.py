import boto3

dynamodb = boto3.resource('dynamodb', region_name= 'us-east-1')
table = dynamodb.Table('joevay-button-press-count')
key = {'id': 'presses'}

def increment_count(event,context):
	#update count
	response = table.update_item(
		Key = key,
		ExpressionAttributeNames = {'#count': 'count'},
		ExpressionAttributeValues = {':increase': 1,},
		UpdateExpression = 'ADD #count :increase',
		ReturnValues = 'UPDATED_NEW'
	)

	#store returned incremented count
	current_count = (response['Attributes']['count'])

	return {
		"statusCode" : 200,
		"headers": {
			"Access-Control-Allow-Origin": "*",
			"Access-Control-Allow-Headers": "*",
			"Access-Control-Allow-Credentials": "*",    #<<<tighten all of these CORS policies
			"Content-Type": "application/json"
		},
		"body": "{ \"count\": \"" + str(current_count) + "\" }"
    }