# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r /app/requirements.txt

EXPOSE 8501

ENTRYPOINT ["python","./main.py"]

CMD ["main.py"]