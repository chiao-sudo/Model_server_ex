# 使用Python官方镜像作为基础镜像
FROM python:3.10-slim

# 设置工作目录为/app
WORKDIR /app

# 将当前目录中的所有文件复制到容器的工作目录中
COPY . .

# 安装依赖
RUN pip install --no-cache-dir fastapi uvicorn

# 启动FastAPI应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
