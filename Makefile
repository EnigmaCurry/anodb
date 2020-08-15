.ONESHELL:

.PHONY: check
check: venv
	. venv/bin/activate
	type python3
	mypy aiodb
	flake8 aiodb
	cd tests && pytest test-aiodb.py

.PHONY: clean
clean:
	$(RM) -r venv __pycache__ aiodb.egg-info dist build */__pycache__ .mypy_cache .pytest_cache

.PHONY: install
install:
	pip3 install -e .

venv:
	python3 -m venv venv
	venv/bin/pip3 install wheel ipython pytest pytest-postgresql psycopg2
	venv/bin/pip3 install -e .

dist:
	python3 setup.py sdist bdist_wheel

.PHONY: publish
publish: dist
	twine upload dist/*
