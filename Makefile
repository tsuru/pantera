clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt --use-mirrors

test: deps clean
	@nosetests --with-coverage --cover-package=pantera -s .
