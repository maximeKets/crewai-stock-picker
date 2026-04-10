# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Récupérer l'exécutable uv depuis l'image officielle
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Configuration de uv
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app

# Création du user sécurisé
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/home/appuser" \
    --shell "/sbin/nologin" \
    --uid "${UID}" \
    appuser

RUN chown appuser:appuser /app

# Optimisation du cache : copie stricte des fichiers de dépendances
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Copie du code source
COPY --chown=appuser:appuser . /app

# Installation du projet local
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Ajout de l'environnement virtuel au PATH
ENV PATH="/app/.venv/bin:$PATH"

USER appuser

EXPOSE 7860

# Point d'entrée direct pour lancer Gradio (sans wrapper cache temp)
CMD ["run_ui"]