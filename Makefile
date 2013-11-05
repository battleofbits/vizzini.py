.PHONY: serve install

venv:
	virtualenv venv --python=python3 --distribute

install: venv
	. venv/bin/activate; pip install -r requirements.txt

serve: venv
	. venv/bin/activate; python battle.py

test: venv
	. venv/bin/activate; flake8 battle_test.py battle.py
	. venv/bin/activate; python battle_test.py

