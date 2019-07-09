html:
	asciidoctor -a source-highlighter=pygments -a '!example-caption' *.asciidoc

test: html
	pytest tests.py --tb=short -vv

update-code:
	# git submodule update --init --recursive
	cd code && git fetch
	./checkout-branches-for-ci.py

count-todos:
	ls *.asciidoc | xargs grep -c TODO | sed  s/:/\\t/

render-diagrams:
	asciidoctor -r asciidoctor-diagram -a imagesoutdir=. images/*.asciidoc
