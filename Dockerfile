FROM python

COPY main.py ./app
COPY ./credentials ./app
COPY ./plugins ./app
COPY requirements.txt ./tmp

RUN pip install git+https://github.com/timgrossmann/InstaPy.git

RUN pip install -r tmp/requirements.txt