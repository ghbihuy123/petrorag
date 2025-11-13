FROM python:3.12-slim AS base

# Build stage
FROM base AS builder

WORKDIR /app

RUN pip install uv

COPY uv.lock pyproject.toml .
RUN uv sync --no-dev --python /usr/local/bin/python

# Final stage
FROM base AS final
WORKDIR /app

COPY . .
COPY --from=builder /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH"
ENV VIRTUAL_ENV="/app/.venv"

CMD ["python", "-m", "streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
