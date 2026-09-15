.PHONY: check build clean

check:
	python3 scripts/validate.py

build:
	./scripts/assemble.sh

clean:
	rm -rf build
