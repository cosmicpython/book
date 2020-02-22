FROM asciidoctor/docker-asciidoctor

RUN apk update && apk add --no-cache \
	git \
	python3 \
	py-pip \
	py-setuptools

RUN gem install pygments.rb
RUN gem install asciidoctor-diagram

RUN pip install --user pygments
