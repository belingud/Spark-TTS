FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt -i https://repo.huaweicloud.com/repository/pypi/simple/
RUN 

EXPOSE 7860

CMD ["python", "webui.py"]
