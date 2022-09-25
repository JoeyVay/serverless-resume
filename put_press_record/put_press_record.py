import boto3
import uuid
import json
import datetime 
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('joevaycom-site-count')

def create_press_record(event,context):
	item={
			'ID': uuid.uuid4().hex,    #<<< chnage var name to new key
			'timestamp': datetime.utcnow().isoformat(),
			'source': 'https://joevay.com/SiteCount.html'
			#'note': 'This is the start of a new era for the button project!'
	}
	table.put_item(Item = item)
	return {
		"statusCode" : 200,
		"headers": {
			"Access-Control-Allow-Origin": "*",
			"Access-Control-Allow-Headers": "*",
			"Access-Control-Allow-Credentials": "*",    #<<<tighten all of these CORS policies
			"Content-Type": "application/json"
		},
		"body": json.dumps(item)
	}