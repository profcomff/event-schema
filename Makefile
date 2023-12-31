configure: venv
	source ./venv/bin/activate && pip install -r requirements.dev.txt

venv:
	python3.11 -m venv venv

format:
	autoflake -r --in-place --remove-all-unused-imports ./event_schema
	isort ./event_schema
	black ./event_schema


