FROM resin/raspberry-pi-python:2.7-wheezy
EXPOSE 5000

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements-pi.txt

CMD ["python", "-u", "app.py"]
