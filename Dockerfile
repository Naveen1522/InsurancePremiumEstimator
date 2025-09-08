FROM python:3.8-bookworm

WORKDIR /insurance_app

RUN python -m pip install --upgrade pip setuptools wheel

COPY requirements.txt requirements.txt

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "EstimatorFlask.py"]