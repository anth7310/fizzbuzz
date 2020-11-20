FROM python:3-onbuild

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV HTTP http://localhost:80

CMD ['python', 'main.py']