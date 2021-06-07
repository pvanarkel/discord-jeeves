init:
    pip install -r requirements.txt

install:
	cp jeevesbot/env.py.dist jeevesbot/env.py

clearlog:
	rm jeeves.log

clean:
	rm jeeves.log
	rm jeevesbot/env.py
	rm -rf jeevesbot/__pycache/
	rm -rf __pycache/

lint: 
	pylint jeeves.py jeevesbot/