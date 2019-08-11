FROM python:3.6.7
MAINTAINER Vian "Faviansyah"
RUN mkdir -p /LKNU
RUN mkdir -p /LKNU/storage/
RUN mkdir -p /LKNU/storage/log
COPY . /LKNU
RUN touch /LKNU/storage/log/app.log
RUN pip install -r /LKNU/requirements.txt
RUN pip install --upgrade pip
WORKDIR /LKNU
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]