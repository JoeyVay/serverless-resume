# Serverless Resume API
SAM app that uses AWS to host a personal json resume API.

## Need to Know:
### /template.yaml
-is the main cofig file used to describe infostructure used by the API, including the API Gateway that will need to be created, each endpoint for the APi and the lambda fucntion it calls, and finally the permisisons applied to the role used by the Execution User.

## Endpoints:
### /resume/json
-returns the resume in a json format
