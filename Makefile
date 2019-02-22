html:
	asciidoctor -a source-highlighter=coderay -a '!example-caption' *.asciidoc

test:
	pytest tests.py --tb=short -vv

update:
	# git submodule update --init --recursive
	cd code && git fetch
