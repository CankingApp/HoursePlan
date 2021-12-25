# https://hub.docker.com/_/python
FROM tiangolo/uwsgi-nginx-flask:python3.8

# 安装依赖
RUN pip install beautifulsoup4 gunicorn
RUN pip install requests gunicorn

# 将本地代码拷贝到容器内
COPY ./app /app

