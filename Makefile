init:
	npm install --save serverless-python-requirements
	npm install --save serverless-plugin-bespoken
	pip install -r requirements.txt

virtualenv:
	mkvirtualenv -p python3 bolterbot
	workon bolterbot

deploy:
	sls deploy --stage production --region us-west-2

invoke:
	sls invoke local --function bolter --path tests/bolter.json
