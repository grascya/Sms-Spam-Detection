FROM python:3.11-slim

RUN pip install pipenv

WORKDIR /app


COPY ["Pipfile","Pipfile.lock","./"]
RUN pipenv install --deploy --system

COPY . .
EXPOSE 9696

CMD ["python","back_end.py"]