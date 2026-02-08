# 빌드 단계
FROM python:3.12-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-cache --no-install-project

# 실행 단계
FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY . .

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app"

EXPOSE 8000

CMD ["python", "src/main.py"]