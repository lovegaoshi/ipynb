FROM tensorflow/tensorflow:2.13.0
COPY . /inaseg
WORKDIR /inaseg
RUN pip install -r /inaseg/requirements.txt
RUN apt update
RUN apt -y install ffmpeg aria2 wget nano
RUN python /inaseg/initialize.py
