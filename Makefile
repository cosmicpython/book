pytopt?=


tdd:
	git ls-files | entr make test pytopt=-x


html:
	asciidoctor \
		-a stylesheet=theme/asciidoctor-clean.custom.css \
		-a source-highlighter=pygments \
		-a pygments-style=friendly \
		-a '!example-caption' \
		-a sectanchors \
		*.asciidoc

test: html
	pytest tests.py --tb=short -vv $(pytopt)

update-code:
	# git submodule update --init --recursive
	cd code && git fetch
	./checkout-branches-for-ci.py

count-todos:
	ls *.asciidoc | xargs grep -c TODO | sed  s/:/\\t/

diagrams: html
	./render-diagrams.py $(CHAP)
