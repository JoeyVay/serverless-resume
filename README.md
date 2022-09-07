# Serverless Resume API
This is small appliction made using the AWS Serverless Application Model (SAM) to deply and run a serverless API to deliver my personal resume in a JOSN format. 

## Need to Know:
### /template.yaml
- is the main cofig file used to describe infostructure used by the API, including the API Gateway that will need to be created, each endpoint for the API and the lambda function it calls, and finally the permissions applied to the Execution Role used.
-resume is pulled directly from s3 and the execution role has an inline policy that grants explicit permission to the individual file.

## Endpoints:
### /resume/json
- returns the resume in a JSON format
