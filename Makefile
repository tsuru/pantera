clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -qr requirements.txt --use-mirrors

test-deps:
	@pip install -qr test-requirements.txt --use-mirrors

test: test-deps clean
	@nosetests --with-coverage --cover-package=pantera --with-xunit -s .
	@find . -name \*.py | xargs flake8
