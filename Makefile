.PHONY: test
deps:
		pip install -r requirements.txt; \
		pip install -r test_requirements.txt

lint:
		flake8 hello_world test


test:
	PYTHONPATH=. py.test

run:
		python main.py
docker_build:
	sudo docker build -t hello_world_printer .
