# Stage 1 - Builder

FROM python:3.13-slim AS builder

LABEL stage=builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .


RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt


# Stage 2 - Runtime

FROM python:3.13-slim

LABEL maintainer="Muhammad Zaid"
LABEL project="ShopSphere"
LABEL version="1.0.0"
LABEL description="Enterprise Three-Tier E-Commerce Backend using FastAPI"
LABEL org.opencontainers.image.source="https://github.com/MuhammadZaid11"


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN groupadd -r appgroup && \
    useradd -r -g appgroup appuser


COPY --from=builder /install /usr/local


COPY app ./app

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000


HEALTHCHECK --interval=30s \
            --timeout=5s \
            --start-period=15s \
            --retries=3 \
CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

COPY --chmod=755 entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]