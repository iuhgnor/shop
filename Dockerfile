# 丝网花售卖网站 - Docker镜像
# 基于Python 3.13的轻量级镜像

FROM python:3.13-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY pyproject.toml uv.lock ./
COPY main.py products.py ./
COPY images/ ./images/

# 安装uv（Python包管理器）
RUN pip install --no-cache-dir uv

# 使用uv安装依赖
RUN uv sync --frozen --no-dev

# 暴露Streamlit默认端口
EXPOSE 8501

# 健康检查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health')"

# 运行Streamlit应用
CMD ["uv", "run", "streamlit", "run", "main.py", \
    "--server.port=8501", \
    "--server.address=0.0.0.0", \
    "--server.headless=true", \
    "--browser.serverAddress=0.0.0.0", \
    "--browser.gatherUsageStats=false"]