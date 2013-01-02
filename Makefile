deps:
	@pip install -r requirements.txt --use-mirrors

test: deps
	@nosetests -s .
