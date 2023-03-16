init:
    pip install -r requirements.txt

install:
	mkdir logs
	cp jeevesbot/env.py.dist jeevesbot/env.py
	cp jeevesbot/secret.json.dist jeevesbot/secret.json

clearlog:
	rm jeeves.log

clean:
	rm jeeves.log
	rm jeevesbot/env.py
	rm jeevesbot/secret.json
	rm -rf jeevesbot/__pycache/
	rm -rf __pycache/

lint: 
	pylint jeeves.py jeevesbot/