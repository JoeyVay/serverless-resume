.PHONY: build

build:
	sam build

deploy-infra:
	sam deploy

deploy-site:
	aws s3 sync ./resume-site s3://serverless-resume-site-bucket-joevay