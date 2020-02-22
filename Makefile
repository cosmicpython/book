COMPOSE_ASCIIDOCTOR = docker-compose run --rm asciidoctor

prepare:
	docker-compose build

html_docker: prepare
	$(COMPOSE_ASCIIDOCTOR) asciidoctor -a stylesheet=theme/asciidoctor.local.css -a source-highlighter=pygments -a '!example-caption' *.asciidoc

html:
	asciidoctor -a stylesheet=theme/asciidoctor.local.css -a source-highlighter=pygments -a '!example-caption' *.asciidoc

test: html
	pytest tests.py --tb=short -vv

update-code:
	# git submodule update --init --recursive
	cd code && git fetch
	./checkout-branches-for-ci.py

count-todos:
	ls *.asciidoc | xargs grep -c TODO | sed  s/:/\\t/

diagrams: html
	./render-diagrams.py $(CHAP)
