.PHONY: build

build:
	sam build

deploy-infra:
	sam deploy

deploy-site:
	aws s3 sync ./resume-site s3://serverless-resume-site-bucket-joevay

invoke-get-view-count:
	sam build && sam local invoke GetSiteViewCountFunction

invoke-put-view-count:
	sam build && sam local invoke PutSiteViewCountFunction