FROM python:3.7.3

LABEL maintainer="Patrick Pedrioli" description="A container for filtering PQP files" version="0.1"

## Let apt-get know we are running in noninteractive mode
ENV DEBIAN_FRONTEND noninteractive

COPY bin/get_prophet_prob.py /usr/local/bin
COPY bin/filterpqp.py /usr/local/bin
COPY Xslt/get_protein_list.xsl /usr/local/bin

RUN apt-get update \
    && apt-get install -y --no-install-recommends xsltproc \
    && pip install --no-cache-dir pandas==1.0.1 \
    bs4==0.0.1
