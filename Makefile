deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test

.PHONY: test
test:
	PYTHONPATH=. py.test

run:
	python main.py
docker_build:
	sudo docker build -t hello-world-printer .

docker_run: docker_build
	sudo docker run \
	 	--name hello-world-printer-dev \
		-p 5000:5000 \
		-d hello-world-printer
