FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
ENV SOLR_CON=http://localhost:8983/solr/arquivo_core/

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]


