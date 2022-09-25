.PHONY: build

build:
	sam build

deploy-infra:
	sam deploy

deploy-site:
	aws s3 sync ./resume-site s3://serverless-resume-site-bucket-joevay

invoke-get-button-count:
	sam build && sam local invoke GetButtonCountFunction

invoke-put-button-count:
	sam build && sam local invoke PutButtonCountFunction