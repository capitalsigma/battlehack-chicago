

.PHONY: make-env
make-env:
	virtualenv -p python2.7 venv

start-env:
	. venv/bin/activate
