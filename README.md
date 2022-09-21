# Serverless Resume API
SAM app that uses AWS to host a personal JOSN resume API.

## Need to Know:
### /template.yaml
- is the main cofig file used to describe infostructure used by the API, including the API Gateway that will need to be created, each endpoint for the API and the lambda function it calls, and finally the permissions applied to the Execution Role used.
-resume is pulled directly from s3 and the execution role has an inline policy that grants explicit permission to the individual file.

## Endpoints:
### /resume/json
- returns the resume in a JSON format

Notes:
- As I do not use Route 53 as a registrar, if the Hosted Zone holding my DNS records is blown away and recreated then I will need to go to NameCheep andter my enter the new nameservers created. 