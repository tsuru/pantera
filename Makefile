clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -qr requirements.txt

test-deps:
	@pip install -qr test-requirements.txt

test: test-deps clean
	@nosetests --with-coverage --cover-package=pantera --with-xunit -s .
	@find . -name \*.py | xargs flake8
