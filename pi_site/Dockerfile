FROM resin/raspberry-pi-python:2.7-wheezy
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements-pi.txt
CMD ["python", "-u", "app.py"]
