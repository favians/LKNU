FROM python:3.6.7
MAINTAINER Vian "Faviansyah"
RUN mkdir -p /LKNU
COPY . /LKNU
RUN pip install -r /LKNU/requirements.txt
RUN pip install --upgrade pip
WORKDIR /LKNU
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]