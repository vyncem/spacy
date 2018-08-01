FROM python:3.6.5

ENV APP_HOME=/usr/src/app

RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME

RUN pip3 install -U spacy

# Download the large English model for spaCy
RUN python3 -m spacy download en_core_web_lg

RUN pip3 install -U textacy

COPY . $APP_HOME/

ENV DATA=/data

RUN mkdir -p $DATA

CMD ["./run.py"]
