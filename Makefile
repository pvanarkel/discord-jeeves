init:
	pip install -r requirements.txt

install:
	mkdir logs
	cp jeevesbot/env.py.dist jeevesbot/env.py
	cp jeevesbot/secret.json.dist jeevesbot/secret.json

clearlog:
	rm logs/jeeves.log*

clean:
	rm logs/jeeves.log*
	rm jeevesbot/env.py
	rm jeevesbot/secret.json
	rm -rf cogs/__pycache__/
	rm -rf jeevesbot/__pycache__/
	rm -rf __pycache__/