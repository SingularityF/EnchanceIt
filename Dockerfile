FROM ubuntu:bionic

WORKDIR /usr/local/EnhanceIt

ENV TZ=US/Eastern
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . .

RUN apt-get update && apt-get -y install vim python3 python3-pip curl wget unzip lsb-release apt-transport-https ca-certificates gnupg
# Install Google Cloud SDK
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - 
RUN apt-get update && apt-get -y install google-cloud-sdk
RUN gcloud auth activate-service-account --key-file /usr/local/EnhanceIt/service_account.json
ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/local/EnhanceIt/service_account.json"

RUN pip3 install -r requirements.txt

WORKDIR /usr/local/EnhanceIt/src
CMD exec gunicorn --bind :$PORT --workers 2 --timeout 0 app:app
