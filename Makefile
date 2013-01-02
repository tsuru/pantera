deps:
	@pip install -r requirements.txt

test: deps
	@nosetests .
