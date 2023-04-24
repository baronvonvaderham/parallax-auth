FROM python:3.10.6
WORKDIR /parallax-auth
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
