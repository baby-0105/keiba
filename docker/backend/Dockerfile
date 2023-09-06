FROM python:3.10

RUN apt update \
    && apt install -y default-mysql-client \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip install -U pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt

# google-chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
apt-get update && \
apt-get install -y google-chrome-stable

# ChromeDriver
ADD https://chromedriver.storage.googleapis.com/77.0.3865.10/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
unzip chromedriver_linux64.zip
