FROM python:rc-slim

ENV LANG C.UTF-8

# install JRE 8, python and other dependencies
RUN apt-get update && \
    apt-get -y --no-install-recommends install \
    git \
    python3.7 python3.7-venv python3.7-dev python3.7-distutil build-essential gcc\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN mkdir -p /opt/cde/venv

WORKDIR /opt/cde

COPY requirements.txt .
COPY cde_service.py .

ENV VIRTUAL_ENV=/opt/cde/venv
RUN python3.7 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip --version

RUN python3 -m pip install pip --upgrade
RUN pip install -r ./requirements.txt
RUN cde data download

CMD ["python3", "/opt/cde/cde_service.py"]