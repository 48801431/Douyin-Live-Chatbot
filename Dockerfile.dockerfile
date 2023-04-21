# 基础镜像，可以根据实际情况选择其他镜像
FROM python:3.8-slim-buster

# 安装依赖包
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# 将应用程序复制到容器中
COPY app.py config.py utils.py /app/

# 设置工作目录
WORKDIR /app

# 暴露端口
EXPOSE 5000

# 运行应用程序
CMD ["python", "app.py"]
