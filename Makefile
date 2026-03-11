run:
	uvicorn ambient_assistant.main:app --host 0.0.0.0 --port 8000 --reload

install:
	pip install -r requirements.txt

test:
	pytest

lint:
	ruff .

format:
	black .
