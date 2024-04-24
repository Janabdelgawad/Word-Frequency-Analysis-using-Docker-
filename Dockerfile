FROM python:alpine

WORKDIR /app

COPY python.py /app/
COPY random_paragraphs.txt /app/

RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt

CMD ["python", "python.py"]
