import boto3
import json

# Creating the low level functional client
client = boto3.client('s3')
S3_BUCKET = 'joevay.backpack' 
object_key = "json_resume_template.json"

def lambda_handler(event,context):
    
    file_content = client.get_object(Bucket=S3_BUCKET, Key=object_key)["Body"].read()
    reasume = json.loads(file_content)
    
    #print('Printing Resume JSON...')
    print(file_content)

    return {
        "statusCode" : 200,
        "body" : file_content
    }