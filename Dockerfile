# 使用官方 Python 镜像作为基础镜像
FROM python:3.10.14

# 将工作目录设置为 /app
WORKDIR /app

# 复制当前目录中的所有文件到工作目录 /app
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 定义容器启动时运行的命令
CMD ["python", "app.py"]
